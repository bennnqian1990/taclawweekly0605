#!/usr/bin/env python3
"""Generate premium OG cover image for social sharing card - v2"""

from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1200, 630
img = Image.new('RGB', (W, H))
draw = ImageDraw.Draw(img)

# Deep dark blue gradient background
for y in range(H):
    ratio = y / H
    r = int(10 + (18 - 10) * min(ratio * 2, 1))
    g = int(22 + (35 - 22) * min(ratio * 2, 1))
    b = int(40 + (65 - 40) * min(ratio * 2, 1))
    if ratio > 0.5:
        sub_r = (ratio - 0.5) * 2
        r = int(r + (13 - r) * sub_r)
        g = int(g + (45 - g) * sub_r)
        b = int(b + (85 - b) * sub_r)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# Font loading
def get_font(size):
    paths = [
        "C:/Windows/Fonts/msyhbd.ttc",  # Bold YaHei
        "C:/Windows/Fonts/msyh.ttc",
        "C:/Windows/Fonts/simhei.ttf",
    ]
    for fp in paths:
        try:
            return ImageFont.truetype(fp, size)
        except:
            continue
    return ImageFont.load_default()

font_tiny = get_font(14)
font_label = get_font(22)
font_title_big = get_font(68)
font_title_sub = get_font(48)
font_date = get_font(24)

# === Decorative elements ===

