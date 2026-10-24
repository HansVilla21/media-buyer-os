# Campaña 1 en el administrador de anuncios, con ManyChat · plan (2026-10-14)

**Decisión de Hans (2026-10-14):** la campaña se arma en el administrador de anuncios, «hacerlo bien todo»,
**sin mensaje automático de Meta**: los mensajes automáticos los controla él desde ManyChat. Reemplaza el
plan de Boost (`memory/decisions.md`). Presupuesto aprobado: $10 al día por 30 días.

## Lo que encontramos antes de armarla

- **Septiembre** (War Chest, `output/pedidos/2026-10-14-estrategia-tecnica-campana-septiembre.md`): la campaña
  se creó por código con objetivo Interacción, destino Instagram Direct, optimización a conversaciones, y el
  mensaje automático quedó **dentro de la plantilla de cada anuncio** (saludo + preguntas frecuentes con
  respuesta automática). Eso es lo que Hans no quiere. Cuenta: `act_1355652845546975` «Hans Villalobos» (en
  colones); página `902554766270020`; Instagram @hansvilla.ai `17841401153096109`.
- **ManyChat** (ayuda oficial, «Instagram Ads Trigger», actualizada 2026-08-27,
  https://help.manychat.com/hc/en-us/articles/14281321942428-Instagram-Ads-Trigger): el anuncio se conecta a
  una automatización de ManyChat desde el administrador de anuncios, en «Plantilla de mensaje → App de
  socio → ManyChat». Solo funciona en campañas creadas en el administrador (no en Boost) con objetivo
  **Tráfico, Interacción o Ventas**, ubicación de conversión Instagram Direct y botón «Enviar mensaje de
  Instagram». El primer mensaje de la automatización no puede llevar variables (nada de [Nombre]) y tiene
  que tener al menos un botón o respuesta rápida.
- **Meta** (ayuda oficial): con objetivo **Clientes potenciales** y destino Instagram, la plantilla es un chat
  automático de Meta con preguntas
  ([crear anuncios de clientes potenciales que abren Messenger o Instagram Direct](https://www.facebook.com/business/help/2398917563501477)).
  Por eso no se usa la receta del curso (Clientes potenciales → Instagram, `[CURSO S7 @ 0:48:41]`): la cambia
  la decisión de Hans de usar ManyChat. Se usa **Interacción**.

## Quién hace qué

### 1. Hans, en ManyChat (antes de publicar)

1. Nueva automatización → disparador **«User clicks an Instagram Ad»** (pestaña Instagram).
2. Primer mensaje, sin variables y con una respuesta rápida (propuesta, en `templates-chat.md`, fase 0).
3. Después de la respuesta rápida, la pregunta 1. De ahí en adelante contesta Hans a mano.
4. Dejar la automatización **en vivo** (si no, no aparece en el administrador).
5. Revisar lo viejo: apagar las automatizaciones por palabra clave de septiembre (CARTERA, SISTEMA, ORDEN,
   SOLO, CRM, AGENTES) y revisar la respuesta por defecto, que le sale a cualquiera que escribe. No prender
   respuestas automáticas en Meta Business Suite: saldrían dos respuestas.

### 2. Media buyer, con el OK 1 de Hans: cargar en borrador

En borrador no se publica nada ni se gasta. Los controles de seguridad (`.claude/settings.json`, desde el
2026-10-14) le impiden al media buyer publicar, activar, editar o borrar en Meta: **publicar lo hace Hans.**

| Nivel | Configuración | De dónde sale |
|---|---|---|
| Campaña | «Campaign 1 – sistemas a medida – video copy 3»; objetivo Interacción; presupuesto de campaña ₡5.000 al día (≈ $10); tope de gasto ₡150.000 | curso (nombres, presupuesto de campaña); ManyChat (objetivo); presupuesto aprobado |
| Conjunto | «Ad set 1 – CR – todos 25-60»; conversión en Instagram Direct, optimizar conversaciones; Costa Rica; 25 a 60 años, todos los géneros, **edad fija** (Advantage+ audiencia apagado: en septiembre la edad quedó como sugerencia y salió de 18 a 65); sin intereses; ubicaciones solo Instagram: feed, historias y reels; fin a los 30 días | curso (un país, sin intereses, pocas ubicaciones); lección de septiembre |

### 3. Hans, en el administrador de anuncios: el anuncio y la publicación (OK 2)

Probado el 2026-10-14. La conexión directa con Meta no sube el video desde la computadora en esta cuenta.
Lo sube desde un link temporal que se borra solo en una hora, como lo hizo War Chest con el OK de Hans
(`RUNBOOK-lanzar-campana-via-mcp.md:116`). Lo que no tiene es elegir la app de socio (ManyChat) en la
plantilla de mensaje: eso es un menú en la pantalla del administrador
([ayuda de Meta](https://www.facebook.com/business/help/2240216809588709)). Reparto: el media buyer sube el
video y deja el anuncio en borrador con texto y botón. Hans entra, elige ManyChat y la automatización en
«Plantilla de mensaje» y publica. Si el borrador hecho por código no deja editar la plantilla en la pantalla
(a War Chest no lo dejó cambiar la imagen, gotcha #5), queda el plan B: anuncio sin mensaje de Meta y
ManyChat responde por la palabra VENTAS.

Hecho por el media buyer el 2026-10-14: anuncio `120250812742640610` con video, portada, texto, botón e
identidad (`campanas.md`). Lo que queda para Hans:

1. Abrir el anuncio en el administrador.
2. Plantilla de mensaje: **App de socio → ManyChat → la automatización** del paso 1. Nada de saludo ni
   preguntas frecuentes de Meta.
3. Revisar la vista previa y **publicar** los tres niveles. Ese clic es el OK 2.

### 4. Media buyer, después

Verificar por lectura que todo quedó como el plan, registrar en `campanas.md`, leer los números cada día con
las reglas de parada aprobadas.
