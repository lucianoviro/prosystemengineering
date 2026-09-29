# Strategia SEO + GEO — Prosystem Engineering

Ambito: le due landing
- `/revamping-macchinari-industriali/`
- `/adeguamento-macchine-marcatura-ce-e-d-lgs-81-08/`

più gli interventi di sito indispensabili perché rendano.

> **SEO** = posizionarsi nei risultati di Google e Bing.
> **GEO** (Generative Engine Optimization) = essere letti, capiti e **citati** da ChatGPT, Perplexity, Gemini, Copilot e dalle AI Overviews di Google.
> Le due cose si sommano: la GEO parte da una buona SEO tecnica, poi richiede contenuti "estraibili" (risposte brevi e precise, dati, fonti) e un'entità aziendale chiara.

---

## 1. Premessa: cosa è stato analizzato

Il sito **non è raggiungibile** dall'ambiente di lavoro (dominio bloccato dalla policy di rete). L'analisi delle due landing si basa sull'export XML di WordPress del 29/09/2026 (contenuto, struttura Elementor e meta Yoast), integrato da:

- informazioni pubbliche su Prosystem Engineering (servizi, sede, contatti, pagine indicizzate);
- analisi dei risultati di ricerca per le keyword target e dei concorrenti;
- normativa vigente al 24/09/2026 (D.Lgs. 81/08, Direttiva 2006/42/CE, Regolamento (UE) 2023/1230 applicabile dal 20/01/2027).

La landing revamping è stata riscritta sui contenuti reali (`02-…`). La landing adeguamento è ancora una bozza generica (`03-…`) da rifare sull'export. La checklist al §7 elenca le verifiche da fare sul sito live.

---

## 2. Cosa emerge dalle fonti pubbliche

| # | Rilievo | Impatto | Azione |
|---|---|---|---|
| 1 | **Pagine in sovrapposizione**: `/marcatura-ce/`, `/marcatura-ce-2/`, `/adeguamenti-per-la-sicurezza/` trattano temi vicini alle due landing | Alto: cannibalizzazione, Google non sa quale pagina mostrare | Assegnare un ruolo a ogni URL (§3) e fare i redirect 301 |
| 2 | **Duplicato** `/marcatura-ce/` e `/marcatura-ce-2/` | Alto | Tenere la versione con più traffico e link, 301 dell'altra |
| 3 | Nei risultati compaiono sia `www.prosystemengineering.com` sia `prosystemengineering.com`, e link `http://` | Medio | Un solo host canonico (senza www, come ora nelle landing) con redirect 301 da www e da http |
| 4 | Il vecchio dominio `prosystemengineering.it` risulta ancora indicizzato (es. `contatti.php`) | Medio | 301 pagina per pagina verso il `.com` |
| 5 | **Ambiguità del nome**: esistono ProSystem (macchine packaging), Prosystem S.r.l., Prosystem Ingegneri. Anche la grafia varia ("Pro System" / "Prosystem") | Alto per la GEO: l'AI può confondere le aziende | Nome sempre identico ("Prosystem Engineering"), schema Organization con P. IVA, indirizzo e `sameAs` (§4) |
| 6 | **NAP non coerente** nelle directory: in alcune compare `info@prosystemingegneria.it` | Medio (SEO locale) | Allineare nome, indirizzo, telefono ed email su Google Business Profile, PagineBianche, LinkedIn, ICE e directory |
| 7 | Versione inglese: la pagina è intitolata "**CE Making**" (refuso di *CE Marking*) e la home EN ha slug `/home-eng-nuova/` | Medio sul mercato estero | Correggere il titolo; valutare le versioni EN delle due landing con `hreflang` |
| 8 | Refuso nello slug `/consulenza-quaita-ambiente/` | Basso | Correggere in `/consulenza-qualita-ambiente/` con 301 |
| 9 | Le due landing sono **molto recenti** (la landing revamping è stata creata il 15/09/2026): normale che non comparissero nelle ricerche di prova | Informativo | Controllo URL in Search Console: indicizzata? canonical corretto? |
| 10 | **Entrambe le landing hanno titolo SEO, meta description e parola chiave della home** ("Prosystem Engineering \| Consulenza e progettazione", kw "consulenza"): sono duplicati l'una dell'altra e di un'altra pagina (ID 4734) | **Alto**: titoli e descrizioni duplicati, nessuna ottimizzazione per le keyword target | Nuovi valori per la revamping in `02-…` §2; per l'adeguamento in `03-…` |

---

## 3. Architettura: un ruolo per ogni pagina

