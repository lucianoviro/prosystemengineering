#!/usr/bin/env python3
"""Genera il template Elementor ottimizzato della landing "Adeguamento macchine, Marcatura CE e D.Lgs. 81/08".

Stesso metodo di ottimizza_revamping.py (di cui riusa le funzioni): legge l'export XML di
WordPress, applica le modifiche descritte in 03-landing-adeguamento-macchine-dlgs-81-08.md e
scrive un template importabile in Elementor. Non tocca la pagina live.

Le FAQ sono lette dal file .md; lo schema Service + FAQPage è generato dagli stessi dati e
incorporato nella pagina come widget HTML.

Se la pagina è stata modificata dopo l'export (ID o testi diversi da quelli attesi) lo script
si ferma con un messaggio: riesportare e rilanciare.

Uso:
    python3 tools/ottimizza_adeguamento.py export.xml            # scrive il template
    python3 tools/ottimizza_adeguamento.py export.xml --outline  # stampa solo i titoli prima/dopo
"""
import argparse
import copy
import json
import sys
from pathlib import Path

import genera_schema
import ottimizza_revamping as base

ROOT = base.ROOT
base.SLUG = "adeguamento-macchine-marcatura-ce-e-d-lgs-81-08"
base.DOC = ROOT / "03-landing-adeguamento-macchine-dlgs-81-08.md"
OUT = ROOT / "elementor" / "adeguamento-ottimizzata.json"
SCHEMA_SRC = ROOT / "schema" / "src" / "adeguamento-macchine-marcatura-ce-dlgs-81-08.json"

SITE = base.SITE
LANDING_REVAMPING = f"{SITE}/revamping-macchinari-industriali/"
EURLEX_2023_1230 = base.EURLEX_2023_1230
NORMATTIVA_81 = "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2008-04-09;81"
AUTORE = "Ingegnere Massimo Cosso"
AUTORE_LINK = "https://it.linkedin.com/in/massimo-cosso-b6415635"
DATA_AGGIORNAMENTO = "29 settembre 2026"

# id widget -> (inizio del testo atteso, nuovo tag, nuovo testo o None)
# L'H1 della pagina è il titolo dello slider; nel corpo non resta nessun H1.
HEADINGS = {
    "581665e": ("LA MARCATURA CE NON È", "h2", None),
    "e31cbeb": ("QUANDO È NECESSARIO", "h2", None),
    "f186e4a": ("ADEGUAMENTO DELLE MACCHINE", "h2", None),
    "22ce6b2": ("Verifica dei requisiti", "h3", None),
    "805bc45": ("VERIFICA DELLA MARCATURA CE", "h2", None),
    "fe83b55": ("COME AFFRONTIAMO", "h2", None),
    "9b6c4d4": ("ADEGUAMENTO “CHIAVI IN MANO”", "h2", None),
    "995bf65": ("Dall’individuazione del rischio", "p", None),
    "dc86924": ("MACCHINE CON E SENZA", "h2", None),
    "bdc7af5": ("Ogni macchina richiede", "p", None),
    "24df61e": ("AUDIT DI SICUREZZA", "h2", None),
    "afeb4e4": ("Conosci lo stato", "p", None),
    "ddbdf2b": ("ESPERIENZA NELLA SICUREZZA", "h2", None),
    "55a7b14": ("PERCHÉ SCEGLIERE", "h2", None),
    "d0da74d": ("FAQ", "h2", "DOMANDE FREQUENTI SULL’ADEGUAMENTO DELLE MACCHINE"),
    "ee339c0": ("DEVI VERIFICARE", "h2", None),
    "e25d640": ("Contattaci, partiremo", "p", None),
}
# copia mobile della sezione contatti: viene eliminata, non serve declassare i titoli
MOBILE_SECTION = "f6beb16"
DESKTOP_SECTION = "81f6811"

DEFINIZIONE = (
    '<p class="p1"><span class="s1">L’<b>adeguamento di una macchina</b> alle norme di sicurezza consiste '
    "nel verificarne la conformità ai requisiti applicabili e, dove necessario, nell’intervenire con ripari, "
    "dispositivi di protezione, modifiche ai comandi, segnaletica e istruzioni, fino a documentare che può "
    "essere usata in sicurezza. L’obbligo ricade sul datore di lavoro, che risponde della sicurezza di tutte "
    "le attrezzature messe a disposizione dei lavoratori (artt. 70 e 71 del D.Lgs. 81/08).</span></p>"
)
ALLEGATO_V_PARAGRAFO = (
    "l’<b>Allegato V del D.Lgs. 81/08</b>.</span></p>"
)
ALLEGATO_V_AGGIUNTA = (
    '<p class="p1"><span class="s1">In pratica l’Allegato V riguarda le macchine antecedenti all’obbligo di '
    "Marcatura CE, in Italia dal <b>21 settembre 1996</b>. Una macchina successiva a quella data e priva di "
    "marcatura non si regolarizza con il solo Allegato V: serve una valutazione tecnica specifica del percorso "
    "di messa in conformità.</span></p>"
)
ICONBOX_MODIFICATE_FINE = "della normativa applicabile."
ICONBOX_MODIFICATE_AGGIUNTA = (
    f'\nSe l’intervento è un ammodernamento della macchina, vedi il servizio di '
    f'<a href="{LANDING_REVAMPING}">revamping dei macchinari industriali</a>.'
)

