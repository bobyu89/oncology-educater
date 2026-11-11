#!/usr/bin/env python3
"""把 handbook/ 的 Markdown 轉成單一互動網頁（學習系統）。

輸出：
  site/index.html            完整 HTML，可離線開啟（醫院網路擋外站時也能用）
  site/artifact.html         不含 <html>/<head> 外殼的版本，供發布成 Artifact 網頁
  handbook/LEARNING_PATH.md  由 handbook/learning-path.json 產生的學習路徑（給在 GitHub 上讀的人）

用法：python3 tools/build_site.py

網頁版除了章節內容，還會產生：
  學習路徑  handbook/learning-path.json 定義的站別與步驟
  測驗      各章「自我測驗」的題目轉成可作答的元件
  藥物卡    藥物篇裡 <!-- drug-cards --> 標記的表格
"""

from __future__ import annotations

import html
import json
import re
import sys
from datetime import date
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
HANDBOOK = ROOT / "handbook"
SITE = ROOT / "site"
TEMPLATE = Path(__file__).resolve().parent / "site_template.html"

CALLOUT_LABELS = {
    "important": "考試重點",
    "tip": "比喻理解",
    "warning": "臨床警示",
    "note": "院內規範",
    "caution": "待核對",
}

EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿️‍]")


def clawd(cls: str = "clawd") -> str:
    return f'<svg class="{cls}" viewBox="1 0 16 10" aria-hidden="true"><use href="#clawd-body"/></svg>'


def gh_slug(text: str, separator: str = "-") -> str:
    """模仿 GitHub 的標題錨點規則，讓 repo 內的連結在網頁版也能用。"""
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", separator)


def convert(md_text: str) -> tuple[str, list[dict]]:
    # <details> 內的 Markdown 需要 md_in_html 才會被解析
    md_text = md_text.replace("<details>", '<details markdown="1">')
    # Python-Markdown 會把空行隔開的相鄰 blockquote 併成一個；GitHub 不會。中間插註解隔開
    md_text = re.sub(r"^(> \[!(?:IMPORTANT|TIP|WARNING|NOTE|CAUTION)\])", r"<!-- -->\n\n\1", md_text, flags=re.M)
    md = markdown.Markdown(
        extensions=["extra", "sane_lists", "toc"],
        extension_configs={"toc": {"slugify": gh_slug, "toc_depth": "2-3"}},
    )
    return md.convert(md_text), md.toc_tokens


def rewrite(body: str, chapter_id: str, file_to_id: dict[str, str], chapter_file: str) -> str:
    body = EMOJI.sub("", body)

    # GitHub alert 語法 → callout；第一行粗體當作框的主題
    def callout(m: re.Match) -> str:
        kind = m.group(1).lower()
        label = CALLOUT_LABELS[kind]
        title = m.group(2)
        head = f'<blockquote class="callout callout-{kind}"><p class="callout-label">{label}</p><p>'
        if title and title.strip() not in CALLOUT_LABELS.values():
            head += f'<strong class="callout-title">{title.strip()}</strong>'
        return head

    body = re.sub(
        r"<blockquote>\s*<p>\[!(IMPORTANT|TIP|WARNING|NOTE|CAUTION)\]\s*(?:<strong>([^<]*)</strong>\s*(?:<br\s*/?>)?\s*)?",
        callout,
        body,
    )
    body = body.replace('</strong><p>', '</strong></p><p>')
    body = re.sub(r'(<strong class="callout-title">[^<]*</strong>)\s*</p>', r"\1</p>", body)

    # 標題 id 加上章節前綴，避免跨章重複
    body = re.sub(r'<(h[1-6]) id="([^"]+)"', lambda m: f'<{m.group(1)} id="{chapter_id}--{m.group(2)}"', body)

    # 改寫連結：同章 #anchor、跨章 xxx.md#anchor
    base = (HANDBOOK / chapter_file).parent

    def link(m: re.Match) -> str:
        href = html.unescape(m.group(1))
        if re.match(r"^[a-z]+:", href):
            return f'href="{html.escape(href)}" target="_blank" rel="noopener"'
        target, _, anchor = href.partition("#")
        if not target:
            return f'href="#{chapter_id}--{anchor}"'
        if target.endswith(".md"):
            try:
                rel = (base / target).resolve().relative_to(HANDBOOK).as_posix()
            except ValueError:
                return m.group(0)
            other = file_to_id.get(rel)
            if other:
                return f'href="#{other}--{anchor}"' if anchor else f'href="#{other}"'
        return m.group(0)

    body = re.sub(r'href="([^"]+)"', link, body)

    # 表格包一層，窄螢幕可在框內橫向捲動
    body = body.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    return body


