---
name: escribir-ad-copy
description: Escribir el texto de un anuncio de video (90 s) a partir del diagnóstico, con la estructura del curso Media Buyers HQ (sesión 3 y Blueprint 3.0), usando AI y naturalizando el resultado. Usar cuando ya existe el diagnóstico de la oferta —de Hans o de un cliente— y hay que producir el primer ad copy o una versión nueva tras un test. Entrega el copy en el documento del cliente, tres hooks alternativos y el mensaje para que el cliente lo apruebe.
---

# Escribir el ad copy

**Estado: en prueba** (sesión 3, 2026-10-09). Aplicada a los copies 1.x y 2.x, descartados
(`output/oferta/2026-10-10-ad-copy-1-llamadas-que-llegan.md`,
`output/oferta/2026-10-11-ad-copy-2-promesa-compartida.md`, `2026-10-11-ad-copy-2.3-propuesta.md`), y al
copy 3 de sistemas, aprobado por Hans el 2026-10-11 (`output/oferta/2026-10-11-ad-copy-3-sistemas.md`).
Pasa a «probada» cuando el copy 3 se haya grabado, publicado y leído con números. Nota de uso: con Hans
los archivos van en `output/oferta/`, no en `output/clientes/`.

**Fuente:** `knowledge/curso/03-cosmic-ai-copywriting.md`; recursos en
`inputs/curso/sesion-03-cosmic-ai-copywriting/recursos/` y
`inputs/curso/recursos/Sebastian-AI-Ads-Blueprint-3.0.pdf.md`. Manual: `knowledge/manual/copy.md`.

## Antes de empezar

- Existe el diagnóstico (skill `diagnostico-de-cliente`), con las cinco preguntas de estructura
  contestadas: proceso de ventas, CTA, plataforma principal, duración, CTA `[CURSO S3 @ 0:08:04]`.
  Sin diagnóstico no se escribe: «sería como tirar los dados» `[CURSO S3 @ 0:07:29]`.
- Hay credibilidad y testimonios reales escritos; si no se meten en el prompt, el copy sale sin
  ellos `[CURSO S3 @ 1:02:40]`. Nada inventado: lo que no exista no va.
- Formato por defecto: 90 segundos, vertical, Instagram/Facebook, en la plataforma donde el
  cliente ya tiene seguidores `[CURSO S3 @ 0:12:15–0:14:58]`. Idioma y trato: lo que diga el
  diagnóstico; el curso usa **usted** `[CURSO S3 @ 0:44:50]`.

## Pasos

1. **La idea.** Leer el diagnóstico entero y decidir, en dos líneas, a quién le habla el ad, qué
   dolor y deseo toca, el mecanismo con nombre, el resultado cuantificable y el CTA. Si no sale, el
   curso da 24–48 horas para pensarla `[CURSO S3 @ 0:15:25–0:16:54]`. **Con Hans, el mecanismo se
   describe como una escena que el cliente imagina y sin nombre público hasta que esté probado**
   (decisión de Hans: `memory/decisions.md`, entradas del 2026-10-10 «La oferta tiene que sonar a Hans…»
   y del 2026-10-11 «Posicionamiento…» y «Sistemas a medida: la frase del mecanismo»); el nombre, si
   existe, queda interno.
2. **La estructura.** Por defecto los 11 bloques del Blueprint 3.0, en ese orden (hook 3–5 s →
   filtrar al cliente ideal → resultado específico → autoridad → dolores → deseos y resultado →
   mecanismo con nombre (con Hans, descrito y sin nombre público: paso 1) → obstáculo → testimonios →
   riesgo de no actuar → CTA)
   `[CURSO S3 · Blueprint, pp. 14–18]`. Si el CTA manda a un video gratuito, el final de la
   plantilla Cosmic `[CURSO S3 · Cosmic]`.
3. **El borrador con AI.** Armar el prompt de `prompt.md` (zona 1 tal cual, zona 2 con las
   respuestas del diagnóstico, zona 3 tal cual) y pedir el copy. Luego: «deme 3 variaciones con
   hooks diferentes» `[CURSO S3 · Blueprint, pp. 19–33]`. Si se escribe a mano, la misma
   estructura.
4. **Naturalizar.** Que suene a la persona que lo va a decir, no a robot ni a empresa: «si usted
   es…» en vez de «¿es usted…?», «entiendo» en vez de «entendemos»; el estilo del cliente
   `[CURSO S3 @ 0:49:45–0:51:56]`. Leerlo en voz alta y cronometrar: 90 segundos. **Antes de declarar la duración, contar las palabras con una herramienta** (nunca «~245» a ojo: el copy 2.2 decía 245 y tenía 378, 2026-10-11), **y se vuelve a contar en cada ronda y por bloque**: una versión que crece por correcciones se pasa sin que nadie lo note (`memory/learnings.md`, entrada «Declaré «~245 palabras ≈ 90 s» sin contar: el copy 2.2 tenía 378»). Referencia: a 2,7–2,8 palabras por segundo (ritmo medido de Sebastián), 90 s son unas 240–250 palabras; **hasta medir el ritmo de quien graba, el tope es 240–245 palabras** (auditoría del 2026-10-11, hallazgo A01: `output/diagnosticos/2026-10-11-auditoria-oferta-y-anuncio.md`, líneas 193–199); el cronómetro del que graba manda.
