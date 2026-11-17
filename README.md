# Rissa al Bar Sport

Picchiaduro arcade in pixel art per browser, in un unico file HTML (nessuna installazione).

## Come giocare
Apri `index.html` con un browser (Chrome, Edge, Firefox).

**P1:** A/D muovi · W salta · S para · F pugno · G calcio · H speciale
**P2:** frecce · K pugno · L calcio · Ò (o tastierino 1/2/3)
**Altro:** INVIO conferma · ESC pausa · M audio · N musica · T manichino (allenamento)

**Joypad** (il 1° collegato è P1, il 2° è P2): croce o levetta muove · A pugno · B calcio · X/Y/RB/RT speciale · START pausa/conferma · SELECT indietro (in pausa: torna al menu).
Se il browser non lo rileva subito, premi un pulsante del joypad con la pagina aperta.

## Modalità
Arcade, Versus CPU, 2 Giocatori, Sopravvivenza, Allenamento, Opzioni (difficoltà, round, tempo, musica).

## Personaggi
Badilino, Il Pitti, Bombarolo, Lollo Miao, Giuso, Bingo Baby.
Arene: Bar Sport, Bayon's Caffè, Da Ceppo (sala giochi con biliardo, calciobalilla e flipper).

## Struttura
- `index.html` — il gioco completo, pronto da aprire
- `src/game.js` — codice del gioco (sprite, arene, musica, logica)
- `src/shell.html` — pagina HTML/CSS che contiene il gioco
- `build.py` — rigenera `index.html` dopo aver modificato i file in `src/` (`python build.py`)