def toc_html(tokens: list[dict], chapter_id: str) -> str:
    flat = []
    for t in tokens:
        flat.extend(t.get("children", []) if t["level"] == 1 else [t])
    items = [
        f'<li><a href="#{chapter_id}--{t["id"]}">{EMOJI.sub("", re.sub(r"<[^>]+>", "", t["name"]))}</a></li>'
        for t in flat
        if t["level"] == 2
    ]
    return "<ol>" + "".join(items) + "</ol>" if items else ""


def split_sections(md_text: str) -> list[tuple[str, str]]:
    """依 H2 把章節切成 (標題, 內文)；``` 區塊內的 ## 不算標題。"""
    out, title, buf, fenced = [], None, [], False
    for ln in md_text.split("\n"):
        if ln.lstrip().startswith("```"):
            fenced = not fenced
        m = None if fenced else re.match(r"^## +(.+?)\s*$", ln)
        if m:
            if title is not None:
                out.append((title, "\n".join(buf)))
            title, buf = m.group(1), []
        elif title is not None:
            buf.append(ln)
    if title is not None:
        out.append((title, "\n".join(buf)))
    return out


def reading_minutes(md: str) -> int:
    """粗估閱讀時間：去掉標記後每分鐘約 450 字（含表格的醫學內容）。"""
    text = re.sub(r"https?://\S+|[|>#*`_\-]|\s", "", md)
    return max(1, round(len(text) / 450))


def sections_meta(md_text: str, tokens: list[dict], chapter_id: str) -> list[dict]:
    flat = []
    for t in tokens:
        flat.extend(t.get("children", []) if t["level"] == 1 else [t])
    ids = [t["id"] for t in flat if t["level"] == 2]
    parts = split_sections(md_text)
    meta = []
    for (title, body), sid in zip(parts, ids):
        plain = re.sub(r"[*_`]", "", title)
        num = re.match(r"^(\d+)\.", plain)
        kind = "quiz" if "自我測驗" in plain else "refs" if "參考文獻" in plain else "read"
        meta.append(
            {
                "id": f"{chapter_id}--{sid}",
                "title": plain,
                "num": int(num.group(1)) if num else None,
                "kind": kind,
                "min": reading_minutes(body),
            }
        )
    if len(parts) != len(ids):
        print(f"warning: {chapter_id}: H2 數量與目錄不一致（{len(parts)} vs {len(ids)}）", file=sys.stderr)
    return meta


QUIZ_RE = re.compile(
    r"<p><strong>Q(\d+)\.</strong>\s*(.*?)</p>\s*((?:(?!<p><strong>Q\d+\.</strong>)(?!<details).)*?)"
    r"<p>(A\.\s.*?)</p>\s*(<details[^>]*>.*?</details>)",
    re.S,
)


