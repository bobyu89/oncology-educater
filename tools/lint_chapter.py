#!/usr/bin/env python3
"""檢查手冊章節是否符合 docs/STYLE_GUIDE.md。

用法：
  python3 tools/lint_chapter.py handbook/01-lung-cancer.md --cancer
  python3 tools/lint_chapter.py handbook/00-shared/*.md
  python3 tools/lint_chapter.py --all          # 全部章節

--cancer  同時檢查 13 段固定架構（0–12）。
退出碼：有 ERROR 為 1，只有 WARN 為 0。
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_site import gh_slug  # noqa: E402

EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
CALLOUTS = {"IMPORTANT", "TIP", "WARNING", "NOTE", "CAUTION"}
CANCER_SECTIONS = [
    "速查卡", "流行病學", "病理", "診斷與分期", "治療策略", "常用處方", "副作用",
    "專師實務", "腫瘤急症", "健保給付", "個案練習", "自我測驗", "參考文獻",
]
LEAK = re.compile(r"\[(?:VERIFIED|PARTIAL|UNVERIFIED)\]|\bFDA label\]|\[A\]|\[FT\]|\[PLS\]|critic additions", re.I)
PLACEHOLDER = re.compile(r"\bTODO\b|\bTBD\b|\bXXX\b|lorem ipsum|<!-- TODO", re.I)


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z]", "", s)


class Report:
    def __init__(self, name: str):
        self.name, self.items = name, []

    def add(self, level: str, line: int, msg: str):
        self.items.append((level, line, msg))

    def print(self) -> tuple[int, int]:
        errs = sum(1 for i in self.items if i[0] == "ERROR")
        warns = sum(1 for i in self.items if i[0] == "WARN")
        for level, line, msg in sorted(self.items, key=lambda x: (x[1], x[0])):
            print(f"{self.name}:{line}: {level}: {msg}")
        return errs, warns


def split_code(lines: list[str]) -> list[bool]:
    """每行是否在 ``` 程式碼區塊內。"""
    inside, flags = False, []
    for ln in lines:
        if ln.lstrip().startswith("```"):
            flags.append(True)
            inside = not inside
        else:
            flags.append(inside)
    return flags


def headings(lines, in_code):
    out = []
    for i, ln in enumerate(lines):
        if in_code[i]:
            continue
        m = re.match(r"^(#{1,6}) +(.+?)\s*$", ln)
        if m:
            out.append((i + 1, len(m.group(1)), m.group(2)))
    return out


def slug_of(heading: str) -> str:
    h = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading)
    h = re.sub(r"[*_`]", "", h)
    return gh_slug(h)


