#!/usr/bin/env python3
"""把 handbook/ 的 Markdown 轉成單一互動網頁。

輸出：
  site/index.html     完整 HTML，可離線開啟（醫院網路擋外站時也能用）
  site/artifact.html  不含 <html>/<head> 外殼的版本，供發布成 Artifact 網頁

用法：python3 tools/build_site.py

章節狀態：在某個 `## N. 標題` 段落內放 `<!-- status: pending -->`，首頁進度表會標成「待補」。
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

# 每個癌別章節固定的 13 段（對應 docs/STYLE_GUIDE.md §2）
TEMPLATE_SECTIONS = ["速查", "流病", "病理", "分期", "治療", "處方", "副作用", "實務", "急症", "健保", "個案", "測驗", "文獻"]

EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿️‍]")


def clawd(cls: str = "clawd") -> str:
    return f'<svg class="{cls}" viewBox="1 0 16 10" aria-hidden="true"><use href="#clawd-body"/></svg>'


def gh_slug(text: str, separator: str = "-") -> str:
    """模仿 GitHub 的標題錨點規則，讓 repo 內的連結在網頁版也能用。"""
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", separator)


def section_status(md_text: str) -> list[str]:
    """回傳 13 段各自的狀態：done / pending / empty。"""
    status = ["empty"] * len(TEMPLATE_SECTIONS)
    parts = re.split(r"^## (\d+)\.", md_text, flags=re.M)
    for i in range(1, len(parts) - 1, 2):
        n = int(parts[i])
        if 0 <= n < len(status):
            status[n] = "pending" if "<!-- status: pending -->" in parts[i + 1] else "done"
    return status


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


def progress_table(rows: list[tuple[dict, list[str]]]) -> str:
    labels = {"done": "完成", "pending": "待補", "empty": "未開始"}
    head = "".join(f"<th scope=\"col\">{s}</th>" for s in TEMPLATE_SECTIONS)
    body = []
    for c, status in rows:
        cells = "".join(
            f'<td><span class="cell cell-{s}" title="{TEMPLATE_SECTIONS[i]}：{labels[s]}"></span>'
            f'<span class="sr-only">{TEMPLATE_SECTIONS[i]}：{labels[s]}</span></td>'
            for i, s in enumerate(status)
        )
        done = status.count("done")
        body.append(
            f'<tr><th scope="row"><a href="#{c["id"]}">{c["title"]}</a></th>{cells}'
            f'<td class="num">{done}/{len(status)}</td></tr>'
        )
    return (
        '<div class="table-wrap progress"><table><thead><tr><th scope="col">癌別</th>'
        f'{head}<th scope="col" class="num">完成</th></tr></thead><tbody>{"".join(body)}</tbody></table></div>'
    )


def main() -> int:
    config = json.loads((HANDBOOK / "chapters.json").read_text(encoding="utf-8"))
    file_to_id = {c["file"]: c["id"] for c in config["chapters"]}

    ordered = [c for g in ("癌別", "共用") for c in config["chapters"] if c["group"] == g]
    next_of = {c["id"]: ordered[i + 1] if i + 1 < len(ordered) else None for i, c in enumerate(ordered)}

    nav, sections, progress = [], [], []
    for group, label in (("癌別", "癌別"), ("共用", "共用章節")):
        nav.append(f'<p class="nav-group">{label}</p><ul>')
        for c in (c for c in config["chapters"] if c["group"] == group):
            path = HANDBOOK / c["file"]
            ready = path.exists()
            status = c["status"] if ready else "規劃中"
            nav.append(
                f'<li><a href="#{c["id"]}" data-chapter="{c["id"]}">'
                f'<span class="nav-title">{c["title"]}</span>'
                f'<span class="chip{" chip-active" if ready else ""}">{status}</span></a></li>'
            )
            md_text = path.read_text(encoding="utf-8") if ready else ""
            if group == "癌別":
                progress.append((c, section_status(md_text)))
            if ready:
                body, tokens = convert(md_text)
                body = rewrite(body, c["id"], file_to_id, c["file"])
                toc = toc_html(tokens, c["id"])
            else:
                body = (
                    f'<h1 id="{c["id"]}--top">{c["title"]}</h1>'
                    f'<p class="empty-state">{clawd()}<span class="lede">這一章還在規劃中。'
                    "肺癌樣板確認後，會照同一套 13 段架構撰寫。</span></p>"
                )
                toc = ""
            nxt = next_of[c["id"]]
            if ready and nxt:
                body += (
                    f'<p class="chapter-end">{clawd()}<span>讀完了？下一章：'
                    f'<a href="#{nxt["id"]}">{nxt["title"]}</a>，或回到 <a href="#home">總覽與進度</a>。</span></p>'
                )
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
    ids = set(re.findall(r'id="([^"]+)"', joined)) | {"home", "clawd-body"} | set(file_to_id.values())
    broken = sorted({h for h in re.findall(r'href="#([^"]+)"', joined) if h not in ids})
    for h in broken:
        print(f"warning: broken internal link #{h}", file=sys.stderr)

    template = TEMPLATE.read_text(encoding="utf-8")
    page = (
        template.replace("{{TITLE}}", config["title"])
        .replace("{{SUBTITLE}}", config["subtitle"])
        .replace("{{NAV}}", "".join(nav))
        .replace("{{PROGRESS}}", progress_table(progress))
        .replace("{{SECTIONS}}", "".join(sections))
        .replace("{{BUILD_DATE}}", date.today().isoformat())
    )

    SITE.mkdir(exist_ok=True)
    (SITE / "artifact.html").write_text(page, encoding="utf-8")
    standalone = (
        '<!doctype html>\n<html lang="zh-Hant">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        "</head>\n<body>\n" + page + "\n</body>\n</html>\n"
    )
    (SITE / "index.html").write_text(standalone, encoding="utf-8")
    print(f"built {len(sections)} chapters → site/index.html, site/artifact.html")
    return 0


if __name__ == "__main__":
    sys.exit(main())
