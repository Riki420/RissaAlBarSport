# Rissa al Bar Sport — note per Claude

Picchiaduro arcade 2D in pixel art per browser, in stile Street Fighter. Tutto gira in un solo file HTML, senza librerie: canvas 2D e WebAudio. Lingua del gioco e dell'utente: **italiano**.

## File
- `src/game.js`: tutto il codice. **Si modifica qui.**
- `src/shell.html`: HTML/CSS della pagina, barra comandi e pulsanti touch.
- `build.py`: unisce shell e game.js in `index.html`. **Va lanciato dopo ogni modifica** (`python build.py`).
- `index.html`: file generato. Non va modificato a mano.
- **Sito**: pubblicato con GitHub Pages da `main` (https://riki420.github.io/RissaAlBarSport/). I meta tag per l'anteprima del link (og:*) e il collegamento al manifest sono in `src/shell.html`; gli URL di og:image devono essere assoluti.
- `manifest.webmanifest` e `sw.js` rendono il gioco installabile e giocabile offline. Il service worker usa prima la rete per i file del sito, quindi gli aggiornamenti arrivano subito. Se aggiungi file da tenere in cache, aggiornali in `CORE` e cambia `VERSION`.
- `assets/`: icone (generate da `tools/make_icons.py`, pixel art 32x32 ingrandita) e `og-image.jpg` (1200x630, schermata del titolo).

## Architettura (src/game.js)
- La risoluzione interna è 384x216, ingrandita via CSS con `image-rendering: pixelated`. Arena larga 576 (`WW`) con camera che scorre; pavimento a `GROUND=204`.
- Il loop è a passo fisso, 60 step/s: `step()` per la logica e `render()` per il disegno. Stati in `mode`: title, options, select, stage, vs, fight, over, continue, ending, results.
- Le modalità sono in `gameMode`: arcade, versus, 2p, survival, training.
- **Motore sprite** (`buildSprite`): i personaggi sono disegnati da uno scheletro con articolazioni definite in `basePose`/`poseOf`. Angoli in gradi: 0 = verso il basso, 90 = in avanti, 180 = in alto. Gli arti sono tratti spessi con ombra e luce, le teste sono pixel art fatta con rettangoli (`headXxx(R,P)`, coordinate relative al collo, x positiva = verso dove guarda). Dopo il disegno c'è una post-elaborazione: soglia alfa, palette quantizzata e contorno di 1px. Gli sprite sono in cache per id, posa e frame.
- Il testo sul cappello di Giuso usa `MIRROR` per non comparire rovesciato quando guarda a sinistra.
- **Arene**: `paintBarSportFar/Near`, `paintBayonsFar/Near` e `paintCeppoFar/Near` disegnano su canvas fuori schermo con parallasse (piano lontano a velocità 0.5). Ogni voce di `STAGES` ha nome, funzioni di disegno e brano (`song`); `NS` è il numero di arene, usato da selezione, arcade e sopravvivenza. Le animazioni (ventilatore, cabinato, flipper, insegne) sono in `drawStage`, divise per indice di arena.
- **Da Ceppo** è una sala interna: il piano vicino ha un'apertura (x 226-420, y 38-190) da cui si vede la sala in fondo. Le animazioni del piano lontano vanno ritagliate con `clip` su quell'apertura.
- **Musica**: sequencer chiptune in `SONGS` (title, barsport, bayons, ceppo, victory). Le note sono stringhe di 16 passi per battuta: `-` prolunga la nota, `.` è una pausa.
- **IA**: `aiInput`, regolata da `DIFFS` (Facile, Normale, Difficile, Leggenda).
- **Prese** (sezione PRESE prima di `updateFighter`): avanti + pugno entro `THROW_RANGE` contro un avversario a terra (anche se para). `THROWS` dà a ogni personaggio nome e tipo (`slam`, `suplex`, `toss`). Chi afferra è nello stato `grab` (`updateGrab` muove la vittima). La vittima passa per `held`, `thrown` e `down`, che sono disegnati ruotati attorno al centro del corpo (`f.cy`, `f.rot`). Il danno all'atterraggio è in `throwLand`/`throwDamage`. Negli stati `NOHIT` non si viene colpiti. Per aggiungere un personaggio, aggiungi anche la sua voce in `THROWS`.
- **Danni**: `applyHit` applica forza, difesa, abilità passive, barra Rabbia/Super e modalità allenamento.

## Personaggi (CHARS / STATS / PAL / headXxx)
| id | nome | speciale | abilità |
|---|---|---|---|
| badilino | Badilino | Spruzzo d'Unto (proiettile) | Scivoloso: 18% di schivata |
| pitti | Il Pitti | Berretto Boomerang | Pellaccia: difesa alta |
| bombarolo | Bombarolo | Bomba di Capodanno (arco, esplode) | Miccia corta |
| lollo | Lollo Miao (barista col grembiule) | Urlo Miaooo (anelli sonori) | Sette vite |
| giuso | Giuso (contadino di Fradusto, cappello di paglia "SARDEGNA") | Trattore di Fradusto (rasoterra) | Doppio salto |
| bingo | Bingo Baby (ubriaca, barcolla, "HIC!") | Rutto Alcolico (nube lenta) | Barcollo |
| michelo | Michelo (ricci scuri, giacca verde-grigia; lancia banchi e fa smorfie a lezione) | Lancio del Banco (parabola, si spacca a terra con `breakDesk`) | Smorfia: 20% di stordimento extra |

- La faccia di Michelo ha due versioni: `headMichelo(R,P,grin)`. La smorfia (occhi storti e linguaccia) compare nel rilascio della speciale, nella vittoria e per 45 frame quando scatta l'abilità (`f.smirk`). In `poseOf` queste pose hanno la chiave con il suffisso `g`.

- Per **aggiungere un personaggio** servono una voce in `CHARS`, `STATS`, `PAL`, `SPEC_LINES` e `IDS`, una funzione `headNome`, i dettagli del busto in `buildSprite`, la posa della speciale in `poseOf`, il proiettile in `spawnProj1`, `updateProjs` e `drawProj`, e il colore della scintilla in `applyHit`.
- Personaggi rappresentati: amici dell'utente, con soprannomi scherzosi. **Non** si aggiungono personaggi famosi reali né marchi registrati: per esempio lo stemma sul cappello di Danielino è generico (Danielino è stato rimosso, ma il codice è ancora presente).

## Comandi
- **P1**: WASD + F (pugno), G (calcio), H (speciale).
- **P2**: frecce + K, L, Ò (Semicolon) oppure tastierino 1/2/3.
- **Altri tasti**: ESC pausa, M audio, N musica, T manichino in allenamento.
- **Joypad** (`pollPads`, chiamato a ogni `step()`): il 1° joypad simula i tasti di P1 e il 2° quelli di P2, scrivendo in `keys`/`buf`. A pugno, B calcio, X/Y/RB/RT speciale, START = ESC in combattimento e INVIO nei menu, SELECT = ESC (in pausa = INVIO, torna al menu).

## Verifica
Dopo le modifiche: `python build.py`, poi apri `index.html` nel browser. Controlla la console del browser per eventuali errori.
