# Prosystem Engineering: kit SEO + GEO per due landing

Ottimizzazione per Google (SEO) e per i motori generativi (GEO: ChatGPT, Perplexity, Gemini, AI Overviews) delle landing:

- https://prosystemengineering.com/revamping-macchinari-industriali/
- https://prosystemengineering.com/adeguamento-macchine-marcatura-ce-e-d-lgs-81-08/

Sito: WordPress + Elementor.

## Contenuto

| File | A cosa serve |
|---|---|
| [`01-strategia-seo-geo.md`](01-strategia-seo-geo.md) | Problemi rilevati, ruolo di ogni pagina, redirect, strategia GEO, misurazione, checklist di audit, priorità |
| [`02-landing-revamping-macchinari-industriali.md`](02-landing-revamping-macchinari-industriali.md) | Landing revamping: keyword, title/meta, struttura, **testi completi**, FAQ, link, immagini |
| [`03-landing-adeguamento-macchine-dlgs-81-08.md`](03-landing-adeguamento-macchine-dlgs-81-08.md) | Landing adeguamento: stessa struttura |
| [`04-implementazione-wordpress-elementor.md`](04-implementazione-wordpress-elementor.md) | Guida passo passo per Elementor, Yoast/Rank Math, schema, redirect, prestazioni |
| `elementor/` | Blocchi HTML pronti (box "In sintesi", tabelle, fasi, box autore) e CSS |
| `schema/*.html` | JSON-LD pronti da incollare: Organization (tutto il sito), Service + FAQPage (per landing) |
| `schema/src/` | Sorgenti dello schema |
| `tools/genera_schema.py` | Rigenera gli snippet schema dalle FAQ dei file `.md` |
| `file-root/` | `llms.txt` e proposta di `robots.txt` per i crawler AI |

## Da dove iniziare

1. Leggere `01-strategia-seo-geo.md` §2 e §8 (5 minuti).
2. Fare l'audit rapido delle pagine live (`01-…` §7).
3. Completare i segnaposto: `grep -rn "\[\[" *.md elementor/` e `grep -rn SOSTITUIRE schema/`.
4. Applicare le landing seguendo `04-implementazione-wordpress-elementor.md`.

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

Le pagine live non erano raggiungibili dall'ambiente di lavoro (dominio bloccato dalla policy di rete), quindi codice, testi attuali, schema esistente e prestazioni **non sono stati verificati**. Con l'accesso al dominio (o il sorgente HTML delle due pagine) si può fare l'analisi delle differenze rispetto ai testi attuali.

Normativa verificata alla data del 24/09/2026.