def check(path: Path, cancer: bool) -> Report:
    rel = path.relative_to(ROOT).as_posix()
    rep = Report(rel)
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    in_code = split_code(lines)
    heads = headings(lines, in_code)

    # --- 架構 ---
    h2 = [(n, t) for n, lv, t in heads if lv == 2]
    if cancer:
        nums = []
        for n, t in h2:
            m = re.match(r"(\d+)\.\s*(.+)", t)
            if m:
                nums.append((int(m.group(1)), m.group(2), n))
        if [x[0] for x in nums] != list(range(13)):
            rep.add("ERROR", 1, f"H2 編號應為 0–12 連續，實際：{[x[0] for x in nums]}")
        for (num, title, n), key in zip(nums, CANCER_SECTIONS):
            if key not in title:
                rep.add("ERROR", n, f"第 {num} 段標題應含「{key}」，實際：{title}")
        if not any(lv == 1 for _, lv, _ in heads):
            rep.add("ERROR", 1, "缺少 H1 章名")

    # 空段落
    h2_lines = [n for n, _ in h2] + [len(lines) + 1]
    for (n, t), nxt in zip(h2, h2_lines[1:]):
        body = [x for x in lines[n:nxt - 1] if x.strip() and not x.strip().startswith("<!--")]
        if len(body) < 3:
            rep.add("ERROR", n, f"段落內容過少：{t}")

    # --- 逐行 ---
    ref_start = None
    for n, t in h2:
        if "參考文獻" in t:
            ref_start = n
    for i, ln in enumerate(lines, 1):
        if in_code[i - 1]:
            continue
        if EMOJI.search(ln):
            rep.add("ERROR", i, "含 emoji")
        if LEAK.search(ln):
            rep.add("ERROR", i, f"研究筆記的內部標籤外洩：{LEAK.search(ln).group(0)}")
        if PLACEHOLDER.search(ln):
            rep.add("WARN", i, "含 TODO／TBD 占位文字")
        if "<!-- status: pending -->" in ln:
            rep.add("WARN", i, "仍有 status: pending 標記")

    # --- 提示框 ---
    for i, ln in enumerate(lines):
        if in_code[i]:
            continue
        m = re.match(r"^> \[!(\w+)\]\s*$", ln)
        if m:
            if m.group(1) not in CALLOUTS:
                rep.add("ERROR", i + 1, f"未知提示框類型 {m.group(1)}")
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if not re.match(r"^> \*\*[^*]+\*\*\s*$", nxt):
                rep.add("WARN", i + 2, "提示框第二行應為單獨一行粗體主題（> **主題**）")
            if i + 2 < len(lines) and not lines[i + 2].startswith(">"):
                rep.add("WARN", i + 2, "提示框只有標題沒有內容")
        elif re.match(r"^> \[!", ln):
            rep.add("ERROR", i + 1, "提示框語法錯誤（> [!TYPE] 後不可接其他文字）")

    # --- 表格 ---
    i = 0
    while i < len(lines):
        if not in_code[i] and re.match(r"^\s*\|", lines[i]):
            j = i
            while j < len(lines) and re.match(r"^\s*\|", lines[j]) and not in_code[j]:
                j += 1
            counts = [len(re.findall(r"(?<!\\)\|", lines[k])) for k in range(i, j)]
            if len(set(counts)) > 1:
                bad = [k + 1 for k, c in zip(range(i, j), counts) if c != counts[0]]
                rep.add("ERROR", i + 1, f"表格欄數不一致（首列 {counts[0]} 個 |），不一致的行：{bad[:6]}")
            if j - i >= 2 and not re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
                rep.add("ERROR", i + 1, "表格第二列不是分隔線")
            i = j
        else:
            i += 1

    # --- details ---
    opens = sum(1 for k, ln in enumerate(lines) if not in_code[k] and ln.strip() == "<details>")
    closes = sum(1 for k, ln in enumerate(lines) if not in_code[k] and ln.strip() == "</details>")
    if opens != closes:
        rep.add("ERROR", 1, f"<details> 與 </details> 數量不符（{opens} vs {closes}）")
    for k, ln in enumerate(lines):
        if ln.strip() == "<details>" and not (k + 1 < len(lines) and lines[k + 1].strip().startswith("<summary>")):
            rep.add("ERROR", k + 1, "<details> 後必須緊接 <summary>")

    # --- 測驗 ---
    quiz = [n for n, t in h2 if "自我測驗" in t]
    if quiz:
        qs = [(k + 1) for k, ln in enumerate(lines) if re.match(r"^\*\*Q\d+\.\*\*", ln)]
        for q in qs:
            window = "\n".join(lines[q - 1:q + 14])
            if not re.search(r"A\..*B\..*C\.", window):
                rep.add("ERROR", q, "測驗題缺少 A/B/C 選項行")
            if "<details>" not in window or "答案" not in window:
                rep.add("ERROR", q, "測驗題缺少答案與詳解摺疊區塊")
        if cancer and len(qs) < 16:
            rep.add("ERROR", quiz[0], f"測驗題只有 {len(qs)} 題，癌別章至少 16 題")
        nums = [int(re.match(r"^\*\*Q(\d+)", lines[q - 1]).group(1)) for q in qs]
        if nums and nums != list(range(1, len(nums) + 1)):
            rep.add("ERROR", quiz[0], f"題號不連續：{nums}")

    # --- 連結 ---
    own = {slug_of(t) for _, _, t in heads}
    for i, ln in enumerate(lines, 1):
        if in_code[i - 1]:
            continue
        for m in re.finditer(r"\]\(([^)\s]+)\)", ln):
            href = m.group(1)
            if re.match(r"^[a-z]+:", href):
                continue
            target, _, anchor = href.partition("#")
            if not target:
                if anchor and anchor not in own:
                    rep.add("ERROR", i, f"站內錨點不存在：#{anchor}")
                continue
            tp = (path.parent / target).resolve()
            if not tp.exists():
                rep.add("ERROR", i, f"連結檔案不存在：{target}")
            elif anchor and tp.suffix == ".md":
                tl = tp.read_text(encoding="utf-8").split("\n")
                slugs = {slug_of(t) for _, _, t in headings(tl, split_code(tl))}
                if anchor not in slugs:
                    rep.add("ERROR", i, f"連結錨點不存在：{target}#{anchor}")

    # --- 引用與文獻表 ---
    if ref_start:
        body = "\n".join(lines[: ref_start - 1])
        ref_text = "\n".join(lines[ref_start:])
        entries = [e.strip() for e in re.split(r"\n\s*\n", ref_text) if e.strip()]
        entries = [e for e in entries if not e.startswith(("APA", "<!--", "---"))]
        refs = []
        for e in entries:
            first = re.split(r"[,.]", e, maxsplit=1)[0]
            y = re.search(r"\((\d{4})[a-z]?[,)]", e)
            refs.append((norm(first), y.group(1) if y else "", e))
            if not re.search(r"doi\.org|PMID|https?://", e):
                rep.add("WARN", ref_start, f"文獻缺 DOI／PMID／網址：{e[:50]}")
        cited = set()
        cite_re = re.compile(
            r"(?<![A-Za-z])([A-ZÀ-Ý][A-Za-zÀ-ÿ'’\-]+)(?: et al\.| (?:&|and) [A-ZÀ-Ý][A-Za-zÀ-ÿ'’\-]+)?,\s*((?:19|20)\d{2})[a-z]?"
        )
        for m in cite_re.finditer(body):
            name, year = m.group(1), m.group(2)
            if name.isupper() or name in {"Version", "Table", "Stage", "Phase", "Grade", "Cycle"}:
                continue
            line_no = body[: m.start()].count("\n") + 1
            n = norm(name)
            hit = [r for r in refs if r[1] == year and (r[0].endswith(n) or n in r[0])]
            if hit:
                cited.add(hit[0][2])
            else:
                rep.add("ERROR", line_no, f"內文引用 {name} {year} 在文獻表找不到")
        for _, _, e in refs:
            if e not in cited:
                rep.add("WARN", ref_start, f"文獻表有、內文未引用：{e[:60]}")
    elif cancer or "00-shared" in rel:
        rep.add("ERROR", 1, "缺少「參考文獻」段落")
    return rep


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--cancer", action="store_true")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--quiet-warn", action="store_true", help="不印 WARN")
    a = ap.parse_args()
    targets: list[tuple[Path, bool]] = []
    if a.all:
        for p in sorted((ROOT / "handbook").glob("0[1-9]-*.md")):
            targets.append((p, True))
        for p in sorted((ROOT / "handbook" / "00-shared").glob("*.md")):
            targets.append((p, False))
    for f in a.files:
        targets.append((Path(f).resolve(), a.cancer))
    if not targets:
        ap.print_help()
        return 2
    total_err = total_warn = 0
    for p, cancer in targets:
        rep = check(p, cancer)
        if a.quiet_warn:
            rep.items = [i for i in rep.items if i[0] == "ERROR"]
        e, w = rep.print()
        total_err += e
        total_warn += w
        print(f"== {p.relative_to(ROOT)}: {e} error, {w} warn")
    return 1 if total_err else 0


if __name__ == "__main__":
    sys.exit(main())
