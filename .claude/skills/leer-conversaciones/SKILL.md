---
name: leer-conversaciones
description: La lectura de las últimas 20 conversaciones de un prospecto o cliente (pieza «el sistema que lee» del Motor de Clientes y, desde el 2026-10-11, también la entrada del anuncio de sistemas a medida, palabra VENTAS): clasificar cada conversación con los criterios del negocio (encaja o curioso), la etapa en que quedó, dónde se perdió y, si se sabe, de qué anuncio vino; entregar una página con los números, los patrones y una frase sobre su anuncio o su chat. Usar como entrada del servicio (a quien califica en el chat, antes de la llamada), como primer reporte semanal de un cliente, y cada semana para alimentar el P&L y la señal a Meta. En la versión 1 la hace el media buyer a mano.
---

# Leer conversaciones

> ⚠️ **Corrección 2026-10-16:** las «respuestas de Josué» del 2026-10-10 que se usan acá las redactó Hans,
> no Josué: no son palabras de cliente. Van marcadas `[SUPUESTO de Hans, no de Josué]`. Lo que Josué dijo de
> verdad está en `output/diagnosticos/2026-10-15-llamada-josue.md`.

**Estado: diseñada el 2026-10-11, sin aplicar.** No viene del curso: es la pieza propia del servicio de
Hans (decisión 2026-10-10, «el diferenciador: un sistema que lee, no uno que habla»). Pasa a «probada»
cuando una lectura se haya entregado a un prospecto real y se sepa si llevó a la llamada. La versión 2
(automatizada, con señal a Meta) se construye con 2–3 clientes pagando.

**Fuente:** `output/oferta/2026-10-10-el-servicio-en-una-pagina.md` (cómo funciona por dentro, pasos 1–4 y
8); `output/oferta/2026-10-11-oso-motor-de-clientes.md` (bloque 8, entrada); decisiones del 2026-10-11 en
`memory/decisions.md`. Método detrás: «dónde falla, qué se arregla» `[CURSO S18 @ 0:55:57]`; pares de
métricas `[CURSO S9]`; palabras del avatar, nunca inventadas (`CLAUDE.md`).

## Para qué

1. **Entrada del servicio:** demostrar el expertise con los datos del propio prospecto, en 24 horas, antes
   de la llamada; y filtrar: `[SUPUESTO]` quien no manda sus conversaciones no era prospecto (nadie lo
   midió; se mide por separado califican → mandan → agendan → llegan: auditoría, hallazgo C04,
   `output/diagnosticos/2026-10-11-auditoria-oferta-y-anuncio.md`, líneas 405–420). Se ofrece
   **adentro del chat, solo a quien pasó la calificación**, nunca anunciada en el video (Hans,
   2026-10-11; si el CTA del copy 3 la anuncia de hecho está pendiente de Hans: `responder-dm-y-agendar`,
   «En este proyecto», punto 3). Hoy es la entrada del anuncio de sistemas a medida (copy 3,
   `output/oferta/2026-10-11-ad-copy-3-sistemas.md`, «Lo que esto mueve…»): la página muestra la fuga en
   plata (paso 5) y la llamada es de sistemas; será también la del Motor cuando se paute.
2. **Reporte semanal:** la lectura de las conversaciones que trajo el anuncio es lo que llena «mensajes
   que encajan», «por anuncio» y «dónde se pierden» del reporte (`skill reporte-semanal`).
3. **Señal a Meta (versión 2):** las etiquetas «calificado» y «compró» son los eventos que se devuelven.

## Entradas

- Las conversaciones: capturas de pantalla, exportación, o acceso de lectura (Instagram por Business
  Suite con el acceso del cliente; WhatsApp con lo que el cliente comparta). **Nunca credenciales en
  archivos ni en el chat.** Si el cliente da acceso, se usa el suyo, no se guarda nada.
- **Datos: PENDIENTE DE HANS:** el texto que se le dice al prospecto sobre qué pasa con sus
  conversaciones, el plazo de borrado y qué herramienta procesa las conversaciones (auditoría, D02,
  `output/diagnosticos/2026-10-11-auditoria-oferta-y-anuncio.md`, líneas 1016–1035, y sección 9,
  punto 10, líneas 1734–1737). La auditoría propone una sola línea en el mismo mensaje que pide las
  capturas, pedir solo capturas o exportación antes del sí (sin acceso de lectura) y tapar nombres y
  teléfonos antes de leer; nada de eso está decidido.
