# Landing 2 — Adeguamento macchine, Marcatura CE e D.Lgs. 81/08

URL: `https://prosystemengineering.com/adeguamento-macchine-marcatura-ce-e-d-lgs-81-08/` (ID pagina 7176)

> **Versione 2**, basata sull'export WordPress del 29/09/2026 (contenuto e struttura Elementor reali). Sostituisce la bozza generica.
> Stesso metodo della landing revamping (`02-…`): un template Elementor importabile, generato dall'export, che non tocca la pagina live.

| Cosa | Come | File |
|---|---|---|
| Meta description, titolo SEO, parola chiave, tipo di schema | A mano in ThinkRank (§2) | — |
| Titoli, nuovi blocchi, FAQ, link, contatti, schema, autore | Import del template Elementor (§6) | `elementor/adeguamento-ottimizzata.json` |
| Testi alternativi | A mano in Libreria media (§5) | — |

---

## 1. Cosa emerge dall'export

La pagina è un clone della landing revamping: i difetti strutturali sono gli stessi, il testo invece è buono e va mantenuto.

| # | Rilievo | Impatto | Correzione |
|---|---|---|---|
| 1 | **13 titoli H1** nel corpo (uno per sezione, più i due della sezione contatti duplicata); i sottotitoli sono H2 e i blocchi di testo interni H3/H4 | **Medio-alto**: nessuna gerarchia leggibile | Un solo H1 (quello dello slider, da verificare), sezioni H2 (§3) |
| 2 | **Nessuna descrizione SEO**: in ThinkRank non risulta impostato nessun campo per questa pagina; la meta description viene ricavata a caso dall'inizio del testo, come sulla revamping prima della correzione. Il titolo di pagina (`Adeguamento macchine, marcatura CE e D.Lgs. 81/08 – Prosystem Engineering`, 72 caratteri) viene troncato nei risultati | **Alto** | §2 |
| 3 | **CTA su mobile**: i 5 pulsanti puntano a `#richiedi-una-valutazione`, sezione nascosta su mobile (copia separata senza ID) | **Alto sulle conversioni** | Copia mobile eliminata, sezione unica (§4) |
| 4 | **Sezione contatti duplicata**: due volte titolo, indirizzo, mappa e lo stesso form (WPForms 6971, ID identici) | Medio | Come sopra |
| 5 | **Nessun link interno**: nemmeno verso la landing revamping | Medio | Link nel testo e nelle FAQ (§4) |
| 6 | **Alt**: tutte le immagini con `alt` vuoto; le icone dei passi hanno come alt il nome del file | Medio-basso | §5 |
| 7 | **FAQ**: 7 domande numerate, senza heading; la risposta sulla modifica non definisce la modifica sostanziale; mancano le domande più cercate (macchine usate, controlli periodici, sanzioni, Regolamento 2027) | Medio (GEO) | 12 domande (§7) |
| 8 | **Riferimenti normativi generici**: Allegato V citato, ma senza data, senza art. 70-72, senza il Regolamento 2023/1230 | Medio (GEO) | Tabella e paragrafi (§4) |
| 9 | Nessun schema Service/FAQPage, nessun autore né data | Medio | Nel template (§4) |
| 10 | **Non verificabile dall'export**: testo dello slider ("Landing Adeguamenti Marcatura CE") | Se non contiene un H1, la pagina resta senza H1 | §5 |

Punti di forza da mantenere: distinzione chiara tra Marcatura CE e D.Lgs. 81/08, elenco dei fattori di verifica, sezioni audit del parco macchine e adeguamento "chiavi in mano", tono prudente ("la conclusione non può essere automatica").

---

## 2. Valori SEO (Modifica pagina → riquadro ThinkRank)

