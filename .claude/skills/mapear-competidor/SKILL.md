---
name: mapear-competidor
description: Mapear por completo a un competidor o referente en Instagram y en la Biblioteca de anuncios de Meta: perfil, todos sus posts y reels con transcripción y métricas, sus anuncios activos e inactivos, pilares, los que más rindieron, qué papel juega la IA en su marca, su embudo reconstruido, y qué tomar y qué no para la oferta de Hans. Usar cuando Hans pase un competidor o una cuenta que «se parece a lo que buscamos», antes de copiar nada de ella; y para revisar la competencia del bloque 7 del OSO.
---

# Mapear un competidor

**Estado: probada una vez** (Felipe Carvajal / NuGen, 2026-10-11:
`output/investigacion/2026-10-11-felipe-carvajal-mapa.md`; crudo en
`inputs/referencias/competencia/felipe-carvajal/`). Lo que sigue es lo que funcionó y lo que se aprendió.

## Para qué

Que lo que se diga de un competidor salga de sus datos, no de la impresión que da un reel suelto. Y que
«qué tomar» quede separado de «qué no», con fuente. El informe sirve al bloque 7 del OSO
(`output/oferta/2026-10-11-oso-motor-de-clientes.md`) y a la referencia de competencia
(`knowledge/referencias/`).

## Herramientas y costo (verificado el 2026-10-11)

- **Apify** (cuenta de Hans; el pedido lo hizo él: «podemos utilizar Apify»):
  - `apify/instagram-profile-scraper` → bio, seguidores, cantidad de posts, enlace externo. ~$0,003.
  - `apify/instagram-post-scraper` (`dataDetailLevel: "detailedData"`) → todos los posts: tipo, caption,
    likes, comentarios, plays, duración. ~$0,002 por post.
  - `apify/instagram-reel-scraper` con `includeTranscript: true` y `includeSharesCount: true` → reels
    con transcripción (la hace el actor; no se bajan videos) y, si está disponible, compartidos. ~$0,05
    por minuto de video transcrito. **Para 35–50 posts, el total queda por debajo de $5.** Capar con
    `maxTotalChargeUsd`.
  - Los datasets se leen con `get-dataset-items` por páginas de 10–12 y con `fields` para no traer
    imágenes ni perfiles de comentaristas.
- **Biblioteca de anuncios de Meta** (herramienta `ads_library_search` del conector de Meta; solo
  lectura): primero por nombre para encontrar el `page_id`, luego por `page_ids` con `ad_active_status:
  ALL`. Devuelve ids, fechas, título del enlace y la URL del snapshot; **el texto del anuncio se lee
  abriendo el snapshot en el navegador** (puede pedir clic; no insistir más de dos veces).
- Un subagente puede hacer la lectura de los datasets y escribir el informe si se le pasan los ids de
  los datasets y la estructura; no debe correr actores nuevos (cuestan plata).

## Pasos

1. Perfil → posts → reels con transcripción (tres actores, en paralelo). Guardar el crudo intacto en
   `inputs/referencias/competencia/<slug>/{perfil,posts,reels,anuncios}.md`.
2. Biblioteca de anuncios: encontrar la página, listar todos los anuncios, leer los activos.
3. Informe en `output/investigacion/AAAA-MM-DD-<slug>-mapa.md` con estas secciones: ficha (bio,
   seguidores, desde cuándo publica, a quién le habla, qué vende, qué promete, palabras clave y qué
   regala por cada una); línea de tiempo (todas las piezas: fecha, tipo, tema, gancho, CTA, plays,
   vistas, likes, comentarios, duración); pilares; los que más rindieron y por qué (hipótesis); qué papel
   juega la IA en su marca y sus guiones, con frases textuales; los anuncios (qué dicen, desde cuándo,
   CTA, a dónde mandan); el embudo reconstruido; qué tomar y qué no para Hans, todo como hipótesis.
4. Cruzar con la referencia de competencia y el OSO; anotar en `knowledge/referencias/indice.md`.

## Lo que se aprendió (errores que no se repiten)

- **Un anuncio no es un reel.** `apify/instagram-reel-scraper` no devuelve publicaciones con
  `productType: ad` («empty or private data»). Para un anuncio: `apify/instagram-scraper` con `directUrls`
  trae los datos (texto, duración, vistas, tipo) y `steadyfetch/instagram-reel-transcript-scraper` con
  `reelUrls` trae la transcripción sin bajar el video (~$0,015; no cobra si falla). Caso: el anuncio de
  Cristina Cali, 2026-10-13 (`inputs/referencias/competencia/cristina-cali/`).
- **El saldo de Apify es uno solo para todos los proyectos** (conexión a nivel usuario). Si se agota, se
  usa la cuenta de respaldo según el `CLAUDE.md` global.

- **Un anuncio «creado» en una fecha no es un anuncio activo.** El 2026-10-11 se le dijo a Hans que
  siete anuncios «corrían desde abril» por la fecha de creación; estaban inactivos y habían corrido tres
  días. Se verifica el estado antes de hablar de «anuncios que funcionan». Lo que sí indica que algo
  funciona: activo y con semanas corriendo.
- Los compartidos casi nunca están disponibles aunque se pidan; no se prometen.
- Dos datasets pueden traer plays distintos para el mismo reel (IG vs. FB, o vistas vs. plays); se
  anotan los dos valores.
- Reels con plays muy por encima de los seguidores (por ejemplo 20–70 mil contra 300 seguidores) son
  casi seguro pauteados; se dice como hipótesis.
- Lo que el competidor dice de sí mismo (casos, cifras, «100 llamadas al mes») se marca como
  afirmación propia; si cuenta el mismo caso de dos maneras, se anota.
- Si Hans quiere transcripciones, el actor las hace sin bajar videos al proyecto; si alguna vez hiciera
  falta bajar un video, es una descarga de un archivo externo: se le pide OK a Hans antes.

## Lo que sigue

Las lecciones del competidor entran al OSO (bloque 7) y, si cambian la oferta o el copy, se decide con
Hans; nunca se copia un texto, una garantía ni una cifra.
