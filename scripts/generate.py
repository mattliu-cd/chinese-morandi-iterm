#!/usr/bin/env python3
"""生成中式莫兰迪 iTerm2 配色的所有产物:

  Morandi-Day.itermcolors / Morandi-Night.itermcolors   配色文件(可导入 Color Presets)
  dynamic-profiles/*.json                                iTerm2 动态 Profile
  screenshots/day.svg / night.svg                        README 预览图

改色只需修改下方 PALETTES,然后运行: python3 scripts/generate.py
"""
import json
import os
import plistlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

COLOR_KEYS = [
    "Background Color", "Foreground Color", "Bold Color",
    "Cursor Color", "Cursor Text Color",
    "Selection Color", "Selected Text Color", "Link Color",
] + [f"Ansi {i} Color" for i in range(16)]

PALETTES = {
    "day": {
        "title": "中式莫兰迪 · 昼",
        "file": "Morandi-Day",
        "profile_name": "莫兰迪·昼 (Morandi Day)",
        "guid": "5B8A1E2C-3D4F-4A5B-9C6D-7E8F0A1B2C3D",
        "colors": {
            "Background Color": "#2D3236",  # 玄青
            "Foreground Color": "#DAD4C6",  # 月白
            "Bold Color": "#EDE9DC",        # 宣纸白
            "Cursor Color": "#C4AA7A",      # 缃黄
            "Cursor Text Color": "#2D3236",
            "Selection Color": "#46525B",   # 黛瓦灰
            "Selected Text Color": "#EDE9DC",
            "Link Color": "#8FA9BE",        # 石青
            "Ansi 0 Color": "#3A4046",      # 苍灰
            "Ansi 1 Color": "#B0766B",      # 朱砂灰
            "Ansi 2 Color": "#8C9C7C",      # 竹青
            "Ansi 3 Color": "#C3A97B",      # 缃色
            "Ansi 4 Color": "#7E94A7",      # 黛蓝
            "Ansi 5 Color": "#A190A2",      # 藕荷
            "Ansi 6 Color": "#89A49F",      # 天青
            "Ansi 7 Color": "#DAD4C6",      # 月白
            "Ansi 8 Color": "#6C7178",      # 烟灰
            "Ansi 9 Color": "#C78D82",      # 妃色
            "Ansi 10 Color": "#A5B596",     # 松花绿
            "Ansi 11 Color": "#D7C096",     # 藤黄
            "Ansi 12 Color": "#98ADC0",     # 石青
            "Ansi 13 Color": "#B8AAB9",     # 紫檀灰
            "Ansi 14 Color": "#A3BDB6",     # 青瓷
            "Ansi 15 Color": "#EDE9DC",     # 宣纸白
        },
    },
    "night": {
        "title": "中式莫兰迪 · 夜",
        "file": "Morandi-Night",
        "profile_name": "莫兰迪·夜 (Morandi Night)",
        "guid": "6C9B2F3D-4E5A-4B6C-8D7E-8F9A0B1C2D3E",
        "colors": {
            "Background Color": "#21252B",  # 玄黑
            "Foreground Color": "#C9C2B2",  # 月白·暗
            "Bold Color": "#E3DDCE",
            "Cursor Color": "#B89A6C",      # 缃黄·暗
            "Cursor Text Color": "#21252B",
            "Selection Color": "#3D4750",   # 黛瓦灰·深
            "Selected Text Color": "#E3DDCE",
            "Link Color": "#7E99AE",
            "Ansi 0 Color": "#31363C",      # 苍灰·深
            "Ansi 1 Color": "#A0695F",      # 朱砂灰·深
            "Ansi 2 Color": "#7E8D70",      # 竹青·深
            "Ansi 3 Color": "#B29870",      # 缃色·深
            "Ansi 4 Color": "#6F8496",      # 黛蓝·深
            "Ansi 5 Color": "#908193",      # 藕荷·深
            "Ansi 6 Color": "#7A938E",      # 天青·深
            "Ansi 7 Color": "#C9C2B2",      # 月白·暗
            "Ansi 8 Color": "#5F646B",      # 烟灰·深
            "Ansi 9 Color": "#B57F75",      # 妃色·深
            "Ansi 10 Color": "#95A486",     # 松花绿·深
            "Ansi 11 Color": "#C5AE86",     # 藤黄·深
            "Ansi 12 Color": "#889DAF",     # 石青·深
            "Ansi 13 Color": "#A799A8",     # 紫檀灰·深
            "Ansi 14 Color": "#93ACA6",     # 青瓷·深
            "Ansi 15 Color": "#DCD5C5",     # 宣纸白·暗
        },
    },
}


