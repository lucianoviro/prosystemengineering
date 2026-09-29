# Landing 1 — Revamping macchinari industriali

URL: `https://prosystemengineering.com/revamping-macchinari-industriali/` (ID pagina 6969)

> **Versione 2**, basata sull'export WordPress del 29/09/2026 (contenuto e struttura Elementor reali) e sul sorgente HTML della pagina pubblicata. **Il plugin SEO del sito è ThinkRank, non Yoast**.
> Sostituisce la prima bozza, che ipotizzava interventi su quadri elettrici e PLC: la pagina reale è centrata su **progettazione meccanica, sicurezza e Marcatura CE**, e i testi seguono quel posizionamento.

Come applicare le modifiche:

| Cosa | Come | File |
|---|---|---|
| Meta description, titolo SEO, immagine social, lingua | A mano in ThinkRank (§2) | — |
| Struttura titoli, nuovi blocchi, FAQ, link, alt, ancora mobile | Import del template Elementor e sostituzione del contenuto (§7) | `elementor/revamping-ottimizzata.json` |
| Schema Service + FAQPage | Snippet nel `<head>` | `schema/revamping-macchinari-industriali.html` |
| Autore, data, caso reale, controllo slider | A mano (§5): servono dati che solo Prosystem ha | — |

---

## 1. Cosa emerge dall'export

| # | Rilievo | Impatto | Correzione |
|---|---|---|---|
| 1 | **Meta description generata a caso**: ThinkRank (l'unico plugin SEO attivo; i campi Yoast dell'export sono residui non usati) ricava la descrizione dall'inizio del testo, e nel sorgente risulta `AGGIORNA IL TUO IMPIANTO SENZA SOSTITUIRLO Il revamping di un macchinario industriale è l'intervento con cui una macchina o un impianto già in uso viene...` (maiuscolo, tagliata a metà frase). Stessa descrizione in Open Graph e Twitter. `og:image` è il logo, `og:locale` è `en_US` | **Alto**: è il testo mostrato nei risultati di ricerca e nelle condivisioni | Descrizione scritta a mano, immagine social e lingua (§2) |
| 2 | **9 titoli H1** nel corpo (uno per sezione, più i due della sezione contatti duplicata), oltre all'H1 dello slider. Il primo titolo nel corpo, con la frase più importante, è un **H4**; nessun titolo contiene "macchinari industriali" in posizione di H1 | **Medio-alto**: la gerarchia non dice a Google e alle AI di cosa parla la pagina | Un solo H1 con la keyword, le sezioni diventano H2, i sottotitoli H3 (§3) |
| 3 | I 4 bottoni CTA puntano a `#richiedi-una-valutazione`, ma la sezione con quell'ID è **nascosta su mobile** (esiste una copia separata per il mobile, senza ID) | **Alto sulle conversioni**: su telefono i bottoni molto probabilmente non scorrono al form (da provare) | Ancora su un elemento sempre visibile (§4) |
| 4 | **Nessun link interno**: l'unico link è l'ancora al form. Nemmeno verso la landing adeguamento, pur citando D.Lgs. 81/08 e Marcatura CE | Medio: la pagina non passa né riceve autorità dalle pagine sorelle | Link nel testo della sezione sicurezza e nelle FAQ (§4) |
| 5 | **Sezione contatti duplicata** (desktop e mobile): nell'HTML ci sono due volte titolo, indirizzo, mappa e lo stesso form (WPForms 6971), con ID del form duplicati | Medio: contenuto ripetuto, peso delle due mappe | Titoli della copia mobile declassati a testo. Per il resto vedi §5 |
| 6 | **Testi alternativi**: nel sorgente le 3 immagini principali hanno `alt=""`, le 6 icone dei passi `alt="01@4x.png"` (nome file) e l'immagine "Esperienza" il nome del file. L'import del template **non conserva gli alt** e ha ricreato le immagini in libreria con il suffisso `-1` | Medio-basso | Testo alternativo in Libreria media sulle nuove immagini (§5) |
| 7 | **FAQ**: 7 domande numerate ("1. …") in un accordion i cui titoli non sono heading; il widget non genera schema FAQ. La risposta sulla Marcatura CE è corretta ma generica | Medio | Titoli H3, 9 domande, risposta CE precisa (§6) |
| 8 | **Contenuti mancanti**: definizione in apertura, confronto revamping/retrofit/macchina nuova, definizione di modifica sostanziale e Regolamento 2023/1230, autore, data, fonti, caso reale | Medio (GEO): sono gli elementi che le AI citano | Aggiunti dove possibile (§4); il resto al §5 |
| 9 | **Schema**: ThinkRank genera WebPage, Organization (nome, logo, descrizione) e BreadcrumbList. Non ci sono Service né FAQPage | Medio | Snippet Service + FAQPage (§5); per Organization vedi §5 |
| 10 | **Non verificabile dall'export**: il testo dello slider in cima alla pagina (Revolution Slider "contatti-1") | Risulta contenere l'H1 "PROGETTAZIONE REVAMPING MACCHINARI INDUSTRIALI" (dallo screenshot): resta l'H1 della pagina | §3, §5 |

