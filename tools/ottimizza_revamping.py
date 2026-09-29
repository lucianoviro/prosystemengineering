#!/usr/bin/env python3
"""Genera il template Elementor ottimizzato della landing "Revamping macchinari industriali".

Legge l'export XML di WordPress (Strumenti > Esporta), estrae i dati Elementor della
pagina con slug `revamping-macchinari-industriali`, applica le modifiche descritte in
02-landing-revamping-macchinari-industriali.md e scrive un template importabile in
Elementor (Template > Template salvati > Importa). Non tocca la pagina live.

Le FAQ sono lette dal file .md (tra <!-- FAQ:START --> e <!-- FAQ:END -->): stessa fonte
dello schema FAQPage generato da tools/genera_schema.py.

Se la pagina è stata modificata dopo l'export (ID o testi diversi da quelli attesi)
lo script si ferma con un messaggio: riesportare e rilanciare.

Uso:
    python3 tools/ottimizza_revamping.py export.xml            # scrive il template
    python3 tools/ottimizza_revamping.py export.xml --outline  # stampa solo i titoli prima/dopo
"""
import argparse
import copy
import html
import json
import random
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOC = ROOT / "02-landing-revamping-macchinari-industriali.md"
OUT = ROOT / "elementor" / "revamping-ottimizzata.json"

NS = {
    "wp": "http://wordpress.org/export/1.2/",
    "content": "http://purl.org/rss/1.0/modules/content/",
}
SLUG = "revamping-macchinari-industriali"
SITE = "https://prosystemengineering.com"
LANDING_ADEGUAMENTO = f"{SITE}/adeguamento-macchine-marcatura-ce-e-d-lgs-81-08/"
EURLEX_2023_1230 = "https://eur-lex.europa.eu/eli/reg/2023/1230/oj?locale=it"

ANCHOR_OLD = "richiedi-una-valutazione"  # resta dov'è (stili collegati)
ANCHOR_NEW = "contatti-revamping"        # su una sezione visibile anche su mobile
ANCHOR_SPACER_SECTION = "f5b9fc3"
CTA_BUTTONS = ["8949db4", "ab0a4d3", "c247953", "271187d"]

# id widget -> (inizio del testo atteso, nuovo tag, nuovo testo o None)
HEADINGS = {
    # l'H1 della pagina è il titolo del Revolution Slider ("PROGETTAZIONE REVAMPING MACCHINARI INDUSTRIALI")
    "581665e": ("AGGIORNA IL TUO IMPIANTO", "h2", None),
    "e31cbeb": ("QUANDO IL REVAMPING", "h2", None),
    "8c4a228": ("PROLUNGA LA VITA", "h3", None),
    "10b127a": ("MIGLIORA LE PRESTAZIONI", "h3", None),
    "0ab3b50": ("AGGIORNA TECNOLOGIA", "h3", None),
    "0c757cb": ("ADEGUAMENTO E RIPROGETTAZIONE", "h2", None),
    "22ce6b2": ("Non sostituire", "p", None),
    "fe83b55": ("COME AFFRONTIAMO", "h2", None),
    "dc86924": ("COSA POSSIAMO MIGLIORARE", "h2", None),
    "bdc7af5": ("Un intervento mirato", "p", None),
    "9b6c4d4": ("ESPERIENZA NELLA PROGETTAZIONE", "h2", None),
    "995bf65": ("Competenze multidisciplinari", "p", None),
    "55a7b14": ("PERCHÉ SCEGLIERE", "h2", None),
    "24df61e": ("REVAMPING E SICUREZZA", "h2", "REVAMPING, MARCATURA CE E SICUREZZA DELLE MACCHINE"),
    "d0da74d": ("FAQ", "h2", "DOMANDE FREQUENTI SUL REVAMPING INDUSTRIALE"),
    "ee339c0": ("HAI UN MACCHINARIO", "h2", None),
    "e25d640": ("Contattaci e raccontaci", "p", None),
    # copia mobile della sezione contatti: stessi testi, non più titoli
    "d2d7849": ("HAI UN MACCHINARIO", "p", None),
    "24bc78b": ("Contattaci e raccontaci", "p", None),
}

IMAGE_ALT = {
    "59b9f47": "Riprogettazione di una macchina industriale esistente",
    "6816ae8": "Progettazione di macchinari e impianti industriali",
    "3be9f5e": "Revamping e sicurezza delle macchine industriali",
    "3ee35fb": "Fase 1",
    "beea454": "Fase 2",
    "7771b71": "Fase 3",
    "e7b3eb5": "Fase 4",
    "cdc09a4": "Fase 5",
    "181fbe8": "Fase 6",
}