- Los criterios de «encaja», dichos por el cliente (en la entrada: en el chat, una pregunta; en un
  cliente activo: en el diagnóstico). Ejemplo real: «gente que de verdad tenga capital para invertir»
  `[SUPUESTO de Hans, no de Josué]` → se le pide el monto mínimo. **PENDIENTE:** el chat del copy 3
  (`responder-dm-y-agendar`, «En este proyecto») no tiene esa pregunta. Se resuelve cuando se escriban
  los templates y Hans decida cuántas preguntas hace el chat; no se agrega una pregunta sin eso.
- Si se sabe, de qué anuncio o canal vino cada conversación (lo que trae el clic al mensaje, o lo que
  la persona dijo: «vi su anuncio de…»).

## Pasos

1. **Numerar las conversaciones** (1–20) con fecha del primer mensaje y canal (Instagram, WhatsApp).
2. **Por cada una, llenar la ficha** (abajo). Clasificar con los criterios del cliente, no con los
   nuestros; cuando no alcance la información, «no se sabe», nunca adivinar.
3. **Etapa en que quedó:** escribió · le contestaron · calificó · agendó · llegó a la llamada · compró ·
   no compró · sin respuesta nuestra · se enfrió (dijo «después» y nadie volvió).
4. **Dónde se perdió** (una sola causa principal): sin respuesta · respuesta tarde (> 5 min, > 1 h, > 1
   día) · no se le ofreció horario · agendó y no llegó, sin recordatorio · dijo «después» y no hubo
   seguimiento · era curioso (no encajaba) · precio/objeción en la llamada.
5. **Los números de la página:** cuántas encajan y cuántas no; cuántas quedaron en cada etapa; el
   tiempo típico hasta la primera respuesta; cuántas se perdieron por cada causa; si hay anuncio, qué
   anuncio trajo a las que encajan. **Y la fuga en plata (Hans, 2026-10-11):** las que encajaban y se
   perdieron × el ticket que él dijo en el chat = «lo que se le fue en estas 20». Es aritmética con sus
   números, no una promesa; si no dio el ticket, se deja la cuenta sin el monto.
6. **Los patrones, en sus palabras:** qué dicen los que encajan al escribir (las frases textuales), qué
   dicen los curiosos, qué objeciones se repiten. Esto alimenta el siguiente copy.
7. **Una frase sobre su anuncio o su chat:** dónde está la fuga más grande y qué se arregla primero
   (`[CURSO S18]`: no escriben → el anuncio; escriben y no agendan → el chat; agendan y no llegan →
   recordatorios; llegan y no compran → la llamada o la oferta).
8. **Entregar en una página**, con los datos arriba y los patrones abajo, en 24 horas. Sin diagnosticar
   el negocio entero ni recomendar comprar nada: la lectura muestra, la llamada propone.

## La ficha por conversación

> N.º · canal · fecha del primer mensaje · vino de: anuncio X / orgánico / no se sabe · **encaja: sí /
> no / no se sabe** (criterio que cumple o no) · etapa en que quedó · se perdió por: … · minutos hasta la
> primera respuesta · frase textual del prospecto que más dice de él · objeción si la hubo.

## Control de calidad

- [ ] Los criterios de «encaja» son los del cliente, escritos antes de leer.
- [ ] Ninguna cifra inventada; «no se sabe» donde no se sabe.
- [ ] Las frases citadas son textuales; nombres de personas fuera de la página (se usa «el prospecto 7»).
- [ ] La página cabe en una pantalla; los números arriba, los patrones abajo, la frase al final.
- [ ] Se entregó en 24 horas o se avisó antes.
- [ ] Datos de terceros: no se guardan las conversaciones en el proyecto; se guarda la página de lectura
      en `output/clientes/<cliente>/lecturas/AAAA-MM-DD.md` (Hans: `output/oferta/`), sin datos personales.

## Lo que sigue

- Entrada: dos horarios para la llamada; Hans la toma con la página en mano (`script-de-cierre`).
- Cliente activo: los números van al P&L y al reporte (`llevar-el-p-and-l`, `reporte-semanal`); las
  frases, al siguiente copy (`escribir-ad-copy`).
- Versión 2: lo que hoy se hace a mano se vuelve el sistema que lee, clasifica, atribuye y manda a Meta
  `QualifiedLead` y `Purchase` (`output/oferta/2026-10-10-el-servicio-en-una-pagina.md`, «el sistema que
  hay detrás»); consultar al Mentor CRM antes de diseñarlo.