Punti di forza da mantenere: testo scritto bene e coerente, sezione sicurezza già impostata correttamente ("non necessariamente" una nuova Marcatura CE), processo in 6 passi, FAQ già presenti, un solo obiettivo di conversione.

---

## 2. Valori SEO (Modifica pagina → riquadro ThinkRank)

| Campo | Valore |
|---|---|
| **Parola chiave principale** | `revamping macchinari industriali` |
| **Titolo SEO** (56 car.) | Quello attuale (`Revamping macchinari industriali – Prosystem Engineering`, 55 car.) va bene: modificarlo solo se ThinkRank lo permette senza sforzo. In alternativa `Revamping Macchinari Industriali \| Prosystem Engineering` |
| **Meta description** (149 car.) | `Revamping di macchinari e impianti industriali: riprogettazione meccanica, analisi dei rischi e Marcatura CE. Aggiorna la macchina senza sostituirla.` |
| **Slug** | invariato: `/revamping-macchinari-industriali/` |
| **Titolo e descrizione social** | Stessi valori. **Immagine 1200×630 con una foto reale** (oggi è il logo) e **lingua `it_IT`** (oggi `en_US`, impostazione probabilmente valida per tutto il sito) |
| **Schema** | Lasciare ThinkRank com'è (WebPage, Organization, BreadcrumbList) e aggiungere lo snippet Service + FAQPage (§5) |

---

## 3. Gerarchia dei titoli: prima e dopo

I titoli hanno tutti tipografia personalizzata: cambiare il tag non cambia l'aspetto. Nessuna differenza visibile. **L'unico H1 è il titolo dello slider** ("PROGETTAZIONE REVAMPING MACCHINARI INDUSTRIALI"), che contiene già la keyword e viene per primo: il titolo sotto lo slider è un H2 con il testo originale.

<!-- OUTLINE:START -->
| Titolo | Prima | Dopo |
|---|---|---|
| AGGIORNA IL TUO IMPIANTO SENZA SOSTITUIRLO | H4 | **H2** |
| QUANDO IL REVAMPING È LA SCELTA GIUSTA | H3 | **H2** |
| PROLUNGA LA VITA DELL'IMPIANTO | H4 | **H3** |
| MIGLIORA LE PRESTAZIONI E L'AFFIDABILITÀ | H4 | **H3** |
| AGGIORNA TECNOLOGIA E FUNZIONALITÀ | H4 | **H3** |
| ADEGUAMENTO E RIPROGETTAZIONE DI MACCHINE ESISTENTI | H1 | **H2** |
| Non sostituire ciò che può essere riprogettato | H2 | **testo** |
| COME AFFRONTIAMO UN PROGETTO DI REVAMPING INDUSTRIALE | H1 | **H2** |
| COSA POSSIAMO MIGLIORARE | H1 | **H2** |
| Un intervento mirato sulle reali esigenze dell'impianto | H2 | **testo** |
| ESPERIENZA NELLA PROGETTAZIONE DI MACCHINARI E IMPIANTI INDUSTRIALI | H1 | **H2** |
| Competenze multidisciplinari per intervenire su macchine e impianti complessi | H2 | **testo** |
| PERCHÉ SCEGLIERE PROSYSTEM ENGINEERING | H1 | **H2** |
| REVAMPING E SICUREZZA DELLE MACCHINE → **REVAMPING, MARCATURA CE E SICUREZZA DELLE MACCHINE** | H1 | **H2** |
| FAQ → **DOMANDE FREQUENTI SUL REVAMPING INDUSTRIALE** | H1 | **H2** |
| HAI UN MACCHINARIO DA AGGIORNARE? | H1 | **H2** |
| Contattaci e raccontaci cosa vuoi migliorare | H2 | **testo** |
| HAI UN MACCHINARIO DA AGGIORNARE? | H1 | **testo** |
| Contattaci e raccontaci cosa vuoi migliorare | H2 | **testo** |
| REVAMPING, RETROFIT O MACCHINA NUOVA? *(nuova sezione)* | — | **H2** |
| Domande delle FAQ (9, senza numerazione) | testo semplice | **H3** |

