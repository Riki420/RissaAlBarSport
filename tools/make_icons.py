"""Genera le icone del sito (pixel art 32x32 ingrandita senza sfocatura).
Uso:  python tools/make_icons.py
Crea in assets/: icon-512.png, icon-192.png, apple-touch-icon.png, favicon-32.png
"""
from pathlib import Path
from PIL import Image, ImageDraw
import math

root = Path(__file__).resolve().parent.parent
out = root / "assets"
out.mkdir(exist_ok=True)

N = 32
img = Image.new("RGBA", (N, N), "#1a1430")
d = ImageDraw.Draw(img)
px = lambda x, y, c: d.point((x, y), fill=c)
rect = lambda x, y, w, h, c: d.rectangle((x, y, x + w - 1, y + h - 1), fill=c)

# esplosione dietro il boccale
cx, cy = 16, 13
for y in range(N):
    for x in range(N):
        a = math.atan2(y - cy, x - cx)
        r = math.hypot(x - cx, y - cy)
        spike = 9 + 3.5 * math.cos(a * 8)
        if r < spike:
            px(x, y, "#ff8a2a" if r > spike - 3 else "#ffd35a")

# boccale di birra
rect(10, 8, 10, 13, "#2a1a0a")          # contorno
rect(11, 9, 8, 11, "#f0a820")           # birra
rect(11, 9, 2, 11, "#ffd060")           # luce
rect(17, 9, 2, 11, "#c88010")           # ombra
for y in (12, 15, 18):
    px(14, y, "#fff2b0")                # bollicine
rect(20, 11, 3, 1, "#2a1a0a"); rect(22, 11, 1, 7, "#2a1a0a"); rect(20, 17, 3, 1, "#2a1a0a")
rect(20, 12, 2, 5, "#e8e8f0")           # manico
rect(9, 5, 12, 4, "#2a1a0a")            # schiuma (contorno)
rect(10, 6, 10, 3, "#ffffff")
for x in (10, 13, 16, 19):
    px(x, 5, "#ffffff")
px(12, 7, "#d8d8e0"); px(17, 7, "#d8d8e0")

# scritta RISSA (font 3x5 del gioco)
MINI = {"R": ["110", "101", "110", "101", "101"], "I": ["111", "010", "010", "010", "111"],
        "S": ["111", "100", "111", "001", "111"], "A": ["010", "101", "111", "101", "101"]}
word, x0, y0 = "RISSA", 6, 23
rect(x0 - 1, y0 - 1, len(word) * 4 + 1, 7, "#2a0a12")
for i, ch in enumerate(word):
    for ry, row in enumerate(MINI[ch]):
        for rx, v in enumerate(row):
            if v == "1":
                px(x0 + i * 4 + rx, y0 + ry, "#ff4a5a")

for size, name in ((512, "icon-512.png"), (192, "icon-192.png"), (180, "apple-touch-icon.png"), (32, "favicon-32.png")):
    img.resize((size, size), Image.NEAREST).save(out / name)
print("icone create in", out)