5. **Control de calidad.** Primero, el targeting está en los primeros 10 segundos: quién sí y
   quién no (exclusion marketing), salvo oferta mass appeal; «el algoritmo se hackea con un buen
   ad copy» `[CURSO S8 @ 0:18:43–0:34:46]`. Luego los secretos de copywriting
   `[CURSO S3 · Cosmic]`: el hook es el 80 %;
   simple; a un avatar específico; sin lenguaje especializado; palabras fáciles; historia; casos
   de estudio; pruebas; números específicos, no generalizaciones; cumplir la promesa; dolores,
   deseos y resultado final nombrados. Y: el CTA es el del proceso de ventas, uno solo; nada que
   viole las políticas de Meta Ads, nada engañoso `[CURSO S3 · Blueprint, p. 26]`. Dos casillas
   más, aprendidas con Hans el 2026-10-10 (`memory/learnings.md`): **congruente con la marca de
   quien habla** (¿esta persona diría esto de sí misma y su audiencia lo reconocería? el puente va
   en el bloque de autoridad) y **todo lo que promete existe hoy, o se dice como promesa, no como
   hecho**; el nombre del mecanismo solo se dice en cámara si quien lo dice se lo cree. Y cuatro
   casillas más, de la auditoría del 2026-10-11 (`output/diagnosticos/2026-10-11-auditoria-oferta-y-anuncio.md`):
   - **Una oferta por anuncio.** Si el copy sirve a dos ofertas, el mecanismo queda en lo que las dos
     tienen en común y no suena a ninguna (`memory/learnings.md`, entrada «Convertí «anuncio de
     sistemas con un giro» en «un anuncio para dos ofertas»»).
   - **La palabra clave, el umbral de precio y la cantidad de preguntas son idénticos en el copy y en
     el chat** (hallazgos K05, líneas 761–773, y C01, líneas 373–389): el video del anuncio 2 filtraba
     desde $2.000 y el chat desde $1.000; el CTA prometía dos preguntas y el chat hacía tres.
   - **Comillas solo para lo que es textual en la fuente** (A08, líneas 276–285; A15, líneas 329–338;
     `memory/learnings.md`, entrada «Comillas que no eran textuales y citas del curso imprecisas»): una
     cita del cliente va contigua y literal; un dolor que nadie dijo no se presenta como palabras del
     avatar.
   - **Cada promesa del mecanismo existe en el núcleo de la oferta** (K08, líneas 835–849): se compara
     frase por frase con el núcleo registrado en `memory/decisions.md`; lo que no esté ahí sale del
     copy o lo confirma Hans antes de grabar.
6. **Guardar y entregar.** El copy en `output/clientes/<cliente>/ad-copy-N.md` con fecha, versión,
   la estructura marcada por bloque, los 3 hooks y el formato. Al cliente: el link al documento y
   un audio leyéndolo; pedirle que revise **que sea congruente con lo que vende**, no el texto
   `[CURSO S3 @ 0:41:30–0:43:30]`. Correcciones solo si no afectan los resultados.
7. **Después.** Instrucciones de grabación (`knowledge/manual/creativos.md`): escritorio, buen
   fondo y micrófono, crudo, sin edición ni emojis. Y la expectativa: el primer ad rara vez es el
   ganador `[CURSO S2 @ 0:58:10]`. Antes de mandarlo a grabar, el nivel 1 de la skill
   `revisar-antes-de-grabar`.

## Lo que no se decide acá

- Cuántas variaciones se lanzan y con qué presupuesto: lo resuelve la skill `definir-presupuesto`
  (Protocolo Ad Budget, paso 3: ads a la vez = diario ÷ $10; principiante, 1–2), con la síntesis
  cerrada el 2026-10-09 en `knowledge/manual/campanas.md:87–92`.

## Para vender el servicio de media buying (sesión 18)

Partir de los copies done-for-you por nicho de
`inputs/curso/sesion-18-clientes-para-el-servicio/recursos/MB Service - Ad Copy 1.md` (leer con las
líneas recortadas: trae imágenes incrustadas), adaptar nicho, país y CTA, quitar los testimonios de
ejemplo (no son nuestros) y generar variaciones con el hack de la sesión 18: tres versiones
distintas → hooks controversiales en los primeros 3 segundos → el mejor hook sobre la base
`[CURSO S18 @ 1:08:06–1:14:43]`. Lo que se promete (plazos, garantías como la de «60 días o no
paga») lo decide Hans antes de escribirlo.