def quizify(body: str, chapter_id: str) -> tuple[str, int]:
    """把「自我測驗」的題目轉成可作答的元件；格式不符的題目保留原樣並印警告。"""
    count = 0

    def one(m: re.Match) -> str:
        nonlocal count
        num, stem, extra, opts, details = m.groups()
        pieces = re.split(r"[\s　]*　[\s　]*(?=[B-E]\.\s)", opts.strip())
        letters = [p[0] for p in pieces]
        ans = re.search(r"<strong>答案：\s*([A-E])", details)
        if letters != list("ABCDE")[: len(letters)] or len(letters) < 3 or not ans or ans.group(1) not in letters:
            print(f"warning: {chapter_id} Q{num}: 選項或答案格式無法解析，保留原樣", file=sys.stderr)
            return m.group(0)
        count += 1
        buttons = "".join(
            f'<button type="button" class="quiz-opt" data-k="{p[0]}"><span class="quiz-k">{p[0]}</span>'
            f'<span class="quiz-t">{p[2:].strip()}</span></button>'
            for p in pieces
        )
        return (
            f'<div class="quiz-q" data-q="{chapter_id}:{num}" data-answer="{ans.group(1)}">'
            f'<p class="quiz-stem"><span class="quiz-no">Q{num}</span> {stem.strip()}</p>{extra}'
            f'<div class="quiz-opts" role="group" aria-label="選項">{buttons}</div>'
            f'<p class="quiz-result" hidden></p>{details}</div>'
        )

    return QUIZ_RE.sub(one, body), count


DRUG_COLS = ["name", "cls", "moa", "use", "tox", "mon"]


