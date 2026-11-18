# Rissa al Bar Sport

Picchiaduro arcade in pixel art per browser, in un unico file HTML (nessuna installazione).

## Come giocare
Apri `index.html` con un browser (Chrome, Edge, Firefox).

**P1:** A/D muovi · W salta · S para · F pugno · G calcio · H speciale
**P2:** frecce · K pugno · L calcio · Ò (o tastierino 1/2/3)
**Presa (wrestling):** avanti + pugno quando sei vicino all'avversario. Funziona anche se l'avversario para.
**Altro:** INVIO conferma · ESC pausa · M audio · N musica · T manichino (allenamento)

**Joypad** (il 1° collegato è P1, il 2° è P2): croce o levetta muove · A pugno · B calcio · X/Y/RB/RT speciale · START pausa/conferma · SELECT indietro (in pausa: torna al menu).
Se il browser non lo rileva subito, premi un pulsante del joypad con la pagina aperta.

## Modalità
Arcade, Versus CPU, 2 Giocatori, **Rissa a 4**, Sopravvivenza, Allenamento, Opzioni (difficoltà, round, tempo, musica).

**Rissa a 4**: fino a quattro lottatori insieme, in due varianti, *tutti contro tutti* (vince l'ultimo in piedi) o *2 contro 2* a squadre, rossa contro blu. Scegli quanti giocatori sono umani: i posti liberi li prende la CPU. P1 usa la tastiera WASD o il joypad 1, P2 le frecce o il joypad 2, P3 e P4 i joypad 3 e 4.
Nella Rissa a 4 l'arena è più larga, la camera allarga lo zoom quando i lottatori si allontanano e ci sono tre piattaforme (ci si sale saltando, si scende con **giù + salto**). Ognuno ha **2 vite**: al primo K.O. rientra dall'alto, al secondo è fuori. Si vince solo per K.O., non si esce dal ring.

## Personaggi
Badilino, Il Pitti, Bombarolo, Lollo Miao, Giuso, Bingo Baby, Michelo.
Ogni personaggio ha la sua presa: Scivolone Unto, Abbraccio del Piumino, Suplex di Capodanno, Servito al Bancone, Aratura di Fradusto, Abbraccio Alcolico, Bocciatura.
Arene: Bar Sport, Bayon's Caffè, Da Ceppo (sala giochi con biliardo, calciobalilla e flipper), Spiaggetta (chiosco tra gli alberi, con patio e prato), Centro Amnil - Esterno (complesso in cemento con ponte su pilastri).

## Online e sul telefono
Si gioca su **https://riki420.github.io/RissaAlBarSport/**.
Sul telefono si può installare come app: dal menu del browser scegli "Aggiungi a schermata Home" (o "Installa app"). Si apre a schermo intero e funziona anche senza internet.

## Struttura
- `index.html` — il gioco completo, pronto da aprire
- `src/game.js` — codice del gioco (sprite, arene, musica, logica)
- `src/shell.html` — pagina HTML/CSS che contiene il gioco
- `build.py` — rigenera `index.html` dopo aver modificato i file in `src/` (`python build.py`)
- `assets/` — icone e immagine di anteprima del link (le icone si rigenerano con `python tools/make_icons.py`)
- `manifest.webmanifest`, `sw.js` — installazione come app e gioco senza internet
