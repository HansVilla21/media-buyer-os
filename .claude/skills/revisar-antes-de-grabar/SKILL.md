---
name: revisar-antes-de-grabar
description: Control de un anuncio antes de grabarlo o publicarlo, en dos niveles. Nivel 1, obligatorio para todo anuncio, lo hace el media buyer solo en minutos: palabras contadas con herramienta, coherencia copy–chat–llamada (palabra clave, umbral, cantidad de preguntas, promesa), promesas del mecanismo contra el núcleo decidido, citas contra su fuente, palabras prohibidas de la marca, redacción vieja de decisiones recientes y una sola oferta por anuncio. Nivel 2, solo para una oferta nueva o un cambio grande: auditores por área, verificadores que intentan refutar, panel de jueces y crítico de completitud. Usar después de escribir-ad-copy y antes de grabar-y-revisar-el-ad, y otra vez antes de publicar.
---

# Revisar antes de grabar

**Estado:** el nivel 2 está **en prueba**: aplicado una vez, en versión grande (la auditoría del
2026-10-11, `output/diagnosticos/2026-10-11-auditoria-oferta-y-anuncio.md`). El nivel 1, la versión
corta, está **diseñado, sin aplicar**; pasa a «probado» cuando se haya corrido sobre un copy antes de
grabarlo y el video no haya tenido que regrabarse por algo de esta lista. No viene del curso: sale de lo
que encontró esa auditoría.

**Por qué existe:** el copy 2.2 se aprobó y se mandó a grabar diciendo «~245 palabras» y tenía 378; el
chat calificaba con otro umbral que el video; la cita del cliente era un empalme; el mecanismo prometía
cosas que no estaban en el núcleo registrado (`memory/learnings.md`, entradas del 2026-10-11). Una lista
corta antes de grabar los atrapa; la auditoría grande queda para ofertas nuevas
(`output/diagnosticos/2026-10-11-recapitulacion-del-servicio.md`, sección 6).

## Nivel 1 — obligatorio antes de grabar o publicar cualquier anuncio

Lo hace el media buyer solo, en minutos, sobre el copy aprobado y lo que lo rodea: el chat, el guion de la
llamada y las instrucciones de grabación. Lo que falla se arregla antes de grabar, o se le pregunta a Hans
si es una decisión suya. Las líneas citadas son del informe de auditoría de arriba.

- [ ] **Palabras contadas con herramienta, por bloque y total**, sobre el texto que se va a decir (sin
      títulos ni etiquetas). Tope de 240–245 hasta medir el ritmo de quien graba; el cronómetro manda
      (skill `escribir-ad-copy`, paso 4; hallazgo A01, líneas 183–199).
- [ ] **El copy, el chat y la llamada dicen lo mismo:** la misma palabra clave; el mismo umbral de
      precio en el filtro del video y en la calificación del chat; la cantidad de preguntas que promete
      el CTA es la que hace el chat; la promesa del video es la que se ofrece en la llamada (K05, líneas
      761–773; C01, líneas 373–389). Y nada contradice una decisión vigente de Hans sobre el anuncio (por
      ejemplo, que el video no anuncia la lectura gratis: `memory/decisions.md`, entrada «Ajustes al
      anuncio único…»).
- [ ] **Cada promesa del mecanismo existe en el núcleo decidido de la oferta:** frase por frase contra
      `memory/decisions.md`; lo que no esté ahí sale del copy o lo confirma Hans (K08, líneas 835–849).
- [ ] **Citas contra su fuente:** lo que va entre comillas está textual y contiguo en la fuente; un
      dolor que nadie dijo no se presenta como palabras del avatar; una cita al curso se confirma en la
      transcripción o el recurso (A08, líneas 276–285; A15, líneas 329–338; `CLAUDE.md`, «Comillas solo
      para lo textual»).
