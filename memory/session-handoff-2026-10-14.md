# Session Handoff — 2026-10-14, noche

> ⚠️ **HANDOFF HISTÓRICO — superado por `session-handoff-2026-10-23.md`**
> Este archivo se conserva como registro del estado al 2026-10-14. Para el estado actual, leer primero el handoff nuevo.

**Propósito:** foto completa del estado del media buyer y de la campaña de Hans al 2026-10-14, 19:50.
Lectura obligatoria al inicio de cualquier sesión nueva, después de `memory/tareas-activas.md`.

**Reemplaza al handoff anterior** (`session-handoff-2026-10-13.md` queda como histórico).

Cargar también:
- `output/clientes/hans/campanas.md`: la campaña, los IDs, el presupuesto y las reglas de parada.
- `output/diagnosticos/2026-10-14-revision-campana-1-contra-curso.md`: qué coincide con el curso y qué no, y
  por qué.
- `output/clientes/hans/templates-chat.md`: el chat.
- `memory/decisions.md`, entradas del 2026-10-14.
- `memory/learnings.md`, entradas del 2026-10-14.

---

## Dónde está el proyecto

**La primera campaña está corriendo desde el 2026-10-14, cerca de las 19:40 de Costa Rica.** Es el paso de
«lanzar» de la entrega del curso: de acá en adelante se opera. Leer números, contestar el chat en menos de 5
minutos, llamadas, P&L y reporte. Al cierre había $0 gastados y 0 mensajes; Meta la tenía «en preparación».

## La campaña

| Nivel | ID | Qué tiene |
|---|---|---|
| Campaña | `120250812122940610` | «Campaign 1 – sistemas a medida – video copy 3»; Interacción; ₡5.000 al día; tope ₡150.000; termina el 2026-11-15 |
| Conjunto | `120250812123670610` | «Ad set 1 – CR – todos 25-60»; conversaciones en Instagram Direct; Costa Rica; 25–60 fijo; todos los géneros; sin intereses; feed, historias y reels de Instagram |
| Anuncio | `120250812742640610` | «Ad 1 – video copy 3 – hook principal»; creativo `2224325601478579`; video `reel-final.mp4` (57,2 s); texto con la palabra VENTAS; botón Enviar mensaje de Instagram; plantilla → ManyChat (lo conectó Hans) |

**Cuenta:** `act_1355652845546975` «Hans Villalobos», en colones y hora de Los Ángeles. El «día» de Meta empieza
a la 1 a. m. de Costa Rica, y a las 2 a. m. desde el 1 de noviembre.

**Decisiones de Hans que se apartan del curso** (todas anotadas, con su razón):
- **Objetivo Interacción en vez de Clientes potenciales:** para que conteste ManyChat. Se optimiza igual, por
  conversaciones.
- **El video va con música:** «Dejémosla así, todo bien. Así me gusta». El riesgo es que Meta lo rechace por
  copyright; en ese caso se publica la versión sin música.
- **Presupuesto de ₡5.000 al día y ₡150.000 de tope:** son unos $11 y $330 al tipo de cambio de venta del BCCR
  del 2026-10-14 (₡454,56). Hans: «Dejalo así».
- **Solo Instagram:** con presupuesto bajo, el curso pide una sola plataforma.

**Reglas de parada** (`campanas.md`). Pausar o cambiar cualquier cosa pide el OK de Hans.
- **2 días sin ningún mensaje:** revisar que el anuncio entregue y que el chat funcione; si todo está bien,
  proponer pausa `[CURSO S18 @ 0:31:25]`.
- **7 días sin mensajes, o costo muy por encima de $1–3 por mensaje:** probar un hook alternativo.
- **$330 gastados sin venta:** pausa y las 6 preguntas.

## El chat

- **Primer mensaje de ManyChat:** «Hola, gracias por escribir. Para ver si esto le sirve, le hago dos
  preguntas rapidas», con la respuesta rápida «Dale». Después va la pregunta 1.
- **Desde la pregunta 2 contesta Hans a mano,** en menos de 5 minutos.
- **Califica** quien vende un servicio de más de $2.000 y está en posición de invertir ahora. Nunca se manda
  el link del calendario: se ofrecen dos horarios.