| Campo | Valore |
|---|---|
| **Parola chiave principale** | `adeguamento macchine D.Lgs 81/08` |
| **Titolo SEO** (59 car.) | `Adeguamento Macchine D.Lgs. 81/08 e Marcatura CE \| Prosystem` |
| **Meta description** (142 car.) | `Messa a norma di macchine con e senza Marcatura CE: verifica Allegato V D.Lgs. 81/08, analisi dei rischi, interventi e documentazione tecnica.` |
| **Tipo di schema** | **WebPage** (non "Article"): Service e FAQPage sono già nel template |
| **Immagine social** | Foto reale 1200×630 |
| **Slug** | invariato |

---

## 3. Gerarchia dei titoli: prima e dopo

<!-- OUTLINE:START -->
| Titolo | Prima | Dopo |
|---|---|---|
| LA MARCATURA CE NON È L’UNICO ASPETTO DA VERIFICARE | H1 | **H2** |
| QUANDO È NECESSARIO VERIFICARE LA CONFORMITÀ DI UNA MACCHINA | H1 | **H2** |
| ADEGUAMENTO DELLE MACCHINE AL D.LGS. 81/08 | H1 | **H2** |
| Verifica dei requisiti di sicurezza delle attrezzature di lavoro | H2 | **H3** |
| VERIFICA DELLA MARCATURA CE E DELLA DOCUMENTAZIONE | H1 | **H2** |
| COME AFFRONTIAMO L’ADEGUAMENTO DI UNA MACCHINA | H1 | **H2** |
| ADEGUAMENTO “CHIAVI IN MANO” | H1 | **H2** |
| Dall’individuazione del rischio alla verifica dell’intervento | H2 | **testo** |
| MACCHINE CON E SENZA MARCATURA CE | H1 | **H2** |
| Ogni macchina richiede un inquadramento specifico | H2 | **testo** |
| AUDIT DI SICUREZZA DEL PARCO MACCHINE | H1 | **H2** |
| Conosci lo stato di conformità del tuo stabilimento | H2 | **testo** |
| ESPERIENZA NELLA SICUREZZA DELLE MACCHINE INDUSTRIALI | H1 | **H2** |
| PERCHÉ SCEGLIERE PROSYSTEM ENGINEERING | H1 | **H2** |
| FAQ → **DOMANDE FREQUENTI SULL’ADEGUAMENTO DELLE MACCHINE** | H1 | **H2** |
| DEVI VERIFICARE O ADEGUARE UNA MACCHINA? | H1 | **H2** |
| Contattaci, partiremo da un’analisi tecnica delle condizioni reali | H2 | **testo** |
| QUALI NORME SI APPLICANO ALLA TUA MACCHINA *(nuova sezione)* | — | **H2** |
| Domande delle FAQ (12, senza numerazione) | testo semplice | **H3** |

