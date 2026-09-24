#!/usr/bin/env python3
"""Save a fetched PMC OA .txt into research/corpus as a verbatim corpus file.

Keeps the article text unchanged from the first body section to the line
before the reference list; drops journal/article metadata blocks and
references. Appends a manifest line and prints the new source_id.

Usage: save_pmc.py <pmc_txt> <type> <cells comma-separated> [--authors="A; B"] [--dry]
"""
import json, re, sys, datetime, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
corpus = root / "corpus"
manifest = corpus / "manifest.jsonl"

def meta(lines, key):
    for l in lines:
        if l.startswith(key + ":"):
            return l.split(":", 1)[1].strip()
    return ""

def main():
    path, typ, cells = sys.argv[1], sys.argv[2], sys.argv[3].split(",")
    dry = "--dry" in sys.argv
    override = next((a.split("=",1)[1] for a in sys.argv if a.startswith("--authors=")), None)
    lines = pathlib.Path(path).read_text().splitlines()
    pmcid, doi = meta(lines, "PMCID"), meta(lines, "DOI")
    existing = [json.loads(l) for l in manifest.read_text().splitlines() if l.strip()]
    for e in existing:
        if (doi and e.get("doi") == doi) or pmcid in e.get("url", ""):
            sys.exit(f"duplicate of {e['source_id']}")
    seps = [i for i, l in enumerate(lines) if "==========" in l]
    art = seps[1]
    title = next(l for l in lines[art + 1:] if l.strip() and ":" not in l[:30])
    ti = lines.index(title, art + 1)
    authors = []
    for l in lines[ti + 1:]:
        if not l.strip() or l.strip() == title:
            continue
        if re.match(r"^\d+\s", l) or l.startswith(("Article Information", "Abstract")) or len(authors) >= 40:
            break
        if re.search(r"[A-Za-z]", l) and not l.startswith("http") and len(l) < 120:
            authors.append(re.sub(r"\s+\d+(\s+\d+)*$", "", re.sub(r"https?://\S+\s*", "", l)).strip())
    year = (re.search(r"\d{4}", meta(lines, "Publication date") or meta(lines, "Electronic publication date")) or [""])[0]
    publisher = next((lines[i + 1 + k].strip() for i in [seps[0]] for k in range(1, 12)
                      if lines[i + 1 + k].strip() and ":" not in lines[i + 1 + k]), "")
    body_start = seps[2] + 1 if len(seps) > 2 else art + 1
    ref = next((i for i in range(len(lines) - 1, body_start, -1)
                if re.match(r"^(References:?|REFERENCES)\s*$", lines[i].strip())), len(lines))
    body = "\n".join(lines[body_start:ref]).strip()
    n = max([int(e["source_id"][2:]) for e in existing] + [0]) + 1
    sid = f"S-{n:04d}"
    fm = {"source_id": sid, "title": title.strip(), "authors": override or "; ".join(a for a in authors if a)[:500],
          "year": year, "url": f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/", "doi": doi,
          "publisher": publisher, "type": typ, "access": "full_text",
          "retrieved_on": datetime.date.today().isoformat(), "cells": cells}
    if dry:
        print(json.dumps(fm, indent=1)); print(body[:300]); print("...", len(body.split()), "words"); return
    head = "\n".join(f"{k}: [{', '.join(v)}]" if isinstance(v, list) else f"{k}: {json.dumps(v) if ':' in str(v) else v}"
                     for k, v in fm.items())
    (corpus / f"{sid}.md").write_text(f"---\n{head}\n---\n\n{title.strip()}\n\n"
        f"[Verbatim text from the NCBI PMC Open Access dataset ({pmcid}); journal metadata block and reference list omitted.]\n\n{body}\n")
    with manifest.open("a") as m:
        m.write(json.dumps(fm) + "\n")
    print(sid)

main()