DEFINIZIONE = (
    "<p>Il <b>revamping di un macchinario industriale</b> è l'intervento con cui una macchina "
    "o un impianto già in uso viene aggiornato, modificato o riprogettato per migliorarne "
    "prestazioni, affidabilità, funzionalità e sicurezza, senza doverlo sostituire.</p>\n"
)

SICUREZZA_VECCHIO = (
    '<p class="p2">Quando l\'intervento modifica in modo sostanziale la macchina, occorre '
    "valutarne gli effetti sulla <b>Marcatura CE e sulla dichiarazione di conformità</b>. "
    "Per le macchine già presenti in azienda devono essere considerati anche gli obblighi di "
    "sicurezza previsti dal <b>D.Lgs. 81/08</b>.</p>"
)
SICUREZZA_NUOVO = (
    '<p class="p2">Una <b>modifica sostanziale</b> è una modifica, non prevista né pianificata dal '
    "fabbricante, che incide sulla sicurezza della macchina creando un nuovo pericolo o aumentando "
    "un rischio esistente. In questo caso chi esegue l'intervento assume gli obblighi del "
    "fabbricante: nuova valutazione dei rischi, Fascicolo Tecnico, dichiarazione di conformità e "
    "<b>Marcatura CE</b>. Il <b>Regolamento (UE) 2023/1230</b>, che dal <b>20 gennaio 2027</b> "
    "sostituisce la Direttiva Macchine 2006/42/CE, definisce espressamente la modifica sostanziale "
    "e comprende anche le modifiche eseguite con mezzi digitali "
    f'(<a href="{EURLEX_2023_1230}" target="_blank" rel="noopener">testo su EUR-Lex</a>).</p>\n'
    '<p class="p2">Per le macchine già presenti in azienda devono essere considerati anche gli '
    "obblighi di sicurezza previsti dal <b>D.Lgs. 81/08</b>: se la macchina non è marcata CE perché "
    "antecedente alle direttive di prodotto, valgono i requisiti dell'Allegato V. Approfondisci: "
    f'<a href="{LANDING_ADEGUAMENTO}">adeguamento delle macchine al D.Lgs. 81/08 e Marcatura CE</a>.</p>'
)

TABELLA_STILE = """<style>
.pse-tabella{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:8px 0 0}
.pse-tabella table{width:100%;min-width:640px;border-collapse:collapse;font-size:16px;line-height:1.5}
.pse-tabella caption{position:absolute;left:-9999px}
.pse-tabella th,.pse-tabella td{border:1px solid #cfdde5;padding:12px 14px;text-align:left;vertical-align:top}
.pse-tabella thead th{background:#081F39;color:#fff;font-weight:600}
.pse-tabella tbody th{background:#E3EEF3;color:#081F39;font-weight:600;width:16%}
</style>
"""
TABELLA = TABELLA_STILE + """<div class="pse-tabella"><table>
<caption>Confronto tra manutenzione, retrofit, revamping e macchina nuova</caption>
<thead><tr><th scope="col">Intervento</th><th scope="col">In cosa consiste</th><th scope="col">Quando si sceglie</th><th scope="col">Effetto sulla Marcatura CE</th></tr></thead>
<tbody>
<tr><th scope="row">Manutenzione</th><td>Ripristina o preserva il corretto funzionamento della macchina.</td><td>Guasti, usura, controlli periodici.</td><td>Di norma nessuno: la macchina resta com'è.</td></tr>
<tr><th scope="row">Retrofit</th><td>Sostituzione o integrazione di specifici componenti tecnologici.</td><td>Aggiornare una macchina valida con un intervento mirato.</td><td>Da valutare caso per caso.</td></tr>
<tr><th scope="row">Revamping</th><td>Revisione progettuale più ampia: funzionalità, prestazioni, affidabilità e sicurezza della macchina nel suo complesso.</td><td>Struttura ancora valida ma non più adeguata alle esigenze produttive o di sicurezza.</td><td>Da valutare sempre: se la modifica è sostanziale chi la esegue assume gli obblighi del fabbricante.</td></tr>
<tr><th scope="row">Macchina nuova</th><td>Sostituzione completa dell'impianto.</td><td>Struttura compromessa o processo produttivo completamente cambiato.</td><td>Marcatura CE a carico del fabbricante della nuova macchina.</td></tr>
</tbody></table></div>"""

CONFRONTO_INTRO = (
    "<p>Manutenzione, retrofit e revamping si usano spesso come sinonimi, ma indicano interventi "
    "di portata diversa. Per la normativa conta soprattutto un aspetto: se la modifica è "
    "<b>sostanziale</b> oppure no.</p>"
)


