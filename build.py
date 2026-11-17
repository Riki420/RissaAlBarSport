"""Ricostruisce index.html unendo src/shell.html e src/game.js.
Uso:  python build.py
"""
from pathlib import Path
root = Path(__file__).parent
shell = (root / "src" / "shell.html").read_text(encoding="utf-8")
game = (root / "src" / "game.js").read_text(encoding="utf-8")
(root / "index.html").write_text(shell + "<script>\n" + game + "</script>\n</body>\n</html>\n", encoding="utf-8")
print("index.html aggiornato")