def drug_cards(md_text: str, chapter: dict) -> list[dict]:
    """讀出 <!-- drug-cards --> 之後的表格，一列一張卡。"""
    cards, lines = [], md_text.split("\n")
    for i, ln in enumerate(lines):
        if ln.strip() != "<!-- drug-cards -->":
            continue
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        rows = []
        while j < len(lines) and lines[j].lstrip().startswith("|"):
            rows.append([c.strip() for c in lines[j].strip().strip("|").split("|")])
            j += 1
        for row in rows[2:]:
            if len(row) != len(DRUG_COLS):
                print(f"warning: {chapter['id']}: 藥物卡欄數不符：{row[:1]}", file=sys.stderr)
                continue
            clean = [re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", re.sub(r"[*_`]", "", c)) for c in row]
            card = dict(zip(DRUG_COLS, clean))
            card["chapter"] = chapter["id"]
            card["group"] = chapter["title"].replace("藥物", "") or chapter["title"]
            card["key"] = chapter["id"] + ":" + re.sub(r"[^a-z0-9]+", "-", clean[0].split("（")[0].lower()).strip("-")
            cards.append(card)
    return cards


def resolve_path(path_cfg: dict, chapters: dict[str, dict]) -> dict:
    """把 learning-path.json 的步驟對應到實際段落 id；章節還沒寫完的步驟標成 pending。"""
    stages = []
    for st in path_cfg["stages"]:
        steps = []
        for sp in st["steps"]:
            if "kind" in sp:
                steps.append({"kind": sp["kind"], "label": sp["label"]})
                continue
            ch = chapters.get(sp["chapter"])
            if ch is None:
                raise SystemExit(f"learning-path.json：找不到章節 {sp['chapter']}")
            readable = [s for s in ch["sections"] if s["kind"] == "read"]
            if sp["sections"] == "all":
                secs = readable
            else:
                secs = []
                for want in sp["sections"]:
                    hit = [s for s in readable if (s["num"] == want if isinstance(want, int) else s["title"] == want)]
                    if not hit and ch["sections"]:
                        raise SystemExit(f"learning-path.json：{sp['chapter']} 沒有段落 {want}")
                    secs.extend(hit)
            steps.append(
                {
                    "kind": "read",
                    "label": sp["label"],
                    "chapter": sp["chapter"],
                    "chapterTitle": ch["title"],
                    "secs": [s["id"] for s in secs],
                    "min": sum(s["min"] for s in secs),
                    "pending": not ch["sections"],
                }
            )
        stages.append({"id": st["id"], "title": st["title"], "goal": st["goal"], "steps": steps, "quiz": st.get("quiz", [])})
    return {"title": path_cfg["title"], "intro": path_cfg["intro"], "passRate": path_cfg["pass_rate"], "stages": stages}


def write_path_markdown(path: dict, chapters: dict[str, dict]) -> None:
    """產生 handbook/LEARNING_PATH.md，讓在 GitHub 上讀的人也有同一份路徑。"""

    def fmt(minutes: int) -> str:
        return f"約 {minutes} 分鐘" if minutes < 90 else f"約 {minutes / 60:.1f} 小時"

    out = [
        "# 學習路徑",
        "",
        "<!-- 這個檔案由 tools/build_site.py 依 handbook/learning-path.json 產生，請不要手動修改。 -->",
        "",
        path["intro"],
        "",
        "網頁版會記錄讀到哪裡、測驗答對幾題；在 GitHub 上讀的人可以把下面的清單複製到自己的筆記打勾。",
        "",
    ]
    for st in path["stages"]:
        out += [f"## {st['title']}", "", f"**目標：** {st['goal']}", ""]
        for sp in st["steps"]:
            if sp["kind"] != "read":
                out.append(f"- [ ] {sp['label']}（網頁版的測驗中心與藥物卡）")
                continue
            ch = chapters[sp["chapter"]]
            if sp["pending"]:
                out.append(f"- [ ] {sp['label']}（撰寫中）")
                continue
            names = "、".join(s["title"] for s in ch["sections"] if s["id"] in sp["secs"])
            whole = len(sp["secs"]) == len([s for s in ch["sections"] if s["kind"] == "read"])
            scope = "整章" if whole else names
            out.append(f"- [ ] [{sp['label']}]({ch['file']})：{scope}（{fmt(sp['min'])}）")
        if st["quiz"]:
            titles = "、".join(chapters[c]["title"] for c in st["quiz"])
            out.append(f"- [ ] 本站測驗：{titles} 的自我測驗，答對率 {int(path['passRate'] * 100)}% 以上")
        out.append("")
    (HANDBOOK / "LEARNING_PATH.md").write_text("\n".join(out), encoding="utf-8")


def embed(data) -> str:
    return json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def main() -> int:
    config = json.loads((HANDBOOK / "chapters.json").read_text(encoding="utf-8"))
    path_cfg = json.loads((HANDBOOK / "learning-path.json").read_text(encoding="utf-8"))
    file_to_id = {c["file"]: c["id"] for c in config["chapters"]}
    groups = (("藥物", "藥物篇"), ("癌別", "癌別"), ("共用", "共用章節"))

    # 第一輪：轉換每一章，收集段落、測驗題數與藥物卡
    built: dict[str, dict] = {}
    drugs: list[dict] = []
    for c in config["chapters"]:
        path = HANDBOOK / c["file"]
        info = {"id": c["id"], "title": c["title"], "en": c.get("en", ""), "group": c["group"], "file": c["file"],
                "sections": [], "quiz": 0, "body": None, "toc": ""}
        if path.exists():
            md_text = path.read_text(encoding="utf-8")
            body, tokens = convert(md_text)
            body = rewrite(body, c["id"], file_to_id, c["file"])
            body, info["quiz"] = quizify(body, c["id"])
            status = c.get("status", "已查核")
            if status != "已查核":   # 還沒通過獨立查核的章節，開頭先講清楚
                note = (
                    '<blockquote class="callout callout-caution"><p class="callout-label">待核對</p>'
                    f'<p><strong class="callout-title">這一章目前的狀態：{html.escape(status)}</strong>'
                    "內容還沒有經過獨立查核。劑量、年份與試驗數字請先對照章末的原始文獻，不要直接用在臨床判斷。</p></blockquote>"
                )
                body = body.replace("</h1>", "</h1>" + note, 1)
            body = body.replace(
                "<!-- drug-cards -->",
                '<p class="to-cards"><a href="#drugs">到「藥物卡」把這張表變成翻卡練習</a></p>',
            )
            info.update(body=body, toc=toc_html(tokens, c["id"]), sections=sections_meta(md_text, tokens, c["id"]))
            drugs.extend(drug_cards(md_text, c))
        built[c["id"]] = info

    learning = resolve_path(path_cfg, built)
    write_path_markdown(learning, built)

    # 「下一章」依學習路徑的順序
    order = []
    for st in learning["stages"]:
        for sp in st["steps"]:
            if sp["kind"] == "read" and sp["chapter"] not in order:
                order.append(sp["chapter"])
    order += [c["id"] for c in config["chapters"] if c["id"] not in order]
    next_of = {cid: order[i + 1] if i + 1 < len(order) else None for i, cid in enumerate(order)}

    nav, sections = [], []
    for group, label in groups:
        members = [c for c in config["chapters"] if c["group"] == group]
        if not members:
            continue
        nav.append(f'<p class="nav-group">{label}</p><ul>')
        for c in members:
            info = built[c["id"]]
            ready = info["body"] is not None
            nav.append(
                f'<li><a href="#{c["id"]}" data-chapter="{c["id"]}">'
                f'<span class="nav-title">{c["title"]}</span>'
                f'<span class="chip" data-chip="{c["id"]}">{"" if ready else "撰寫中"}</span></a></li>'
            )
            if ready:
                body, toc = info["body"], info["toc"]
                nxt = built.get(next_of.get(c["id"]) or "")
                tail = f'，或直接讀下一章：<a href="#{nxt["id"]}">{nxt["title"]}</a>' if nxt and nxt["body"] else ""
                body += (
                    f'<p class="chapter-end">{clawd()}<span>讀完了？回到 <a href="#path">學習路徑</a> 看下一步{tail}。</span></p>'
                )
            else:
                body = (
                    f'<h1 id="{c["id"]}--top">{c["title"]}</h1>'
                    f'<p class="empty-state">{clawd()}<span class="lede">這一章還在撰寫中。</span></p>'
                )
                toc = ""
            aside = (
                f'<aside class="chapter-toc" aria-label="本章目錄"><p class="toc-label">本章目錄</p>{toc}</aside>'
                if toc
                else ""
            )
            sections.append(
                f'<section class="view chapter" id="v-{c["id"]}" data-route="{c["id"]}" data-title="{c["title"]}" hidden>'
                f'<article class="prose">{body}</article>{aside}</section>'
            )
        nav.append("</ul>")

    # 站內連結檢查：指向不存在錨點的連結印出警告
    joined = "".join(sections)
    routes = {"board", "home", "path", "quiz", "drugs", "clawd-body"}
    ids = set(re.findall(r'id="([^"]+)"', joined)) | routes | set(file_to_id.values())
    broken = sorted({h for h in re.findall(r'href="#([^"]+)"', joined) if h not in ids})
    for h in broken:
        print(f"warning: broken internal link #{h}", file=sys.stderr)

    chapters_data = [
        {k: info[k] for k in ("id", "title", "en", "group", "sections", "quiz")}
        for info in (built[c["id"]] for g, _ in groups for c in config["chapters"] if c["group"] == g)
    ]
    template = TEMPLATE.read_text(encoding="utf-8")
    page = (
        template.replace("{{TITLE}}", config["title"])
        .replace("{{SUBTITLE}}", config["subtitle"])
        .replace("{{NAV}}", "".join(nav))
        .replace("{{SECTIONS}}", joined)
        .replace("{{DATA_CHAPTERS}}", embed(chapters_data))
        .replace("{{DATA_PATH}}", embed(learning))
        .replace("{{DATA_DRUGS}}", embed(drugs))
        .replace("{{BUILD_DATE}}", date.today().isoformat())
    )

    SITE.mkdir(exist_ok=True)
    (SITE / "artifact.html").write_text(page, encoding="utf-8")
    # 離線檔與 GitHub Pages 用的完整 HTML：把 <title>、字型與樣式放進 <head>
    cut = page.index("</style>") + len("</style>")
    standalone = (
        '<!doctype html>\n<html lang="zh-Hant">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        f'<meta name="description" content="{html.escape(config["subtitle"])}">\n'
        + page[:cut]
        + "\n</head>\n<body>\n"
        + page[cut:]
        + "\n</body>\n</html>\n"
    )
    (SITE / "index.html").write_text(standalone, encoding="utf-8")
    quiz_total = sum(i["quiz"] for i in built.values())
    read_total = sum(1 for i in built.values() for x in i["sections"] if x["kind"] == "read")
    print(
        f"built {len(sections)} chapters（{read_total} 段、{quiz_total} 題、{len(drugs)} 張藥物卡）"
        " → site/index.html, site/artifact.html, handbook/LEARNING_PATH.md"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