def comp(hex_color):
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    return {"Red Component": r, "Green Component": g, "Blue Component": b,
            "Alpha Component": 1.0, "Color Space": "sRGB"}


def write_itermcolors(p):
    path = os.path.join(ROOT, f"{p['file']}.itermcolors")
    with open(path, "wb") as f:
        plistlib.dump({k: comp(p["colors"][k]) for k in COLOR_KEYS}, f, sort_keys=True)
    return path


def write_dynamic_profile(p):
    path = os.path.join(ROOT, "dynamic-profiles", f"{p['file']}.json")
    profile = {"Name": p["profile_name"], "Guid": p["guid"],
               "Dynamic Profile Parent Name": "Default",
               **{k: comp(p["colors"][k]) for k in COLOR_KEYS}}
    with open(path, "w") as f:
        json.dump({"Profiles": [profile]}, f, indent=2, ensure_ascii=False)
    return path


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def write_svg(p):
    c = p["colors"]
    bg, fg = c["Background Color"], c["Foreground Color"]
    W, H = 760, 500
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}" font-family="Menlo, monospace">',
         f'<rect width="{W}" height="{H}" rx="12" fill="{bg}"/>']
    for i, k in enumerate(["Ansi 1 Color", "Ansi 3 Color", "Ansi 2 Color"]):
        s.append(f'<circle cx="{42 + i * 24}" cy="34" r="6" fill="{c[k]}"/>')
    s.append(f'<text x="380" y="40" font-size="15" fill="{fg}" text-anchor="middle">'
             f'{esc(p["title"])} · Morandi for iTerm2</text>')
    lines = [
        ("Ansi 2 Color", "$ git push origin main"),
        ("Ansi 4 Color", "Documents/  Downloads/  codework/"),
        ("Ansi 2 Color", "[ok] build passed, 128 tests"),
        ("Ansi 1 Color", "[error] preset not found"),
        ("Ansi 3 Color", "[warn] deprecated option"),
        ("Ansi 6 Color", "commit 9f3a2c1 (main)"),
    ]
    y = 80
    for k, t in lines:
        s.append(f'<text x="42" y="{y}" font-size="14" fill="{c[k]}">{esc(t)}</text>')
        y += 26
    y0 = 252
    for i in range(16):
        row, col = divmod(i, 8)
        x, yy = 42 + col * 85, y0 + row * 96
        hexv = c[f"Ansi {i} Color"]
        s.append(f'<rect x="{x}" y="{yy}" width="72" height="48" rx="6" fill="{hexv}"/>')
        s.append(f'<text x="{x + 36}" y="{yy + 66}" font-size="11" fill="{fg}" '
                 f'text-anchor="middle" opacity="0.8">{hexv}</text>')
        s.append(f'<text x="{x + 36}" y="{yy + 82}" font-size="11" fill="{fg}" '
                 f'text-anchor="middle" opacity="0.55">ANSI {i}</text>')
    s.append(f'<text x="42" y="{y0 + 222}" font-size="13" fill="{fg}">'
             f'背景 {bg} · 前景 {fg} · 光标 {c["Cursor Color"]} · 选区 {c["Selection Color"]}</text>')
    s.append('</svg>')
    path = os.path.join(ROOT, "screenshots", f"{p['file'].split('-')[1].lower()}.svg")
    with open(path, "w") as f:
        f.write("\n".join(s) + "\n")
    return path


def main():
    os.makedirs(os.path.join(ROOT, "dynamic-profiles"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "screenshots"), exist_ok=True)
    for p in PALETTES.values():
        for path in (write_itermcolors(p), write_dynamic_profile(p), write_svg(p)):
            print(os.path.relpath(path, ROOT))


if __name__ == "__main__":
    main()
