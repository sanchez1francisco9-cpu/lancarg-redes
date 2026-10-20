# lancarg-redes

Repositorio público con las imágenes que se publican en las redes de Transportes Lancarg.
Metricool descarga cada imagen desde su link "raw" de GitHub. Acá va SOLO contenido que se publica: nunca datos internos.

## Antes de diseñar

- Leer la Guía de contenido (doc de Claude): https://claude.ai/code/artifact/da1707bc-728b-4f0f-b727-094289d8617d
  Ahí están el foco (paquetería chica), los valores, el tono, las reglas, los teléfonos y las ideas de formatos.
- Reglas que no se rompen: logo SIEMPRE original (nunca recoloreado ni en blanco; sobre verde va en un recuadro blanco),
  nunca mencionar la cantidad de camiones, no inventar reseñas, no copiar a la competencia, no usar Higgsfield ni generadores pagos.

## Carpetas

- `fotos/` — fotos reales de la empresa (camiones, depósitos, cajas). Base de todos los diseños.
- `marca/` — logos originales. `logo-lancarg-color-transparente.png` es el que va en los diseños.
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
   providers facebook + instagram, zona horaria America/Buenos_Aires. Las historias van sin texto.
6. Si una idea necesita una imagen que no existe, programarla con una foto alternativa y pedírsela a Fran en el resumen.
7. Mandar a Fran un resumen corto: qué quedó programado y cuándo, y las imágenes que hacen falta.