# ----------------------------------------------------------------------------- utilità
def load_page(xml_path):
    root = ET.parse(xml_path).getroot()
    for it in root.find("channel").findall("item"):
        if it.findtext("wp:post_name", namespaces=NS) == SLUG and it.findtext("wp:post_type", namespaces=NS) == "page":
            for m in it.findall("wp:postmeta", namespaces=NS):
                if m.findtext("wp:meta_key", namespaces=NS) == "_elementor_data":
                    return json.loads(m.findtext("wp:meta_value", namespaces=NS))
    sys.exit(f"Pagina '{SLUG}' con dati Elementor non trovata nell'export")


def index(elements):
    found = {}

    def walk(e):
        found[e["id"]] = e
        for c in e.get("elements", []):
            walk(c)

    for e in elements:
        walk(e)
    return found


def settings(e):
    """Elementor salva `[]` (lista vuota PHP) al posto di `{}`: lo normalizza."""
    if not isinstance(e.get("settings"), dict):
        e["settings"] = {}
    return e["settings"]


def strip(s):
    s = re.sub(r"<br\s*/?>", " ", s or "")
    s = re.sub(r"<[^>]+>", "", s)
    return " ".join(html.unescape(s).split())


def md_inline_to_html(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', text)
    return re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)


def read_faq():
    md = DOC.read_text(encoding="utf-8")
    block = re.search(r"<!-- FAQ:START -->(.*?)<!-- FAQ:END -->", md, re.S)
    if not block:
        sys.exit(f"Blocco FAQ non trovato in {DOC.name}")
    faq = []
    for chunk in re.split(r"^#### ", block.group(1), flags=re.M)[1:]:
        question, _, answer = chunk.partition("\n")
        faq.append((question.strip(), md_inline_to_html(" ".join(answer.split()))))
    return faq


class Ids:
    def __init__(self, taken):
        self.taken = set(taken)
        self.rng = random.Random(6969)

    def new(self):
        while True:
            i = "%07x" % self.rng.getrandbits(28)
            if i not in self.taken:
                self.taken.add(i)
                return i


def outline(elements):
    """Titoli nell'ordine del documento: (livello, testo, origine)."""
    rows = []

    def walk(e):
        s = e.get("settings") if isinstance(e.get("settings"), dict) else {}
        w = e.get("widgetType")
        if w == "heading":
            tag = s.get("header_size", "h2")
            rows.append((tag, strip(s.get("title")), "titolo"))
        elif w == "icon-box":
            rows.append((s.get("title_size", "h3"), strip(s.get("title_text")), "icon box"))
        elif w == "text-editor":
            for tag, txt in re.findall(r"<(h[1-6])[^>]*>(.*?)</\1>", s.get("editor", ""), re.S):
                if strip(txt):
                    rows.append((tag, strip(txt), "testo"))
        elif w == "accordion":
            tag = s.get("title_html_tag", "div")
            for t in s.get("tabs", []):
                rows.append((tag, strip(t.get("tab_title")), "faq"))
        for c in e.get("elements", []):
            walk(c)

    for e in elements:
        walk(e)
    return rows


def print_outline(title, elements):
    rows = outline(elements)
    print(f"\n{title}")
    for tag, txt, src in rows:
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            print(f"  {tag.upper():<3} {'  ' * (int(tag[1]) - 1)}{txt[:80]}  [{src}]")
    print(f"  -> H1: {sum(1 for r in rows if r[0] == 'h1')}, H2: {sum(1 for r in rows if r[0] == 'h2')}, "
          f"H3: {sum(1 for r in rows if r[0] == 'h3')}, H4+: {sum(1 for r in rows if r[0] in ('h4', 'h5', 'h6'))}")


def expect(cond, msg):
    if not cond:
        sys.exit(f"La pagina è cambiata rispetto a quanto atteso: {msg}\n"
                 "Riesportare da WordPress e ricontrollare le modifiche in tools/ottimizza_revamping.py")


