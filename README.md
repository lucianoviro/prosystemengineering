# Prosystem Engineering: kit SEO + GEO per due landing

Ottimizzazione per Google (SEO) e per i motori generativi (GEO: ChatGPT, Perplexity, Gemini, AI Overviews) delle landing:

- https://prosystemengineering.com/revamping-macchinari-industriali/
- https://prosystemengineering.com/adeguamento-macchine-marcatura-ce-e-d-lgs-81-08/

Sito: WordPress + Elementor.

## Contenuto

| File | A cosa serve |
|---|---|
| [`01-strategia-seo-geo.md`](01-strategia-seo-geo.md) | Problemi rilevati, ruolo di ogni pagina, redirect, strategia GEO, misurazione, checklist di audit, priorità |
| [`02-landing-revamping-macchinari-industriali.md`](02-landing-revamping-macchinari-industriali.md) | **Landing revamping, analizzata sulla pagina reale**: rilievi, valori Yoast, gerarchia dei titoli prima/dopo, testi nuovi, FAQ, cosa fare a mano, come importare |
| [`03-landing-adeguamento-macchine-dlgs-81-08.md`](03-landing-adeguamento-macchine-dlgs-81-08.md) | Landing adeguamento: **bozza generica** da rifare sull'export reale (prossimo passo) |
| [`04-implementazione-wordpress-elementor.md`](04-implementazione-wordpress-elementor.md) | Guida passo passo per Elementor, Yoast/Rank Math, schema, redirect, prestazioni |
| `elementor/revamping-ottimizzata.json` | **Template Elementor importabile** della landing revamping (pagina reale + modifiche) |
| `elementor/adeguamento-blocchi.html`, `pse-stili.css` | Blocchi HTML della bozza adeguamento |
| `schema/*.html` | JSON-LD pronti da incollare: Organization (tutto il sito), Service + FAQPage (per landing) |
| `schema/src/` | Sorgenti dello schema |
| `tools/ottimizza_revamping.py` | Genera il template Elementor dall'export XML di WordPress (`python3 tools/ottimizza_revamping.py export.xml`) |
| `tools/genera_schema.py` | Rigenera gli snippet schema dalle FAQ dei file `.md` |
| `file-root/` | `llms.txt` e proposta di `robots.txt` per i crawler AI |

## Da dove iniziare

**Landing revamping** (pronta): seguire `02-landing-revamping-macchinari-industriali.md` §2 (Yoast), §7 (import del template) e §5 (attività a mano).

**Landing adeguamento**: da rifare partendo dall'export, con lo stesso metodo.

Strategia generale e redirect: `01-strategia-seo-geo.md`. Guida generica Elementor/schema: `04-…`.

## Da completare prima della pubblicazione

I segnaposto `[[...]]` indicano dati che solo l'azienda conosce. Non vanno inventati:

- **nome e qualifica dell'autore** (ingegnere, n. di iscrizione all'Ordine);
- **area servita** reale;
- **caso studio** con numeri reali (uno per landing): è l'elemento che più aumenta le citazioni nelle risposte AI;
- tempi e costi indicativi, se l'azienda vuole comunicarli;
- servizi effettivamente eseguiti in proprio o con partner (sezione "Cosa comprende");
- **agevolazioni fiscali** (iperammortamento 2026-2028): requisiti e soglie da far verificare al consulente fiscale;
- logo e immagine in `schema/src/organization.json`; verificare P. IVA (`IT10307730019`), indirizzo e profili `sameAs`, presi da fonti pubbliche.

## Rigenerare lo schema

Dopo aver modificato le FAQ in un file `.md` o i dati in `schema/src/`:

```bash
python3 tools/genera_schema.py
```

Lo script scrive gli snippet in `schema/` e segnala i segnaposto ancora presenti.

## Limiti di questa analisi

Il sito non è raggiungibile dall'ambiente di lavoro (dominio bloccato dalla policy di rete): l'analisi si basa sull'export XML di WordPress del 29/09/2026, che contiene contenuto, struttura Elementor e meta Yoast **solo delle due landing**. Non sono verificabili da qui: testo dello slider, `<head>` reale (schema, plugin SEO), indicizzazione, prestazioni. La landing revamping è analizzata sui dati reali; la landing adeguamento (file `03-…`, `elementor/adeguamento-blocchi.html`) è ancora una bozza generica da rifare sull'export. Con l'accesso al dominio (o il sorgente HTML delle due pagine) si può fare l'analisi delle differenze rispetto ai testi attuali.

Normativa verificata alla data del 24/09/2026.
