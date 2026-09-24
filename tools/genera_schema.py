#!/usr/bin/env python3
"""Genera gli snippet JSON-LD da incollare in WordPress/Elementor.

- schema/organization.html      <- schema/src/organization.json
- schema/<pagina>.html          <- schema/src/<pagina>.json (Service)
                                   + FAQ lette dal file .md della landing,
                                   tra <!-- FAQ:START --> e <!-- FAQ:END -->

Così il testo delle FAQ nello schema è identico a quello visibile in pagina.
Uso: python3 tools/genera_schema.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "schema" / "src"
OUT = ROOT / "schema"


def plain(text):
    """Toglie il markdown inline (link, grassetto, corsivo)."""
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    return " ".join(text.split())


def read_faq(md_path):
    md = md_path.read_text(encoding="utf-8")
    block = re.search(r"<!-- FAQ:START -->(.*?)<!-- FAQ:END -->", md, re.S)
    if not block:
        sys.exit(f"Blocco FAQ non trovato in {md_path.name}")
    faq = []
    for chunk in re.split(r"^#### ", block.group(1), flags=re.M)[1:]:
        question, _, answer = chunk.partition("\n")
        faq.append((plain(question), plain(answer)))
    return faq


def script_tag(data):
    body = json.dumps(data, ensure_ascii=False, indent=2).replace("</", "<\\/")
    return f'<script type="application/ld+json">\n{body}\n</script>\n'


def write(name, data):
    html = script_tag(data)
    (OUT / f"{name}.html").write_text(html, encoding="utf-8")
    for marker in ("[[", "SOSTITUIRE"):
        if marker in html:
            print(f"ATTENZIONE: {name}.html contiene '{marker}': completare prima di pubblicare")
    print(f"scritto schema/{name}.html")


def main():
    write("organization", json.loads((SRC / "organization.json").read_text(encoding="utf-8")))

    for src in sorted(SRC.glob("*.json")):
        if src.stem == "organization":
            continue
        page = json.loads(src.read_text(encoding="utf-8"))
        url = page["url"]
        service = {"@id": f"{url}#service", **page["service"], "url": url}
        faq = read_faq(ROOT / page["faq_source"])
        faq_page = {
            "@type": "FAQPage",
            "@id": f"{url}#faq",
            "url": url,
            "inLanguage": "it-IT",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": a},
                }
                for q, a in faq
            ],
        }
        write(src.stem, {"@context": "https://schema.org", "@graph": [service, faq_page]})


if __name__ == "__main__":
    main()