**Riepilogo**: nel corpo, prima 13 H1 e 8 H2. Dopo: **0 H1 nel corpo** (l'H1 è quello dello slider), 15 H2, sottotitoli e slogan come testo semplice, FAQ in H3. Le righe della sezione contatti presenti due volte erano la stessa sezione in versione desktop e mobile: ora è una sola.

Restano invariati i titoli dentro i blocchi di testo (passi del processo H4, blocchi "Perché scegliere" H3, ecc.), perché il loro aspetto dipende dal tema. In particolare restano due H2 interni: la citazione *"Prosystem Engineering individua le criticità…"* (una frase intera, in un riquadro di citazione) e *"Il servizio può comprendere"* (bianco su fondo blu). Modificarli cambierebbe l'aspetto; sono difetti minori.
<!-- OUTLINE:END -->

---

## 4. Cosa contiene il template Elementor

`elementor/adeguamento-ottimizzata.json` è la pagina attuale con queste modifiche:

1. **Titoli** come al §3. L'H1 resta quello dello slider.
2. **Definizione in apertura** (prima del testo esistente): che cos'è l'adeguamento di una macchina e a chi spetta (artt. 70 e 71 D.Lgs. 81/08).
3. **Precisazione sull'Allegato V**: vale per le macchine antecedenti all'obbligo di Marcatura CE (in Italia dal 21 settembre 1996); per quelle successive e prive di marcatura non basta.
4. **Nuova sezione "Quali norme si applicano alla tua macchina"**, dopo "Macchine con e senza Marcatura CE": tabella con sette casi (marcata CE, non marcata antecedente, non marcata successiva, costruita in proprio, modificata, insieme di macchine, usata venduta o noleggiata), il Regolamento 2023/1230 e le fonti (EUR-Lex, Normattiva).
5. **Link alla landing revamping**: nel riquadro "Macchine modificate o integrate", sotto la tabella e nelle FAQ. Link alla pagina sulla verifica degli impianti di sollevamento nella FAQ sui controlli.
6. **FAQ**: 12 domande, titoli H3, senza numerazione (§7). Le 7 originali sono mantenute (la 4 è riscritta, le 1 e 2 hanno un riferimento in più).
7. **Contatti**: eliminata la copia mobile; la sezione con ID `richiedi-una-valutazione` è ora visibile ovunque, quindi tutti i CTA e il pulsante dello slider funzionano su telefono. Un solo form, una sola mappa.
8. **Autore e data** sotto le FAQ (stesso formato della landing revamping) e **schema Service + FAQPage** come widget HTML.

Il file non contiene segnaposto. Non contiene gli alt (l'import li perde: §5).

---

## 5. Da fare a mano

| Priorità | Attività | Perché |
|---|---|---|
| 1 | **ThinkRank**: titolo, meta description, tipo di schema WebPage, immagine social (§2) | Non si importano con Elementor |
| 1 | **Slider "Landing Adeguamenti Marcatura CE"** (Slider Revolution): verificare che il titolo grande sia un layer H1, e che compaia nel sorgente pubblicato (`view-source:`, cerca `<h1`). Se manca, dimmelo: il titolo "La Marcatura CE non è l'unico aspetto da verificare" va rimesso come H1 nel corpo | L'export non contiene lo slider |
| 1 | **Alt in Libreria media** sulle immagini nuove (`…-1`): icone dei passi "Fase 1…8"; immagini principali con testo descrittivo (verificare sulle immagini reali: le tre sono `pexels-sergey-sergeev…`, `ADEGUAMENTO-CHIAVI-IN-MANO…`, `AUDIT-DI-SICUREZZA-DEL-PARCO-MACCHINE…`) | L'import perde gli alt |
| 1 | **Provare il form da telefono** | La copia mobile è stata eliminata |
| 2 | **Confronto con i testi ufficiali**: l'ingegnere verifica sui testi di legge le affermazioni su artt. 70, 71, 72, 87 D.Lgs. 81/08, sul 21 settembre 1996 e sulla definizione di modifica sostanziale (art. 3, punto 16, Reg. 2023/1230). Non ho potuto consultare EUR-Lex né Normattiva da qui | Contenuto normativo |
| 2 | **Verificare in ThinkRank** che lo schema pubblicato contenga un solo FAQPage e nessun "Article" (`view-source:`, cerca `application/ld+json`) | Doppioni |
| 2 | **Un caso reale** con numeri (anche anonimo): verifica di una macchina non CE, audit di un parco macchine, un adeguamento chiavi in mano | Manca ancora su entrambe le landing |
| 2 | **Link in entrata**: dalla landing revamping (aggiungere "adeguamento delle macchine" nel testo), dalla home, dal menu Servizi, dalla pagina Marcatura CE | Il link reciproco dalla revamping è già presente nel template di quella pagina, non nel testo |
| 3 | **Link a Marcatura CE**: da aggiungere quando si sceglie tra `/marcatura-ce/` e `/marcatura-ce-2/` | URL da chiarire |
| 3 | **Area servita nello schema**: ho scritto "Piemonte" e "Italia" (`schema/src/…`): confermare | Dato non verificabile da qui |
| 3 | **Peso delle immagini** (JPG da `-scaled`, PNG delle icone `@4x`): convertire in WebP | Prestazioni |

---

## 6. Come importare il template

Come per la revamping:

1. Elementor → **Template → Template salvati → Importa template** → `elementor/adeguamento-ottimizzata.json`.
2. **Pagine → Aggiungi nuova** (bozza), template **Elementor a larghezza intera con header e footer** → Modifica con Elementor → icona cartella → Template salvati → **Inserisci**.
3. Controllare anteprima su desktop, tablet e telefono: titoli, nuova tabella, sezione contatti unica.
4. Copiare il contenuto nella pagina 7176 (o incollare le sezioni), poi ThinkRank (§2), alt (§5) e slider (§5).
5. Aggiornare la pagina, svuotare la cache SiteGround, controllare il sorgente.

L'import ricrea le immagini nella libreria (suffisso `-1`) e perde gli alt. Non l'ho provato su un WordPress; se dà errore la pagina live non cambia.

---

## 7. FAQ (fonte unica)

Alimenta sia il template sia lo schema FAQPage. Dopo ogni modifica: `python3 tools/ottimizza_adeguamento.py <export.xml>` e `python3 tools/genera_schema.py`.

Le risposte 1-7 sono quelle di Prosystem, con ritocchi minimi (1, 2) o riscritte (4). Le 8-12 sono nuove. Le affermazioni normative vanno verificate dall'ingegnere (§5).

<!-- FAQ:START -->
#### Una macchina con Marcatura CE è automaticamente conforme al D.Lgs. 81/08?
La Marcatura CE attesta la conformità della macchina al momento della sua immissione sul mercato o messa in servizio secondo la normativa di prodotto applicabile. Il datore di lavoro deve comunque installarla, utilizzarla e mantenerla correttamente, verificando nel tempo che conservi condizioni di sicurezza adeguate (artt. 70 e 71 del D.Lgs. 81/08).

#### Le macchine vecchie devono essere marcate CE?
Non tutte le macchine datate devono essere marcate CE retroattivamente. Per le attrezzature costruite prima dell’applicazione delle direttive europee pertinenti (in Italia, prima del 21 settembre 1996) occorre verificare la conformità ai requisiti di sicurezza applicabili, tra cui quelli previsti dall’Allegato V del D.Lgs. 81/08.

#### Chi è responsabile della sicurezza delle macchine utilizzate in azienda?
Il fabbricante è responsabile degli obblighi connessi alla conformità del prodotto. Il datore di lavoro ha invece l’obbligo di mettere a disposizione attrezzature idonee e sicure, installarle e utilizzarle correttamente e mantenerle in condizioni adeguate nel tempo.

#### Una modifica richiede sempre una nuova Marcatura CE?
No. Serve una nuova Marcatura CE quando la modifica è sostanziale: non prevista né pianificata dal fabbricante, incide sulla sicurezza della macchina creando un nuovo pericolo o aumentando un rischio esistente. In questo caso chi esegue la modifica assume gli obblighi del fabbricante: valutazione dei rischi, Fascicolo Tecnico, dichiarazione di conformità e Marcatura CE. Negli altri casi è consigliabile documentare la valutazione svolta. Soltanto un’analisi tecnica permette di stabilire quale procedura applicare. Approfondisci: [revamping dei macchinari industriali](https://prosystemengineering.com/revamping-macchinari-industriali/).

#### Cosa comprende un audit di sicurezza delle macchine?
L’audit può comprendere il censimento delle attrezzature, l’analisi delle norme applicabili, la verifica tecnica e documentale, l’individuazione delle non conformità e la definizione delle priorità di intervento.

#### È possibile adeguare un’intera linea di produzione?
Sì. L’analisi può riguardare le singole macchine, le interconnessioni, i sistemi di comando, gli accessi e i rischi generati dal funzionamento complessivo della linea.

#### Prosystem può seguire anche la realizzazione degli interventi?
Sì. Oltre all’analisi e alla progettazione, Prosystem Engineering può supportare l’esecuzione degli adeguamenti, coordinare le lavorazioni specialistiche e verificare gli interventi al termine dei lavori.

#### Cosa fare con una macchina senza Marcatura CE?
Occorre distinguere. Se la macchina è antecedente all’obbligo di Marcatura CE (in Italia dal 21 settembre 1996) si verifica la conformità ai requisiti dell’Allegato V del D.Lgs. 81/08, si eseguono gli eventuali interventi di adeguamento e si documenta l’esito in una relazione tecnica. Se invece è successiva a quella data ed è priva di marcatura, non basta l’Allegato V: serve una valutazione tecnica specifica sul percorso di messa in conformità.

#### Posso vendere, noleggiare o concedere in uso una macchina usata non marcata CE?
Chi vende, noleggia o concede in uso una macchina non conforme alle direttive di prodotto, ad esempio perché antecedente all’obbligo di Marcatura CE, deve attestare sotto la propria responsabilità che al momento della consegna è conforme ai requisiti dell’Allegato V del D.Lgs. 81/08 (art. 72). Conviene basare l’attestazione su una verifica tecnica documentata.

#### Ogni quanto vanno controllate le macchine?
L’art. 71 del D.Lgs. 81/08 richiede un controllo iniziale per le attrezzature la cui sicurezza dipende dalle condizioni di installazione e controlli periodici per quelle soggette a deterioramento, con frequenze indicate dal fabbricante, dalle norme tecniche o dalle buone prassi. Alcune attrezzature, come gli apparecchi di sollevamento elencati nell’Allegato VII, sono inoltre soggette a verifiche periodiche obbligatorie: vedi la [verifica degli impianti di sollevamento](https://prosystemengineering.com/verifica-impianti-di-sollevamento/).

#### Quali sanzioni si rischiano con macchine non a norma?
Il D.Lgs. 81/08 prevede sanzioni penali, con arresto o ammenda, per il datore di lavoro e i dirigenti che mettono a disposizione dei lavoratori attrezzature non conformi ai requisiti di sicurezza (art. 87). In caso di infortunio si aggiungono la responsabilità penale per lesioni o omicidio colposo e, per le violazioni delle norme sulla sicurezza, la possibile responsabilità amministrativa dell’azienda ai sensi del D.Lgs. 231/2001. Le sanzioni e i presupposti esatti dipendono dalla violazione contestata.

#### Cosa cambia con il Regolamento Macchine (UE) 2023/1230?
Dal 20 gennaio 2027 il Regolamento (UE) 2023/1230 sostituisce la Direttiva Macchine 2006/42/CE e si applica direttamente in tutti gli Stati membri. Per chi utilizza le macchine restano validi gli obblighi del D.Lgs. 81/08; cambia il modo di valutare le modifiche, perché il Regolamento definisce espressamente la modifica sostanziale, anche se eseguita con mezzi digitali, e attribuisce gli obblighi del fabbricante a chi la esegue.
<!-- FAQ:END -->

---

## 8. Checklist pre-pubblicazione

- [ ] ThinkRank: titolo, meta description, schema WebPage, immagine social
- [ ] Un solo `<h1>` nel sorgente (`view-source:`): quello dello slider
- [ ] Alt impostati in Libreria media e controllati sulle immagini reali
- [ ] CTA e pulsante dello slider scorrono al form da telefono; form provato
- [ ] Schema: un solo FAQPage, nessun "Article"; Rich Results Test senza errori
- [ ] Affermazioni normative verificate dall'ingegnere
- [ ] Link in entrata inseriti (dalla landing revamping, home, menu, Marcatura CE)
- [ ] Cache svuotata; indicizzazione richiesta in Search Console e Bing Webmaster Tools