TABELLA = base.TABELLA_STILE + """<div class="pse-tabella"><table>
<caption>Quali norme si applicano alla tua macchina</caption>
<thead><tr><th scope="col">Situazione</th><th scope="col">Riferimento normativo</th><th scope="col">Cosa serve</th></tr></thead>
<tbody>
<tr><th scope="row">Macchina marcata CE (immessa sul mercato dal 21/09/1996)</th><td>Direttiva Macchine (oggi 2006/42/CE, recepita con D.Lgs. 17/2010); dal 20/01/2027 Regolamento (UE) 2023/1230; artt. 70 c.1 e 71 D.Lgs. 81/08</td><td>Dichiarazione di conformità, istruzioni in italiano, verifica che la macchina sia rimasta conforme (manutenzione, ripari, dispositivi di sicurezza)</td></tr>
<tr><th scope="row">Macchina senza marcatura CE, antecedente all'obbligo</th><td>Art. 70 c.2 e Allegato V D.Lgs. 81/08</td><td>Verifica dei requisiti dell'Allegato V, interventi di adeguamento, relazione tecnica di conformità</td></tr>
<tr><th scope="row">Macchina senza marcatura CE immessa sul mercato dopo il 21/09/1996</th><td>Direttiva / Regolamento Macchine</td><td>Non si regolarizza con il solo Allegato V: va valutato con un tecnico il percorso di messa in conformità e marcatura CE</td></tr>
<tr><th scope="row">Macchina costruita internamente per uso proprio</th><td>Direttiva / Regolamento Macchine</td><td>Chi la costruisce è fabbricante: valutazione dei rischi, fascicolo tecnico, dichiarazione e marcatura CE</td></tr>
<tr><th scope="row">Macchina modificata in modo sostanziale</th><td>Direttiva 2006/42/CE; dal 20/01/2027 Reg. (UE) 2023/1230, artt. 3 e 18</td><td>Nuova valutazione dei rischi, fascicolo tecnico, dichiarazione e marcatura CE</td></tr>
<tr><th scope="row">Insieme di macchine (linea)</th><td>Direttiva 2006/42/CE; Reg. (UE) 2023/1230</td><td>Valutazione dei rischi dell'insieme e marcatura CE dell'insieme</td></tr>
<tr><th scope="row">Macchina usata venduta, noleggiata o concessa in uso</th><td>Art. 72 D.Lgs. 81/08</td><td>Per le macchine non conformi alle direttive di prodotto: attestazione di conformità all'Allegato V al momento della consegna</td></tr>
</tbody></table></div>"""

NORME_INTRO = (
    "<p>La normativa applicabile dipende dall’anno di costruzione, dalla presenza della Marcatura CE e "
    "dall’uso che se ne fa. Ecco i casi più frequenti.</p>"
)
NORME_CHIUSURA = (
    "<p>Dal <b>20 gennaio 2027</b> il Regolamento (UE) 2023/1230 sostituisce la Direttiva Macchine "
    "2006/42/CE e definisce espressamente la modifica sostanziale. Se l’intervento è un ammodernamento, vedi "
    f'il servizio di <a href="{LANDING_REVAMPING}">revamping dei macchinari industriali</a>.</p>'
    f'<p>Fonti: <a href="{EURLEX_2023_1230}" target="_blank" rel="noopener">Regolamento (UE) 2023/1230</a> · '
    f'<a href="{NORMATTIVA_81}" target="_blank" rel="noopener">D.Lgs. 81/2008</a></p>'
)
AUTORE_HTML = (
    f'<p>Contenuto a cura di: <a href="{AUTORE_LINK}" target="_blank" rel="noopener">{AUTORE}</a>. '
    f"Ultimo aggiornamento: {DATA_AGGIORNAMENTO}.</p>"
)