- **Cada conversación se anota** en `output/clientes/hans/chats.md`.
- **Pendiente de Hans:** revisar los textos y decidir dónde va la lectura de las 20 conversaciones.

## Lo que pasó el 2026-10-14

- **Video:** grabado, editado (v3, «sin marca ni clínica») y aprobado. Destino: Instagram Direct. Presupuesto:
  $10 al día por 30 días.
- **Boost descartado:** Hans pidió armar la campaña en el administrador de anuncios, «hacerlo bien todo», sin
  el mensaje automático de Meta y con ManyChat.
- **Guardrails por código conectados** (`.claude/settings.json`). El media buyer no puede activar, editar ni
  borrar en Meta; publicar es de Hans.
- **El media buyer cargó campaña, conjunto y anuncio.** El video subió desde un link temporal de una hora,
  porque la cuenta no acepta archivos locales.
- **Revisión completa contra el curso,** a pedido de Hans. Encontró la música y la conversión del presupuesto,
  dos errores míos de no medir, y Hans decidió dejar las dos como están.
- **Al publicar:**
  - Hans prendió primero solo la campaña. En la lista de conjuntos, el interruptor azul era el de un conjunto
    viejo de Nexus OS, que sigue prendido pero no gasta porque su campaña está apagada.
  - Meta frenó nuestro conjunto con el error #1870194, un tipo de ubicación que eliminó. Hans volvió a cargar
    Costa Rica.
  - Leído de vuelta: los tres niveles activos y sin errores.
- **Aprendizajes nuevos:** la vuelta por Chrome que no hacía falta, y el presupuesto sin convertir junto con la
  música sin medir. Los dos están en `memory/learnings.md`. La skill `lanzar-campana-business-manager` se
  reescribió entera, a pedido de Hans, con el procedimiento real:
  - quién hace qué y los pasos por la conexión, con sus parámetros;
  - lo que Hans hace en la pantalla;
  - la verificación después de publicar;
  - la tabla de errores conocidos;
  - la lista de chequeo contra el curso, en `checklist-contra-curso.md`.
  Además, `grabar-y-revisar-el-ad` ahora mide la música y el manual (`business-manager.md`) suma «En la
  práctica».

## Lo que sigue, en orden

1. **2026-10-15:** primera lectura de números (skill `leer-los-numeros`). ¿Entrega? ¿Llegan mensajes? ¿Cuánto
   cuesta cada uno?
2. **Guion de la llamada de sistemas a medida** (skill `script-de-cierre`): es lo siguiente del media buyer,
   porque las llamadas pueden llegar en días.
3. **P&L desde el primer gasto** (skill `llevar-el-p-and-l`). El primer reporte semanal, el 2026-10-21.
4. **Josué, jueves 2026-10-15, 4 pm:** el guion sigue en pausa por decisión de Hans.

## Abierto con Hans

- Probar el chat desde otra cuenta cuando le aparezca el anuncio.
- Si los proyectos nuevos de sistemas arrancan después del 2026-11-02, por la capacidad con el doctor. Se
  preguntó dos veces.
- Si el contrato de AIKUS está firmado: `pm` no encontró una copia firmada.
- Confirmar los números del doctor antes de usarlos.
- Apagar las automatizaciones viejas de ManyChat por palabra clave, si siguen prendidas.
- Llevar los paquetes al cerebro y al CEO.

## Sesiones paralelas

- **Contenido:** estudia el curso Personal Brand OS con el método de este proyecto.
- **Mentor CRM:** se consulta al diseñar la versión 2 del sistema que lee.

## Cómo trabajar con Hans

- Una decisión por mensaje, con recomendación y razones. Criterio propio, no yes-man. Corto.
- Las decisiones sobre su plata, su video y su marca son de él, aunque se aparten del curso. Se le dice una vez,
  con el riesgo, y se anota.
- Medir antes de afirmar: tipo de cambio, música, duración.
- Antes de decir «no se puede», mirar cómo lo resolvió otro departamento.
- Nunca mencionarle herramientas internas.

## Última actualización

2026-10-14 19:50, checkpoint pedido por Hans. Próximo: la primera lectura de números, el 2026-10-15.
