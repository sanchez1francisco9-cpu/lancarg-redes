# lancarg-redes

Repositorio público con las imágenes que se publican en las redes de Transportes Lancarg.
Metricool descarga cada imagen desde su link "raw" de GitHub. Acá va SOLO contenido que se publica: nunca datos internos.

## Antes de diseñar

- Leer la Guía de contenido (doc de Claude): https://claude.ai/code/artifact/da1707bc-728b-4f0f-b727-094289d8617d
  Ahí están el foco (paquetería chica), los valores, el tono, las reglas, los teléfonos y las ideas de formatos.
- Logo: sobre fondo verde o foto usar `marca/logo-lancarg-sobre-verde.png` (rojo original + letras verdes pasadas a blanco,
  aprobado por Fran), sin recuadro, con sombra suave y con la parte de arriba de la foto oscurecida para que se lea.
  Sobre fondo blanco o claro, usar el logo original a color. No inventar otras versiones del logo.
- Fotos: nunca recortar personas ni camiones. En historias (9:16) las fotos horizontales van completas
  (object-fit: contain, centradas un poco arriba) sobre el fondo verde; ver `photo()` en plantillas/generar_semana_*.py.
- Vocabulario: decir "paquete/paquetes", no "caja"; "camiones" en plural (ej. "Camiones todos los días").
- Reglas que no se rompen: nunca mencionar la cantidad de camiones, no inventar reseñas, no copiar a la competencia,
  no usar Higgsfield ni generadores pagos.

## Carpetas

- `fotos/` — fotos reales de la empresa (camiones, depósitos, cajas). Base de todos los diseños.
- `marca/` — logos. `logo-lancarg-sobre-verde.png` para fondos verdes o fotos; `logo-lancarg-color-transparente.png` para fondos claros.
- `pedidos/` — imágenes que Fran crea a pedido (también puede subirlas a Drive, carpeta "fotos lancarg").
- `plantillas/` — `ejemplo-carrusel.html` (estilo de referencia) y `render.py`.
- `publicaciones/AAAA-MM-DD-tema/` — una carpeta por pieza: `diseno.html` + los JPG renderizados.

## Flujo semanal (lunes)

1. Revisar en Metricool (marca "Expreso Lancarg", Facebook + Instagram @lancargsan) qué hay programado y qué rindió.
2. Armar la semana: 4 publicaciones de feed (lunes, miércoles, viernes, domingo) y 14 historias (2 por día).
3. Por cada pieza: `publicaciones/<fecha>-<tema>/diseno.html` con `.slide` de 1080x1350 (feed) o 1080x1920 (historia),
   renderizar con `python3 -I plantillas/render.py publicaciones/<carpeta>/diseno.html lancarg` y mirar cada JPG antes de subirlo.
4. `git add`, commit y push a `main`.
5. Programar en Metricool con `media` = `https://raw.githubusercontent.com/sanchez1francisco9-cpu/lancarg-redes/main/<ruta>`,
   providers facebook + instagram, zona horaria America/Buenos_Aires, `autoPublish: false` (y `instagramData.autoPublish: false`):
   a la hora programada le llega a Fran un aviso en la app de Metricool y él aprueba y publica. Las historias van sin texto.
6. Si una idea necesita una imagen que no existe, programarla con una foto alternativa y pedírsela a Fran en el resumen.
7. Mandar a Fran un resumen corto: qué quedó programado y cuándo, y las imágenes que hacen falta.