def optimize(elements):
    ids = base.Ids(base.index(elements))
    by = base.index(elements)

    # 1. titoli
    for wid, (starts, tag, new_text) in HEADINGS.items():
        e = by.get(wid)
        base.expect(e and e.get("widgetType") == "heading", f"heading {wid} non trovato")
        s = base.settings(e)
        base.expect(base.strip(s.get("title")).startswith(starts),
                    f"heading {wid}: atteso '{starts}…', trovato '{base.strip(s.get('title'))[:40]}'")
        s["header_size"] = tag
        if new_text:
            s["title"] = new_text

    # 2. definizione in apertura
    s = base.settings(by["34683cc"])
    base.expect(s["editor"].startswith('<p class="p1"><span class="s1">Prosystem Engineering affianca'), "testo introduttivo 34683cc")
    s["editor"] = DEFINIZIONE + s["editor"]

    # 3. precisazione sull'Allegato V
    s = base.settings(by["cff9f54"])
    base.expect(s["editor"].count(ALLEGATO_V_PARAGRAFO) == 1, "paragrafo sull'Allegato V (cff9f54)")
    s["editor"] = s["editor"].replace(ALLEGATO_V_PARAGRAFO, ALLEGATO_V_PARAGRAFO + ALLEGATO_V_AGGIUNTA)

    # 4. link alla landing revamping nel riquadro "Macchine modificate o integrate"
    s = base.settings(by["aa9e0f5"])
    base.expect(s["description_text"].endswith(ICONBOX_MODIFICATE_FINE), "riquadro 'Macchine modificate' (aa9e0f5)")
    s["description_text"] += ICONBOX_MODIFICATE_AGGIUNTA

    # 5. FAQ: titoli H3, senza numerazione, con le nuove domande
    acc = base.settings(by["ab30225"])
    old_tabs = acc.get("tabs", [])
    base.expect(len(old_tabs) == 7, f"attese 7 FAQ, trovate {len(old_tabs)}")
    faq = base.read_faq()
    tabs = []
    for n, (q, a) in enumerate(faq):
        tab = copy.deepcopy(old_tabs[n]) if n < len(old_tabs) else {"_id": ids.new()}
        tab["tab_title"] = q
        tab["tab_content"] = f"<p>{a}</p>"
        tabs.append(tab)
    acc["tabs"] = tabs
    acc["title_html_tag"] = "h3"

    # 6. contatti: eliminata la copia mobile, la sezione desktop diventa visibile ovunque
    desk = base.settings(by[DESKTOP_SECTION])
    base.expect(desk.get("hide_mobile") == "hidden-mobile" and desk.get("_element_id") == base.ANCHOR_OLD,
                "sezione contatti desktop 81f6811")
    base.expect(base.settings(by[MOBILE_SECTION]).get("hide_desktop") == "hidden-desktop", "sezione contatti mobile f6beb16")
    del desk["hide_mobile"]
    base.expect(any(e["id"] == MOBILE_SECTION for e in elements), "copia mobile non a livello superiore")
    elements[:] = [e for e in elements if e["id"] != MOBILE_SECTION]

    # 7. nuova sezione con la tabella delle norme (dopo "Macchine con e senza Marcatura CE")
    def widget(kind, **st):
        return {"id": ids.new(), "elType": "widget", "settings": st, "elements": [], "widgetType": kind}

    heading = copy.deepcopy(by["fe83b55"])
    heading["id"] = ids.new()
    base.settings(heading).update({"title": "QUALI NORME SI APPLICANO ALLA TUA MACCHINA", "header_size": "h2"})
    sezione = {
        "id": ids.new(), "elType": "section", "isInner": False,
        "settings": {"_element_id": "norme-applicabili"},
        "elements": [{"id": ids.new(), "elType": "column", "isInner": False,
                      "settings": {"_column_size": 100, "_inline_size": None},
                      "elements": [heading, widget("text-editor", editor=NORME_INTRO),
                                   widget("html", html=TABELLA), widget("text-editor", editor=NORME_CHIUSURA)]}],
    }
    spaziatore = copy.deepcopy(by["9878f22"])

    def renew(e):
        e["id"] = ids.new()
        for c in e.get("elements", []):
            renew(c)

    renew(spaziatore)
    pos = next(i for i, e in enumerate(elements) if e["id"] == "9878f22")
    elements[pos + 1:pos + 1] = [sezione, spaziatore]

    # 8. autore, data e schema Service + FAQPage in fondo alla sezione FAQ
    schema_html = genera_schema.script_tag(genera_schema.page_graph(SCHEMA_SRC))
    faq_column = next(c for e in elements if e["id"] == "4cb977f" for c in e["elements"])
    faq_column["elements"] += [widget("text-editor", editor=AUTORE_HTML), widget("html", html=schema_html)]
    return elements


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("xml", help="export XML di WordPress")
    ap.add_argument("--outline", action="store_true", help="stampa solo i titoli prima/dopo, senza scrivere il file")
    args = ap.parse_args()

    original = base.load_page(args.xml)
    before = copy.deepcopy(original)
    after = optimize(copy.deepcopy(original))
    base.print_outline("PRIMA", before)
    base.print_outline("DOPO", after)
    if args.outline:
        return

    ids = list(base.index(after))
    assert len(ids) == len(set(ids)), "ID Elementor duplicati"
    template = {
        "version": "0.4",
        "title": "Adeguamento macchine D.Lgs. 81/08 (ottimizzata)",
        "type": "page",
        "content": after,
        "page_settings": [],
    }
    OUT.write_text(json.dumps(template, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"\nscritto {OUT.relative_to(ROOT)} ({OUT.stat().st_size // 1024} KB, {len(ids)} elementi)")


if __name__ == "__main__":
    main()