**Riepilogo**: nel corpo, prima 9 H1, 5 H2 e primo titolo in H4. Dopo: **0 H1 nel corpo** (l'H1 è quello dello slider), 11 H2, sottotitoli e slogan come testo semplice, FAQ in H3. Le righe della sezione contatti presenti due volte (desktop e mobile) sono la stessa sezione: in mobile diventano testo normale.
<!-- OUTLINE:END -->

Restano invariati i titoli H3/H4 dentro gli editor di testo (passi del processo, blocchi "Perché scegliere", sezione sicurezza): il loro aspetto dipende dal tema e cambiarli richiederebbe di ridefinire gli stili. I passi del processo restano H4 sotto un H2: un salto di livello innocuo per Google, da sistemare solo se si vuole la perfezione.

---

## 4. Cosa contiene il template Elementor

`elementor/revamping-ottimizzata.json` è la pagina attuale con queste modifiche, e nient'altro:

1. **Titoli**: sezioni H2, sottotitoli e slogan da H2 a testo semplice (§3). L'H1 resta quello dello slider.
2. **Definizione in apertura**, prima del paragrafo esistente:
   > Il revamping di un macchinario industriale è l'intervento con cui una macchina o un impianto già in uso viene aggiornato, modificato o riprogettato per migliorarne prestazioni, affidabilità, funzionalità e sicurezza, senza doverlo sostituire.
3. **Nuova sezione "Revamping, retrofit o macchina nuova?"** con tabella di confronto, dopo "Quando il revamping è la scelta giusta". Le definizioni di manutenzione, retrofit e revamping sono quelle già scritte da Prosystem nella FAQ.
4. **Sezione sicurezza** ("Revamping, Marcatura CE e sicurezza delle macchine"): il blocco *Marcatura CE e D.Lgs. 81/08* ora definisce la modifica sostanziale, cita il Regolamento (UE) 2023/1230 (applicabile dal 20 gennaio 2027) con link a EUR-Lex, l'Allegato V per le macchine antecedenti alla Marcatura CE e **linka la landing adeguamento**.
5. **FAQ**: 9 domande senza numerazione, titoli H3, testo da §6. Nuove: macchine senza Marcatura CE; cosa cambia con il Regolamento 2023/1230. Riscritta: la risposta sulla Marcatura CE.
6. **Ancora mobile**: id `contatti-revamping` sulla sezione spaziatrice sopra i due blocchi contatti (sempre visibile) e i 4 CTA ora puntano lì. L'ID originale `richiedi-una-valutazione` resta dov'era, così eventuali stili collegati non si rompono.
7. **Contatti duplicati**: i titoli della copia mobile diventano testo normale, per non avere due volte gli stessi H1/H2.
8. **Testi alternativi** nel JSON: non sopravvivono all'import di Elementor (che ricrea le immagini e perde il campo). Vanno impostati in Libreria media (§5).

Il file **non contiene segnaposto**: tutto quello che c'è è pubblicabile. Autore, data e caso reale mancano perché servono dati reali (§5).

---

## 5. Da fare a mano (non è nel file)

| Priorità | Attività | Perché |
|---|---|---|
| 1 | **ThinkRank**: meta description (§2), immagine social e lingua | Non si importano con Elementor |
| 1 | **Pulsante dello slider**: in Slider Revolution → "Landing REVAMPING" → layer del pulsante → azione *Scroll to ID*, sostituire `richiedi-una-valutazione` con `contatti-revamping` | Sul sorgente il pulsante ha ancora l'ID vecchio (nascosto su mobile): su telefono probabilmente non scorre |
| 1 | **Provare il form da telefono**: la pagina contiene due volte lo stesso form (`id="wpforms-6971"`), e da telefono è visibile la seconda copia. Inviare una richiesta di prova | ID duplicati: la validazione e l'invio potrebbero non funzionare sulla copia mobile |
| 1 | **Alt in Libreria media** sulle nuove immagini (`…-1.png`): icone "Fase 1…6", immagini principali con alt descrittivo | Vedi §1, punto 6 |
| 1 | **Slider in cima**: aprire Revolution Slider → "Landing REVAMPING" e verificare che il layer del titolo sia un H1 (lo è) e che compaia nel sorgente della pagina pubblicata (`Ctrl+U`, cerca `<h1`). Se manca, lo slider lo disegna via JavaScript: in quel caso l'H1 va rimesso nel corpo | Evita un doppio H1; il testo dello slider non è nell'export |
| 1 | **Provare i CTA da telefono** dopo la pubblicazione | Verifica del punto 3 del §1 |
| 2 | **Autore e data**: aggiungere sotto le FAQ un blocco "Contenuto a cura di [nome], ingegnere iscritto all'Ordine [provincia, n.]. Ultimo aggiornamento: [data]" | E-E-A-T: chi firma un contenuto normativo |
| 2 | **Un caso reale** (anche anonimo) in una sezione dedicata: settore, macchina, problema, intervento, esito normativo, risultati misurabili | È quello che più aumenta le citazioni delle AI; oggi la pagina non ha nessun dato reale |
| 2 | **Schema**: incollare `schema/revamping-macchinari-industriali.html` (Service + FAQPage, ThinkRank non li genera) e controllare con il Rich Results Test. **Non** incollare `schema/organization.html` finché non si è deciso dove tenere i dati aziendali: ThinkRank emette già un'Organization con lo stesso `@id`, e due blocchi con dati diversi si contraddicono | Il provider del Service punta già all'Organization di ThinkRank |
| 2 | **Plugin SEO doppi**: guardare il sorgente della pagina (`Ctrl+U`) e cercare `application/ld+json` e `<title`: devono esserci un solo `<title>`, una sola meta description, e nessun FAQPage duplicato | Il widget Accordion non genera schema, ma un secondo plugin potrebbe |
| 3 | **Link verso la pagina**: dalla landing adeguamento, dalla pagina Marcatura CE, dal menu Servizi e dalla home | Oggi la pagina ha zero link in entrata verificabili da qui |
| 3 | **Link a Marcatura CE**: nel testo della sezione sicurezza, agganciare "Marcatura CE" alla pagina corretta (esistono `/marcatura-ce/` e `/marcatura-ce-2/`: da chiarire quale tenere) | Non l'ho inserito per non linkare l'URL sbagliato |
| 3 | **Sezione contatti**: valutare di sostituire le due copie con un unico blocco responsive (un solo form, una sola mappa) | Meno peso, niente ID duplicati |
| 3 | **Agevolazioni 4.0**: se Prosystem vuole presidiare "revamping + iperammortamento", aggiungere una FAQ dedicata con link all'articolo sulle perizie asseverate. Richiede la verifica del consulente fiscale su requisiti e soglie | Ricerca commerciale molto frequente, non trattata dalla pagina |
| 3 | **Peso delle immagini**: le tre PNG principali (da 1024 px) e le icone `@4x` sono PNG; convertire in WebP e verificare il peso con PageSpeed | Non misurabile dall'export |

---

## 6. FAQ (fonte unica)

Questo blocco alimenta **sia** il template Elementor **sia** lo schema FAQPage. Se lo si modifica: rieseguire `python3 tools/ottimizza_revamping.py <export.xml>` e `python3 tools/genera_schema.py`.

Le risposte 1-5 e 7 sono quelle già scritte da Prosystem, con ritocchi minimi. Sono nuove o riscritte le risposte 6, 8 e 9. Il testo della definizione di modifica sostanziale segue l'art. 3, punto 16, del Regolamento (UE) 2023/1230; **non ho potuto consultare EUR-Lex da qui**, quindi la formulazione va confrontata con il testo ufficiale prima della pubblicazione.

<!-- FAQ:START -->
#### Che cos'è il revamping di un macchinario industriale?
Il revamping di un macchinario industriale è un intervento di aggiornamento progettuale, meccanico, tecnologico o funzionale eseguito su una macchina esistente. L'obiettivo è migliorarne prestazioni, affidabilità, sicurezza e capacità produttiva, prolungandone la vita utile ed evitando, quando possibile, la sostituzione completa dell'impianto.

#### Quando conviene effettuare il revamping di una macchina industriale?
Il revamping può essere conveniente quando la struttura della macchina è ancora valida, ma alcuni componenti risultano obsoleti oppure le prestazioni non rispondono più alle esigenze produttive. Può essere utile anche per introdurre nuove lavorazioni, aumentare la produttività, migliorare la manutenibilità o integrare nuovi sistemi di automazione e sicurezza. Il confronto con l'acquisto di una macchina nuova si fa su costi, tempi di fermo, prestazioni ottenibili e vita utile residua.

#### Qual è la differenza tra revamping, retrofit e manutenzione?
La manutenzione serve principalmente a ripristinare o preservare il corretto funzionamento della macchina. Il retrofit riguarda generalmente la sostituzione o l'integrazione di specifici componenti tecnologici. Il revamping industriale prevede invece una revisione progettuale più ampia, finalizzata a migliorare complessivamente funzionalità, prestazioni, affidabilità o sicurezza del macchinario. Per la normativa conta soprattutto se la modifica è sostanziale oppure no.

#### Quanto costa il revamping di un macchinario industriale?
Il costo di un intervento di revamping dipende dalle condizioni della macchina, dalla complessità delle modifiche e dagli obiettivi da raggiungere. Per formulare una valutazione attendibile è necessario analizzare il macchinario, verificare la documentazione disponibile e definire gli interventi meccanici, tecnologici e di sicurezza richiesti. Uno studio di fattibilità preliminare permette di valutare compatibilità tecnica, attività necessarie e criticità prima di decidere se procedere.

#### Quali macchinari industriali possono essere sottoposti a revamping?
Il revamping può interessare numerose tipologie di macchine e impianti, tra cui linee di produzione, trasportatori, rulliere, elevatori, palettizzatori, isole robotizzate, stazioni di montaggio, banchi prova e magazzini automatici. La fattibilità dell'intervento deve essere valutata caso per caso attraverso un'analisi tecnica preliminare.

#### Il revamping richiede una nuova Marcatura CE?
Non necessariamente. Serve una nuova Marcatura CE quando l'intervento è una modifica sostanziale: una modifica, non prevista né pianificata dal fabbricante, che incide sulla sicurezza della macchina creando un nuovo pericolo o aumentando un rischio esistente. In questo caso chi esegue la modifica assume gli obblighi del fabbricante: nuova valutazione dei rischi, Fascicolo Tecnico, dichiarazione di conformità e Marcatura CE. Se la modifica non è sostanziale, è comunque consigliabile documentare la valutazione svolta e aggiornare i documenti della macchina. Per le macchine già in uso valgono anche gli obblighi del [D.Lgs. 81/08](https://prosystemengineering.com/adeguamento-macchine-marcatura-ce-e-d-lgs-81-08/).

#### Come si sviluppa un progetto di revamping industriale?
Un progetto di revamping parte generalmente dal sopralluogo e dal rilievo del macchinario esistente. Seguono la definizione degli obiettivi, lo studio di fattibilità, la progettazione delle modifiche, le verifiche relative alla sicurezza e il supporto alla realizzazione. Il percorso può comprendere anche disegni costruttivi, calcoli strutturali, installazione e collaudo finale.

#### Si può fare il revamping di una macchina senza Marcatura CE?
Sì, ma il punto di partenza è diverso. Se la macchina è antecedente all'obbligo di Marcatura CE (immessa sul mercato prima del 21 settembre 1996) deve rispettare i requisiti generali di sicurezza dell'Allegato V del D.Lgs. 81/08, e il revamping va progettato mantenendo o migliorando questa conformità. Se invece è successiva a quella data ed è priva di Marcatura CE serve una valutazione tecnica specifica. Se l'intervento è una modifica sostanziale, la macchina va trattata come nuova e marcata CE. Approfondisci: [adeguamento delle macchine al D.Lgs. 81/08](https://prosystemengineering.com/adeguamento-macchine-marcatura-ce-e-d-lgs-81-08/).

#### Cosa cambia per il revamping con il Regolamento Macchine (UE) 2023/1230?
Dal 20 gennaio 2027 il Regolamento (UE) 2023/1230 sostituisce la Direttiva Macchine 2006/42/CE e si applica direttamente in tutti gli Stati membri. Per il revamping la novità principale è la definizione esplicita di modifica sostanziale, che comprende anche le modifiche eseguite con mezzi digitali, e l'attribuzione degli obblighi del fabbricante a chi la esegue. Per le macchine in servizio restano validi gli obblighi del D.Lgs. 81/08.
<!-- FAQ:END -->

---

## 7. Come importare il template (senza toccare la pagina live)

1. Elementor → **Template → Template salvati → Importa template** → scegliere `elementor/revamping-ottimizzata.json`.
2. **Pagine → Aggiungi nuova** (bozza), titolo "Revamping (bozza)", template pagina **Elementor a larghezza intera con header e footer** (come l'originale) → *Modifica con Elementor* → icona cartella → **Template salvati** → *Inserisci* "Revamping macchinari industriali (ottimizzata)".
3. Controllare l'anteprima su desktop, tablet e telefono: aspetto dei titoli, nuova tabella, CTA che scorrono al form.
4. Se tutto è a posto, due strade equivalenti:
   - copiare il contenuto della bozza nella pagina 6969 (o incollare le sezioni), oppure
   - pubblicare la bozza con slug `/revamping-macchinari-industriali/` **dopo aver cambiato lo slug della pagina vecchia** (e copiando le impostazioni ThinkRank). La prima è più sicura: non cambia l'URL né la cronologia.
5. Inserire i valori ThinkRank (§2), sistemare il pulsante dello slider (§5), pubblicare e chiedere l'indicizzazione in Search Console.

Il template contiene lo shortcode dello slider e i widget WPForms/EAEL già usati dalla pagina: l'import funziona sullo stesso sito. Non l'ho potuto provare su un WordPress: se l'import desse errore, la pagina live non subisce alcun effetto e mi si può passare il messaggio.

---

## 8. Link interni ed esterni

| Da | A | Anchor / dove |
|---|---|---|
| Revamping (sezione sicurezza) | Landing adeguamento | "adeguamento delle macchine al D.Lgs. 81/08 e Marcatura CE" (nel template) |
| Revamping (FAQ 6 e 8) | Landing adeguamento | "D.Lgs. 81/08" (nel template) |
| Revamping (sezione sicurezza) | EUR-Lex, Regolamento 2023/1230 | fonte (nel template) |
| Landing adeguamento | Revamping | "revamping dei macchinari industriali" (da fare) |
| Home e menu Servizi | Revamping | "Revamping macchinari industriali" (da fare) |
| Pagina Marcatura CE | Revamping | "Stai modificando una macchina esistente? Scopri il servizio di revamping" (da fare) |

---

## 9. Checklist pre-pubblicazione

- [ ] ThinkRank: meta description, immagine social e lingua aggiornati
- [ ] Un solo `<h1>` nel sorgente (`Ctrl+U`): quello dello slider
- [ ] I 4 CTA scorrono al form su desktop **e** su telefono
- [ ] Tabella leggibile su telefono (scorre in orizzontale)
- [ ] Testi alternativi impostati in Libreria media e controllati sulle immagini reali
- [ ] Form provato da telefono
- [ ] Definizione di modifica sostanziale confrontata con EUR-Lex
- [ ] Schema Service + FAQPage + Organization incollati e validati
- [ ] Autore, data e caso reale aggiunti
- [ ] Link in entrata inseriti
- [ ] Richiesta di indicizzazione in Search Console e Bing Webmaster Tools