# Large subtle circle glow top-right
for r in range(500, 0, -8):
    alpha = int(12 * (r / 500) ** 1.5)
    color = (20 + alpha, 100 + alpha // 2, 180 + alpha)
    draw.ellipse([W-300-r//2, -r//2, W-300+r//2, r//2], fill=color)

# Teal glow bottom-left
for r in range(350, 0, -6):
    alpha = int(10 * (r / 350) ** 1.5)
    color = (15 + alpha, 180 + alpha // 3, 170 + alpha)
    draw.ellipse([-r//2, H-150-r//2, r//2, H-150+r//2], fill=color)

# Grid lines - very subtle
grid_color = (255, 255, 255, 6)
for x in range(0, W, 80):
    draw.line([(x, 0), (x, H)], fill=(255, 255, 255, 4), width=1)
for y in range(0, H, 80):
    draw.line([(0, y), (W, y)], fill=(255, 255, 255, 4), width=1)

# Diagonal accent line from bottom-right to center area
draw.line([(W+50, H+80), (W-200, H-180)], fill=(56, 189, 248, 25), width=60)

# === Main Content Area ===

# Label badge at top
label = "WEEKLY REPORT"
lbbox = draw.textbbox((0, 0), label, font=font_label)
lw = lbbox[2] - lbbox[0] + 70
lh = 44
lx = (W - lw) // 2
ly = 130

# Badge background with rounded rect effect
draw.rounded_rectangle([lx, ly, lx+lw, ly+lh], radius=22,
                       fill=(56, 189, 248, 35),
                       outline=(56, 189, 248, 90), width=1)
# Glowing dot on left of badge
draw.ellipse([lx+26, ly+14, lx+38, ly+26], fill=(56, 189, 248))
draw.ellipse([lx+28, ly+16, lx+36, ly+24], fill=(147, 237, 250))
# Badge text
tx_off = 52
draw.text((lx+tx_off, ly+9), label, fill=(140, 230, 255), font=font_label)

# === Title: TAClaw & ChatBOT 建设周报 ===

# Line 1: TAClaw & ChatBOT
title1 = "TAClaw & ChatBOT"
t1bbox = draw.textbbox((0, 0), title1, font=font_title_big)
t1w = t1bbox[2] - t1bbox[0]
t1x = (W - t1w) // 2
t1y = 210

# Draw title with cyan gradient effect
chars = list(title1)
pos_x = t1x
for i, ch in enumerate(chars):
    progress = i / max(len(chars) - 1, 1)
    # Gradient from bright cyan (#38bdf8) to teal (#2dd4bf)
    cr = int(56 + (45 - 56) * progress)
    cg = int(189 + (212 - 189) * progress)
    cb = int(248 + (191 - 248) * progress)
    # Add white highlight to first part
    if i < len("TAClaw"):
        cr = min(cr + 120, 255)
        cg = min(cg + 120, 255)
        cb = min(cb + 120, 255)
    
    ch_bbox = draw.textbbox((0, 0), ch, font=font_title_big)
    ch_w = ch_bbox[2] - ch_bbox[0]
    draw.text((pos_x, t1y), ch, fill=(cr, cg, cb), font=font_title_big)
    
    # Subtle shadow/glow under each char
    pos_x += ch_w

# Line 2: 建设周报
title2 = "建设周报"
t2bbox = draw.textbbox((0, 0), title2, font=font_title_sub)
t2w = t2bbox[2] - t2bbox[0]
t2x = (W - t2w) // 2
t2y = 305
draw.text((t2x, t2y), title2, fill=(220, 240, 255), font=font_title_sub)

# === Date section ===
date_text = "2026.05.15"
dbbox = draw.textbbox((0, 0), date_text, font=font_date)
dw = dbbox[2] - dbbox[0]
line_len = 55
gap = 20
total_w = line_len + gap + dw + gap + line_len
dx = (W - total_w) // 2
dy = 400

# Left decorative line - gradient
for i in range(line_len):
    prog = i / line_len
    a = int(80 * prog ** 2)
    c = (int(56 + (45-56)*prog), int(189+(212-189)*prog), int(248+(191-248)*prog))
    draw.line([(dx+i, dy+14), (dx+i, dy+14)], fill=c, width=2)

# Date text
draw.text((dx+line_len+gap, dy), date_text, fill=(160, 190, 210), font=font_date)

# Right decorative line
for i in range(line_len):
    prog = i / line_len
    c = (int(56 + (45-56)*(1-prog)), int(189+(212-189)*(1-prog)), int(248+(191-248)*(1-prog)))
    draw.line([(dx+line_len+gap+dw+gap+i, dy+14), (dx+line_len+gap+dw+gap+i, dy+14)], fill=c, width=2)

# === Corner tech decorations ===
cc = (56, 189, 248, 50)  # corner color
cs = 70  # corner size
co = 50  # offset

# Top-left
draw.line([(co, co), (co+cs, co)], fill=cc[:3]+(cc[3],), width=2)
draw.line([(co, co), (co, co+cs)], fill=cc[:3]+(cc[3],), width=2)
# Small dot at corner
draw.ellipse([co-4, co-4, co+4, co+4], fill=(56, 189, 248))

# Top-right
draw.line([(W-co-cs, co), (W-co, co)], fill=cc[:3]+(cc[3],), width=2)
draw.line([(W-co, co), (W-co, co+cs)], fill=cc[:3]+(cc[3],), width=2)
draw.ellipse([W-co-4, co-4, W-co+4, co+4], fill=(56, 189, 248))

# Bottom-left
draw.line([(co, H-co), (co+cs, H-co)], fill=cc[:3]+(cc[3],), width=2)
draw.line([(co, H-co-cs), (co, H-co)], fill=cc[:3]+(cc[3],), width=2)
draw.ellipse([co-4, H-co-4, co+4, H-co+4], fill=(45, 212, 191))

# Bottom-right
draw.line([(W-co-cs, H-co), (W-co, H-co)], fill=cc[:3]+(cc[3],), width=2)
draw.line([(W-co, H-co-cs), (W-co, H-co)], fill=cc[:3]+(cc[3],), width=2)
draw.ellipse([W-co-4, H-co-4, W-co+4, H-co+4], fill=(45, 212, 191))

# Small version indicator
ver = "TA Claw Weekly"
vbox = draw.textbbox((0, 0), ver, font=font_tiny)
vw = vbox[2] - vbox[0]
draw.text((co+cs+15, co-5), ver, fill=(80, 110, 140), font=font_tiny)

output_path = "C:/Users/BenQian/WorkBuddy/2026-05-14-task-7/og-cover-new.png"
img.save(output_path, "PNG")
print(f"Cover image saved: {output_path} ({img.size})")