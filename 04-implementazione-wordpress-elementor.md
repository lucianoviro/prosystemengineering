# Guida all'implementazione in WordPress + Elementor

Procedura passo passo per applicare il kit alle due landing. I nomi dei menu possono variare leggermente con la versione di Elementor e del plugin SEO.

---

## 0. Prima di iniziare

1. **Backup** completo (database + file) o lavoro su un **ambiente di staging**.
2. In Search Console esportare le query e le posizioni attuali delle due landing (*Prestazioni → Pagina*): serviranno per il confronto prima/dopo.
3. Il plugin SEO del sito è **ThinkRank** (verificato sul sorgente della landing revamping); le indicazioni su Yoast/Rank Math qui sotto vanno adattate ai suoi campi, che non ho visto.

---

## 1. Title, meta description e Open Graph

In Elementor, aprire la pagina → pannello del plugin SEO (Yoast o Rank Math compaiono nell'editor):

- **Titolo SEO** e **meta description**: copiare dal §1 dei file `02-…` e `03-…`.
- **Keyword principale** (focus keyword): solo come promemoria, non incide sul posizionamento.
- Scheda **Social**: OG title, OG description, immagine 1200×630.
- **Rank Math**: nella scheda *Schema* della pagina impostare **Nessuno** (o *WebPage*), non *Article*: lo schema Service viene dal kit.

---

## 2. Un solo H1 e gerarchia dei titoli

1. **Impostazioni pagina** (icona ingranaggio) → **Nascondi titolo** = Sì, così il titolo del tema non crea un secondo H1.
2. Widget **Titolo** (Heading) dell'hero → *Tag HTML* = **H1**. Tutti gli altri widget Titolo: H2 o H3 come indicato nei file delle landing.
3. Negli **Icon Box** / **Image Box** impostare *Tag HTML del titolo* = H3 (per default spesso sono H3; verificare che non siano H2 o H1).
4. Non usare un heading solo per avere un testo grande: per quello si usa lo stile, non il tag.
5. Verifica: estensione del browser "Detailed SEO Extension" o "HeadingsMap", oppure *Visualizza sorgente* e ricerca di `<h1`.

---

## 3. Testi e blocchi HTML

1. **CSS una volta sola**: copiare `elementor/pse-stili.css` in *Elementor → Impostazioni sito → CSS personalizzato* (Elementor Pro) oppure in *Aspetto → Personalizza → CSS aggiuntivo*. Adattare i colori (`--pse-accento`) alla palette del sito.
2. Testi normali: widget **Editor di testo**, incollando dal file della landing (i `**grassetti**` vanno applicati a mano o incollando dalla versione HTML).
3. Box "In sintesi", tabelle, fasi del processo, callout e box autore: widget **HTML**, incollando il blocco corrispondente da `elementor/adeguamento-blocchi.html` (per la landing revamping vedi invece l'import del template, `02-…` §7).
4. Sezione del form: *Avanzate → ID CSS* = `contatti` (i bottoni dell'hero puntano a `#contatti`).
5. Cercare `[[` nella pagina prima di pubblicare: nessun segnaposto deve restare.

---

## 4. FAQ

1. Widget **Accordion** (o *Nested Accordion*): una voce per domanda, titolo = domanda, contenuto = risposta, **testo identico** a quello del file della landing.
2. *Tag HTML del titolo* = **H3**.
3. Se il widget ha l'opzione **FAQ Schema**, lasciarla **disattivata**: lo schema FAQ è già nello snippet del kit, e due FAQPage sulla stessa pagina sono un errore.
4. Il contenuto degli accordion chiusi è comunque nell'HTML: Google e le AI lo leggono.

> Se si modifica una FAQ: aggiornare il file `.md`, lanciare `python3 tools/genera_schema.py` e sostituire lo snippet nella pagina. Il testo dello schema deve sempre coincidere con quello visibile.

---

## 5. Dati strutturati (JSON-LD)

Tre snippet già pronti, ciascuno con il suo tag `<script>`:

| File | Dove | Frequenza |
|---|---|---|
| `schema/organization.html` | Tutto il sito | Una volta |
| `schema/revamping-macchinari-industriali.html` | Solo landing revamping | — |
| `schema/adeguamento-macchine-marcatura-ce-dlgs-81-08.html` | Solo landing adeguamento | — |

**Prima di incollare** `organization.html`: sostituire gli URL `SOSTITUIRE-…` di logo e immagine e verificare P. IVA, indirizzo e profili `sameAs`.

**Opzione A — Elementor Pro (consigliata)**
*Elementor → Codice personalizzato → Aggiungi nuovo* → incollare lo snippet → Posizione **`<head>`** → Pubblica → Condizioni:
- Organization: *Intero sito*.
- Landing: *Includi → Singolare → Pagine → [nome pagina]*.

**Opzione B — plugin WPCode (gratuito)**
*Code Snippets → Add Snippet → HTML* → posizione *Site Wide Header* per l'Organization. Per le landing usare le regole condizionali per pagina, se disponibili nella versione in uso, altrimenti l'opzione C.

**Opzione C — widget HTML**
Per gli snippet delle landing: un widget HTML in fondo alla pagina con lo snippet incollato. Lo schema nel `<body>` è valido.

**Organization e plugin SEO**
ThinkRank (come Yoast e Rank Math) genera già un nodo Organization con lo stesso `@id` (`https://prosystemengineering.com/#organization`): i due blocchi vengono uniti da Google, quindi basta che i dati coincidano. Compilare comunque *Yoast → Impostazioni → Rappresentazione del sito* o *Rank Math → Titoli e Meta → SEO locale* con gli stessi nome, logo e dati.

**Validazione** (dopo la pubblicazione):
- [Rich Results Test](https://search.google.com/test/rich-results): nessun errore.
- [Schema Markup Validator](https://validator.schema.org/): vedere Service, FAQPage, ProfessionalService.
- Controllare che non ci siano **due** FAQPage o due Service sulla stessa pagina.

---

## 6. Link interni

1. Inserire i link in uscita indicati al §4 di ciascun file landing, con gli anchor text proposti.
2. Aggiungere i link in entrata: homepage (blocco servizi), menu *Servizi*, `/marcatura-ce/`, `/verifica-impianti-di-sollevamento/`, `/formazione/`.
3. Link alle fonti esterne (EUR-Lex, Normattiva): nuova scheda, **senza** `nofollow`.

---

## 7. Redirect

Dopo la verifica in Search Console (vedi `01-strategia-seo-geo.md` §3):

- `/marcatura-ce-2/` → `/marcatura-ce/` (o l'inverso) — 301
- `/adeguamenti-per-la-sicurezza/` → `/adeguamento-macchine-marcatura-ce-e-d-lgs-81-08/` — 301
- `/consulenza-quaita-ambiente/` → `/consulenza-qualita-ambiente/` — 301 (dopo aver corretto lo slug)

Strumenti: *Rank Math → Reindirizzamenti*, Yoast Premium *Redirect*, oppure il plugin gratuito **Redirection**. Poi aggiornare i link interni che puntavano ai vecchi URL.

---

## 8. Immagini

- Formato **WebP**, larghezza massima 1600 px, peso indicativo < 150 KB.
- Nome file descrittivo **prima** del caricamento (es. `revamping-macchinario-industriale.webp`).
- Testo alternativo nella Libreria media (Elementor lo riprende): descrivere la foto reale, come indicato al §5 dei file landing.
- Immagine dell'hero: **nessun lazy load** (in Elementor: impostazione del widget Immagine o del plugin di cache).

---

## 9. Prestazioni (Core Web Vitals)

1. *Elementor → Impostazioni → Funzionalità / Prestazioni*: attivare le opzioni di ottimizzazione, se non già attive: output DOM ottimizzato, caricamento migliorato degli asset e del CSS, icone inline, lazy load delle immagini di sfondo, cache degli elementi.
2. **Google Fonts in locale** (opzione di Elementor *Carica Google Fonts localmente*) e al massimo 2 famiglie di font.
3. Togliere le **animazioni d'ingresso** dagli elementi sopra la piega: ritardano la visualizzazione del contenuto (LCP).
4. Plugin di cache (WP Rocket, LiteSpeed Cache, FlyingPress…) con minificazione e ritardo del JavaScript non essenziale.
5. Misurare con [PageSpeed Insights](https://pagespeed.web.dev/) su mobile prima e dopo. Obiettivo: LCP < 2,5 s, INP < 200 ms, CLS < 0,1.

---

## 10. File nella root del sito

- **robots.txt**: vedi `file-root/robots-ai.txt`. In Yoast: *Strumenti → Editor di file*; in Rank Math: *Impostazioni generali → Modifica robots.txt*.
- **llms.txt**: caricare `file-root/llms.txt` nella root (`https://prosystemengineering.com/llms.txt`) via FTP o File Manager dell'hosting, dopo aver verificato gli URL.
- Se c'è **Cloudflare**: *Sicurezza → Bot / AI Crawl Control*, verificare che i bot di ricerca AI (OAI-SearchBot, PerplexityBot, Claude-SearchBot…) non siano bloccati.

---

## 11. Data di aggiornamento e autore

- Box autore (blocco HTML) con nome, qualifica e data. In alternativa, con Elementor Pro, un Editor di testo con il tag dinamico *Data del post* impostato sulla data di **modifica**.
- Cambiare la data **solo** quando il contenuto viene davvero aggiornato.
- Ideale: una pagina autore (o una sezione "Chi siamo" con i profili degli ingegneri) a cui il nome nel box rimanda.

---

## 12. Dopo la pubblicazione

1. Search Console → **Controllo URL** → *Richiedi indicizzazione* per entrambe le landing.
2. **Bing Webmaster Tools** → *Invio URL* (o IndexNow automatico).
3. Aggiornare la **sitemap** (Yoast/Rank Math lo fanno da soli) e verificare che contenga le due landing.
4. Google Business Profile: aggiungere i due servizi con link alla landing.
5. Dopo 4-6 settimane: confronto con i dati del punto 0 e primo test dei prompt AI (`01-strategia-seo-geo.md` §6).