| URL | Keyword principale | Chi cerca | Ruolo |
|---|---|---|---|
| `/revamping-macchinari-industriali/` | revamping macchinari industriali | Azienda che vuole **ammodernare** una macchina | Landing servizio |
| `/adeguamento-macchine-marcatura-ce-e-d-lgs-81-08/` | adeguamento macchine D.Lgs 81/08 | Datore di lavoro / RSPP che deve **mettere a norma** macchine in uso | Landing servizio |
| `/marcatura-ce/` | marcatura CE macchine | **Costruttore** di macchine nuove o speciali, costruzione in proprio | Pagina servizio (lato fabbricante) |
| `/marcatura-ce-2/` | — | — | **301 → `/marcatura-ce/`** (o viceversa, vedi dati GSC) |
| `/adeguamenti-per-la-sicurezza/` | — | — | **301 → landing adeguamento** se il tema coincide; altrimenti riscrivere su un tema distinto |
| `/verifica-impianti-di-sollevamento/`, `/formazione/`, articolo perizie 4.0 | rispettive | — | Pagine collegate: link reciproci con le landing |

Prima dei redirect: in Search Console → *Prestazioni* filtrare per pagina e confrontare clic, impressioni e query di ogni URL; in *Link* verificare i link esterni. Si tiene l'URL più forte.

---

## 4. Strategia GEO

### 4.1 Nelle pagine (già applicata nei testi proposti)

- **Risposta subito**: ogni H2 è una domanda reale e il primo paragrafo risponde in 40-60 parole, autosufficienti (un'AI può citarle senza contesto).
- **Box "In sintesi"** in apertura: 5 punti fattuali, facili da estrarre.
- **Tabelle** di confronto (revamping/retrofit, CE/non CE, norme): formato che i motori generativi riprendono volentieri.
- **Riferimenti precisi**: articoli di legge, numeri di norma, date (21/09/1996, 20/01/2027). Le AI citano chi è preciso.
- **FAQ** con domande in linguaggio naturale, uguali a quelle poste agli assistenti.
- **E-E-A-T**: autore con qualifica e iscrizione all'Ordine, data di aggiornamento visibile, fonti ufficiali linkate (EUR-Lex, Normattiva).
- **Esperienza diretta**: caso studio con numeri reali. È l'elemento che manca oggi e che più distingue dai concorrenti. Va completato.
- **Attualità**: il tema *Regolamento Macchine 2023/1230 e modifica sostanziale* diventerà centrale con l'applicazione dal 20/01/2027. Le due landing lo presidiano già adesso.

### 4.2 Dati strutturati (schema.org)

- `schema/organization.html`: **ProfessionalService** con P. IVA, indirizzo, contatti, `knowsAbout`, `sameAs`. Da inserire **una sola volta**, su tutto il sito.
- `schema/<landing>.html`: **Service** + **FAQPage** per ciascuna landing, collegati all'organizzazione tramite `@id`.
- Le rich result FAQ oggi Google le mostra quasi solo ai siti istituzionali e sanitari, ma lo schema FAQ resta utile per far capire la pagina a Google e ai motori AI.

### 4.3 Accesso dei crawler AI

1. **robots.txt**: verificare che non blocchi i bot AI. Vedi `file-root/robots-ai.txt`.
2. **Firewall / CDN**: se il sito usa Cloudflare, controllare *AI Crawl Control / Block AI bots*: da luglio 2025 Cloudflare blocca i crawler AI di default sui nuovi domini. Stessa verifica per Wordfence, Sucuri e simili.
3. **Bing Webmaster Tools**: registrare il sito e inviare la sitemap. ChatGPT Search e Copilot si appoggiano all'indice di Bing. Attivare **IndexNow** (integrato in Rank Math; per Yoast c'è il plugin IndexNow di Microsoft).
4. **llms.txt** (`file-root/llms.txt`): standard proposto, oggi poco usato dai grandi motori. Costa 5 minuti ed è innocuo: consigliato, ma non prioritario.

### 4.4 Autorità dell'entità (fuori dal sito)

Le AI citano più volentieri aziende menzionate in modo coerente da più fonti:

- **Google Business Profile**: categoria principale adatta (es. "Studio di ingegneria"), servizi "Revamping macchinari" e "Adeguamento macchine D.Lgs. 81/08" con link alle landing, post periodici, **recensioni** di clienti che citano il servizio.
- **LinkedIn aziendale** e profili degli ingegneri: articoli brevi sul Regolamento 2023/1230 con link alle landing.
- **Citazioni esterne**: associazioni di categoria del territorio, portali di settore sulla sicurezza, fiere, comunicati sui casi reali.
- Profili coerenti su ICE, PagineBianche e directory con gli stessi dati NAP.

---

## 5. Contenuti di supporto (cluster)

Articoli del blog che rispondono a domande specifiche e linkano la landing di riferimento:

| Titolo proposto | Domanda a cui risponde | Linka |
|---|---|---|
| Regolamento Macchine 2023/1230: cosa cambia dal 20 gennaio 2027 per chi usa e modifica macchine | Cosa cambia nel 2027? | Entrambe |
| Modifica sostanziale di una macchina: definizione, esempi e obblighi | Quando serve una nuova marcatura CE? | Revamping |
| Allegato V D.Lgs. 81/08: checklist per le macchine senza marcatura CE | Come si adegua una macchina non CE? | Adeguamento |
| Revamping o macchina nuova? Come calcolare la convenienza | Conviene ammodernare? | Revamping |
| Vendere o comprare una macchina usata: obblighi dell'art. 72 D.Lgs. 81/08 | Posso vendere una macchina non CE? | Adeguamento |
| Revamping 4.0 e iperammortamento: requisiti tecnici e perizia | Il revamping è agevolabile? | Revamping + articolo perizie |

Ritmo sostenibile: 1 articolo al mese, ciascuno con autore, data, fonti e FAQ.

---

## 6. Misurazione

- **Google Search Console**: impressioni, clic e posizione per le query del §2 delle landing; filtro per pagina.
- **Bing Webmaster Tools**: stessi dati per Bing, che è la base di ChatGPT Search e Copilot.
- **GA4, traffico da AI**: creare un gruppo di canali personalizzato "AI assistants" con condizione *Sorgente corrisponde all'espressione regolare*:
  ```
  chatgpt\.com|chat\.openai\.com|perplexity\.ai|gemini\.google\.com|copilot\.microsoft\.com|claude\.ai|deepseek\.com
  ```
- **Conversioni**: evento `generate_lead` sull'invio del form e clic su `tel:`.
- **Test manuale mensile** su ChatGPT, Perplexity, Gemini e Google (AI Overview), annotando se Prosystem viene citata e con quale URL:
  1. Il revamping di una macchina richiede una nuova marcatura CE?
  2. Differenza tra revamping e retrofit di un macchinario
  3. Chi fa revamping di macchinari industriali in Piemonte?
  4. Cosa fare con una macchina senza marcatura CE?
  5. Allegato V D.Lgs 81/08: come adeguare una macchina vecchia
  6. Posso vendere una macchina usata non marcata CE?
  7. Cosa cambia con il Regolamento Macchine 2023/1230 per le modifiche alle macchine?
  8. Consulenza adeguamento macchine D.Lgs 81/08 vicino a Torino / Pinerolo

---

## 7. Checklist di audit sulle pagine live (da fare subito)

Non è stato possibile eseguirla da qui. Richiede 20 minuti con il browser o con Screaming Frog (gratuito fino a 500 URL).

**Indicizzazione**
- [ ] Search Console → Controllo URL: pagina indicizzata? "Canonical selezionato da Google" = URL della pagina?
- [ ] Nessun `noindex` (Yoast/Rank Math → Avanzate) e pagina presente nella sitemap
- [ ] `http://` e `www.` reindirizzano con **un solo** 301 all'URL canonico

**Struttura**
- [ ] **Un solo H1** (Elementor spesso lascia il titolo del tema come H1 aggiuntivo, oppure non ce n'è nessuno)
- [ ] Gerarchia H2 → H3 senza salti; nessun heading usato solo per lo stile
- [ ] Il testo principale è HTML, non dentro immagini, slider o popup

**Codice e dati**
- [ ] Title e meta description presenti e unici (tasto destro → Visualizza sorgente)
- [ ] Schema esistente: [Rich Results Test](https://search.google.com/test/rich-results) e [Schema Validator](https://validator.schema.org/). Evitare doppi Organization o FAQPage
- [ ] Open Graph (anteprima LinkedIn) corretto

**Prestazioni** ([PageSpeed Insights](https://pagespeed.web.dev/), mobile)
- [ ] LCP < 2,5 s · INP < 200 ms · CLS < 0,1
- [ ] Immagine hero non in lazy load; immagini WebP con dimensioni esplicite
- [ ] Animazioni d'ingresso di Elementor assenti o ridotte sopra la piega

**Collegamenti**
- [ ] Almeno 3 link interni in entrata per landing (home, menu, pagine correlate)
- [ ] Nessun link rotto; nessun link interno verso URL che reindirizzano

---

## 8. Priorità

| Quando | Cosa |
|---|---|
| **Settimana 1** | Audit §7 · verifica robots/Cloudflare · decisione sui redirect (§3) · nuovi title/meta · un solo H1 |
| **Settimane 2-3** | Pubblicazione dei nuovi testi · schema Organization + Service + FAQ · link interni · box autore e data · Bing Webmaster Tools + IndexNow |
| **Mese 2** | Caso studio reale per landing · Google Business Profile · prime recensioni · primo articolo del cluster (Regolamento 2023/1230) |
| **Mese 3 e oltre** | 1 articolo al mese · test prompt AI mensile · aggiornamento contenuti prima del 20/01/2027 · valutazione versioni EN |
