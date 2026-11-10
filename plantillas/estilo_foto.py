"""Estilo secundario "foto completa" (Fran, 10-nov-2026): foto a todo el cuadro, texto blanco sobre el cielo,
línea blanca y frase en caja roja. Sin logo (Fran: no hace falta, así no queda cargado). Texto nunca sobre el camión.
Uso: from estilo_foto import page, foto  ->  page([foto("feed"|"story", ...)])
"""
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#777;font-family:Inter,sans-serif}
.slide{width:1080px;position:relative;overflow:hidden;margin-bottom:20px;background:#5d86b8}
.story{height:1920px}.feed{height:1350px}
.photo{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.shade{position:absolute;left:0;right:0;top:0;background:linear-gradient(180deg,rgba(10,30,50,.40),rgba(10,30,50,.16) 60%,transparent)}
.shadeb{position:absolute;left:0;right:0;bottom:0;height:260px;background:linear-gradient(0deg,rgba(0,0,0,.38),transparent)}
.c{position:absolute;left:40px;right:40px;text-align:center;color:#fff}
.c h1{font-family:"Inter Display",Inter;font-weight:900;line-height:.94;letter-spacing:-.035em;text-transform:uppercase;text-shadow:0 6px 30px rgba(0,0,0,.25)}
.c h2{font-family:"Inter Display",Inter;font-weight:500;letter-spacing:-.01em;line-height:1.12;margin-top:16px;text-shadow:0 4px 20px rgba(0,0,0,.3)}
.line{width:300px;height:5px;background:#fff;margin:30px auto 26px;border-radius:3px}
.box{display:inline-block;background:#E70A0F;color:#fff;font-weight:800;font-style:italic;padding:6px 26px 10px;letter-spacing:-.01em;line-height:1.2}
.cta{position:absolute;right:0;bottom:44px;text-align:right;color:#fff;font-weight:800;font-size:38px;line-height:1.15;background:#E70A0F;padding:16px 46px 18px 40px;border-radius:14px 0 0 14px;box-shadow:0 10px 26px rgba(0,0,0,.25)}
.cta small{display:block;font-size:24px;font-weight:600}
.story .cta{font-size:48px;bottom:80px;padding:20px 50px 22px 46px}.story .cta small{font-size:30px}
"""


def foto(kind, photo, h1, h2=None, box=None, top=None, pos="50% 0%", h1_size=None, h2_size=None, box_size=None, cta=True, shade=0.40, extra=""):
    H = 1920 if kind == "story" else 1350
    top = top if top is not None else (300 if kind == "story" else 180)
    h1_size = h1_size or (140 if kind == "story" else 132)
    h2_size = h2_size or (60 if kind == "story" else 56)
    box_size = box_size or (50 if kind == "story" else 50)
    out = [f'<div class="slide {kind}">',
           f'<img class="photo" src="../../fotos/{photo}" style="object-position:{pos}">',
           f'<div class="shade" style="height:{int(H * .55)}px;background:linear-gradient(180deg,rgba(10,30,50,{shade}),rgba(10,30,50,{shade*.45:.2f}) 60%,transparent)"></div><div class="shadeb"></div>',
           f'<div class="c" style="top:{top}px"><h1 style="font-size:{h1_size}px">{h1}</h1>']
    if h2:
        out.append(f'<h2 style="font-size:{h2_size}px">{h2}</h2>')
    if box:
        out.append(f'<div class="line"></div><div class="box" style="font-size:{box_size}px">{box}</div>')
    out.append('</div>')
    out.append(extra)
    if cta:
        out.append('<div class="cta"><small>Cotizá por WhatsApp</small>264 454-3612</div>')
    out.append('</div>')
    return "\n".join(out)


def page(slides):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>\n' + "\n".join(slides) + "\n</body></html>"