- [ ] **Palabras prohibidas de la marca:**
      - «agentes» y «ejecuta solo» **referido a una IA que decide o actúa por su cuenta**. Lo que una
        automatización hace sola (calcular una comisión, mandar un recordatorio, armar el contrato) **sí se
        puede decir**: Hans, 2026-10-11, noche, sobre «su comisión calculada sola»: «dentro del sistema,
        técnicamente, se hacen ciertas automatizaciones… no como agentes de IA, pero igual hay
        automatizaciones» (`memory/decisions.md`, entrada «Lo que corre solo se puede decir…»);
      - «inteligencia artificial» más de una vez, o fuera de quién habla (`memory/decisions.md`, entrada
        «Sistemas a medida: sin agentes, y la IA solo en quién habla»);
      - «construyo sistemas» (se dice «instalo»), «soy media buyer», «agencia», «le manejo los anuncios»,
        «chatbot», «automatización», «más leads», «escalar»
        (`output/oferta/2026-10-11-posicionamiento-y-marca.md`, «El vocabulario» y «Resolución con las
        dos investigaciones»); «optimización», «leads» y «funnel», buscadas palabra por palabra en la
        auditoría (línea 109);
      - el nombre del producto o del mecanismo, que no se dice en público hasta probarlo
        (`memory/decisions.md`, entrada «Posicionamiento…»).

      Si una decisión nueva suma o quita palabras, se cambia esta lista en el mismo cambio.
- [ ] **Redacción vieja de decisiones recientes:** buscar en `output/`, `memory/` y `.claude/skills/` la
      formulación anterior de lo último que cambió (palabra clave, umbral, promesa, oferta que se
      anuncia, términos); cada aparición se corrige o se marca «histórico» (`CLAUDE.md`, «Propagar y
      verificar»).
- [ ] **El anuncio promete una sola oferta** (`memory/learnings.md`, entrada «Convertí «anuncio de
      sistemas con un giro» en «un anuncio para dos ofertas»»).

**Salida:** `output/diagnosticos/AAAA-MM-DD-revision-<anuncio>.md`, con cada casilla en sí o no, la
evidencia (archivo y línea, o el conteo) y qué se cambió. A Hans, una línea con el resultado y el enlace.

## Nivel 2 — solo para una oferta nueva o un cambio grande

Cuándo: una oferta nueva; un cambio de promesa, precio o garantía; o el primer anuncio de una oferta que
nunca se pautó. Cuesta horas: lo pide o lo aprueba Hans.

**Cómo se hizo el 2026-10-11** (informe de auditoría, líneas 3–15, 45–66 y 121–127; `memory/proyecto.md`:
15 auditores, 160 hallazgos únicos, panel de 5 jueces):

1. **Auditores por área**, cada hallazgo con archivo y línea. Las áreas del informe: anuncio y hooks; chat
   y entrada; cada oferta; coherencia entre documentos; legal y términos; entrega y capacidad; Meta;
   marca; grabación; la llamada.
2. **Verificadores con tres lentes (método, datos, negocio) que intentan refutar** cada hallazgo. Los de
   severidad alta pasaron por los tres y quedaron solo si sobrevivieron a dos de tres; los de media, solo
   por el lente de datos; los de baja quedaron marcados como no verificados. Donde un verificador
   corrigió la propuesta original, manda la corrección.
3. **Panel de cinco jueces** que puntúan cada pieza y dicen qué sube y qué baja el puntaje: el método del
   curso (Sebastián), el avatar, un media buyer senior, Hormozi y la marca de Hans. Se reporta la
   condición que más se repite.
4. **Un crítico de completitud** que busca lo que nadie miró (sección 8 del informe).
5. **El informe:** veredicto primero; lo que funciona y no se toca; hallazgos por área y severidad, con
   «Bloquea» si frena la grabación; lo descartado tras verificar; y lo que decide Hans marcado
   **[DECIDE HANS]**.

**Lo que salió mal, y cómo se hace la próxima vez:**

- **La consolidación en un solo agente reventó con 318 hallazgos** (dato de la sesión del 2026-10-11; no
  quedó escrito en el informe). Se consolida por área y después se juntan las áreas.
- **El detalle de los jueces quedó fuera del proyecto**, en la carpeta temporal de la sesión (el informe
  remite a `scratchpad/jueces.json`, líneas 65–66). Todo lo que el informe cita queda dentro del proyecto,
  en `output/diagnosticos/`.
- **El informe salió de 1.777 líneas, y Hans se pierde con lo largo** (`memory/learnings.md`, entrada
  «Hans se pierde con mensajes largos»). Para Hans, una página: el veredicto, lo que bloquea y lo que
  decide él. El informe completo queda como anexo para el media buyer.

## Salida de cualquier nivel

Todo va a `output/diagnosticos/`. Lo que decide Hans se le pregunta uno por mensaje; lo que es del media
buyer se corrige en el mismo cambio.