# ----------------------------------------------------------------------------- trasformazione
def optimize(elements):
    ids = Ids(index(elements))
    by = index(elements)

    # 1. titoli
    for wid, (starts, tag, new_text) in HEADINGS.items():
        e = by.get(wid)
        expect(e and e.get("widgetType") == "heading", f"heading {wid} non trovato")
        s = settings(e)
        expect(strip(s.get("title")).startswith(starts), f"heading {wid}: atteso '{starts}…', trovato '{strip(s.get('title'))[:40]}'")
        s["header_size"] = tag
        if new_text:
            s["title"] = new_text

    # 2. definizione in apertura
    s = settings(by["34683cc"])
    expect(s["editor"].startswith("<p>Prosystem Engineering affianca"), "testo introduttivo 34683cc")
    s["editor"] = DEFINIZIONE + s["editor"]

    # 3. sezione sicurezza: definizione di modifica sostanziale e link alla landing adeguamento
    s = settings(by["12462f6"])
    expect(SICUREZZA_VECCHIO in s["editor"], "testo del blocco 'Marcatura CE e D.Lgs. 81/08' (12462f6)")
    s["editor"] = s["editor"].replace(SICUREZZA_VECCHIO, SICUREZZA_NUOVO)

    # 4. FAQ: titoli H3, senza numerazione, con le nuove domande
    acc = settings(by["ab30225"])
    old_tabs = acc.get("tabs", [])
    expect(len(old_tabs) == 7, f"attese 7 FAQ, trovate {len(old_tabs)}")
    faq = read_faq()
    tabs = []
    for n, (q, a) in enumerate(faq):
        tab = copy.deepcopy(old_tabs[n]) if n < len(old_tabs) else {"_id": ids.new()}
        tab["tab_title"] = q
        tab["tab_content"] = f"<p>{a}</p>"
        tabs.append(tab)
    acc["tabs"] = tabs
    acc["title_html_tag"] = "h3"

    # 5. testi alternativi
    for wid, alt in IMAGE_ALT.items():
        e = by[wid]
        expect(e.get("widgetType") == "image", f"image {wid} non trovata")
        settings(e)["image"]["alt"] = alt

    # 6. ancora sempre visibile per i CTA (la sezione con l'ID originale è nascosta su mobile)
    expect(settings(by["81f6811"]).get("hide_mobile") == "hidden-mobile"
           and settings(by["81f6811"]).get("_element_id") == ANCHOR_OLD, "sezione contatti desktop 81f6811")
    settings(by[ANCHOR_SPACER_SECTION])["_element_id"] = ANCHOR_NEW
    for wid in CTA_BUTTONS:
        link = settings(by[wid])["creative_button_link_url"]
        expect(link.get("url") == f"#{ANCHOR_OLD}", f"link del bottone {wid}")
        link["url"] = f"#{ANCHOR_NEW}"

    # 7. nuova sezione di confronto (dopo la sezione "quando conviene" e il suo spaziatore)
    def widget(kind, **st):
        return {"id": ids.new(), "elType": "widget", "settings": st, "elements": [], "widgetType": kind}

    heading = copy.deepcopy(by["fe83b55"])  # stesso stile dei titoli di sezione
    heading["id"] = ids.new()
    settings(heading).update({"title": "REVAMPING, RETROFIT O MACCHINA NUOVA?", "header_size": "h2"})
    intro = widget("text-editor", editor=CONFRONTO_INTRO)
    tabella = widget("html", html=TABELLA)
    sezione = {
        "id": ids.new(), "elType": "section", "isInner": False,
        "settings": {"_element_id": "revamping-retrofit"},
        "elements": [{"id": ids.new(), "elType": "column", "isInner": False,
                      "settings": {"_column_size": 100, "_inline_size": None},
                      "elements": [heading, intro, tabella]}],
    }
    spaziatore = copy.deepcopy(by["f21e83a"])

    def renew(e):
        e["id"] = ids.new()
        for c in e.get("elements", []):
            renew(c)

    renew(spaziatore)
    pos = next(i for i, e in enumerate(elements) if e["id"] == "f21e83a")
    elements[pos + 1:pos + 1] = [sezione, spaziatore]
    return elements


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("xml", help="export XML di WordPress")
    ap.add_argument("--outline", action="store_true", help="stampa solo i titoli prima/dopo, senza scrivere il file")
    args = ap.parse_args()

    original = load_page(args.xml)
    before = copy.deepcopy(original)
    after = optimize(copy.deepcopy(original))

    print_outline("PRIMA", before)
    print_outline("DOPO", after)
    if args.outline:
        return

    ids = [i for i in index(after)]
    assert len(ids) == len(set(ids)), "ID Elementor duplicati"
    template = {
        "version": "0.4",
        "title": "Revamping macchinari industriali (ottimizzata)",
        "type": "page",
        "content": after,
        "page_settings": [],
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(template, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"\nscritto {OUT.relative_to(ROOT)} ({OUT.stat().st_size // 1024} KB, {len(ids)} elementi)")


if __name__ == "__main__":
    main()
