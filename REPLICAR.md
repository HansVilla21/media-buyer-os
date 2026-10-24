# Replicar el media buyer

> Para la sesión de Claude Code a la que Hans le pasa este repositorio. Se sigue en orden, sin saltar
> pasos. Copia del proyecto original al 2026-10-23.

## Qué trae

El Media Buyer OS completo, igual al original:

- **El método:** `CLAUDE.md` (cómo aprende, las reglas, cómo trabajar con Hans) y las 20 skills de
  `.claude/skills/`, cada una con su estado.
- **El curso** Media Buyers HQ, de Sebastián Gómez: las 10 sesiones procesadas (2–9, 17 y 18; 16 h 44 min
  de video), cada una con su transcripción con minutos, sus recursos en original y en texto, sus apuntes
  y su examen verificado. Índice: `knowledge/curso/indice.md`.
- **El manual:** 15 notas por tema en `knowledge/manual/`. Es lo que se consulta para trabajar.
- **Las referencias:** Hormozi ($100M Offers, Leads, Money Models, GOATed Ads), competencia y políticas
  de Meta, en `knowledge/referencias/` e `inputs/referencias/`.
- **El primer caso, Hans (2026-10-07 a 2026-10-23):** la bitácora en `memory/` y todo lo producido en
  `output/`: la oferta, los diagnósticos, los copies, la campaña 1 con sus números y Josué.
- **La memoria automática** de Claude Code del original, en `replicar/memoria-automatica/`.

Lo que no trae:

| Falta | Por qué | Qué hacer |
|---|---|---|
| Los videos del curso (3 GB) | la materia prima ya es la transcripción | solo para retranscribir: están en la máquina de Hans (`inputs/curso/LEEME.md`) |
| `.venv/` y `.cache/` (6,7 GB) | el entorno y los modelos del transcriptor se reinstalan | paso 6, solo si hay videos nuevos |
| Lo que vive fuera de la carpeta | el cerebro, los otros departamentos, los conectores de la cuenta de Claude | paso 5 |

## 1. Clonar

Con la carpeta nueva abierta y vacía, y `gh` con la cuenta de Hans:

```bash
gh repo clone HansVilla21/media-buyer-os . -- -c core.longpaths=true
```

- **La ruta de la carpeta, corta: menos de 150 caracteres.** La ruta más larga del repositorio tiene 95, y
  Windows no abre rutas de más de 260: con una carpeta más larga, el clon queda incompleto. Pasó en la
  prueba del 2026-10-23, con una carpeta de 190 caracteres. `core.longpaths` deja que git las escriba,
  pero otras herramientas pueden no abrirlas.
- **Después de clonar,** `git status` sale limpio y las cuentas dan: 20 skills, 10 transcripciones, 10
  exámenes y 15 notas del manual. Si no, se para y se le dice a Hans.
- Si la carpeta no está vacía, se clona en una subcarpeta y se le pregunta a Hans antes de mover nada.
- Después se lee `CLAUDE.md` entero: la sesión no lo cargó al abrir, porque la carpeta estaba vacía.

## 2. Una pregunta a Hans: ¿para qué es la réplica?

- **A · El mismo caso, en otra carpeta o en otra máquina.** No se cambia nada. Sigue en el paso 4.
- **B · Otro producto de Hans.** Paso 3.
- **C · El producto de otra persona**, un cliente del servicio de media buying. Paso 3.

En B y C se le pregunta además, de a una cosa: cómo se llama el producto, de quién es y en qué cuenta de
Meta se va a pautar.

## 3. Arrancar con un producto nuevo (B y C)

**Nada se mueve ni se borra.** Las skills citan archivos del caso Hans como ejemplos resueltos (por
ejemplo, `construir-oferta` remite a `output/oferta/2026-10-11-oso-y-gso-sistemas-a-medida.md`). Si se
mueven, esas referencias se rompen.

1. **Las carpetas del producto:** `inputs/clientes/<producto>/` para lo que traiga el dueño (llamadas,
   datos, material) y `output/clientes/<producto>/` para lo que se produzca. La estructura ya está hecha
   para varios clientes.
2. **La memoria:**
   - `memory/tareas-activas.md` se reescribe para el producto nuevo. Primera línea: «El caso Hans quedó
     como antecedente; su estado al 2026-10-23 está en `memory/session-handoff-2026-10-23.md`».
   - `memory/proyecto.md`: arriba, el estado de la réplica. Lo de Hans queda abajo, bajo «Caso Hans
     (2026-10-07 a 2026-10-23)».
   - `memory/decisions.md`: una entrada nueva, «Réplica para <producto>». Lo que manda es `CLAUDE.md`. Las
     decisiones de Hans sobre su oferta son precedentes, no reglas del producto nuevo.
   - `memory/learnings.md` queda como está: todo aplica.
3. **`CLAUDE.md`:** se cambia solo lo que describe el negocio.
   - «Qué es» y el párrafo de «Hoy está»: el producto, su dueño y en qué estado está.
   - **En C**, lo que decide el dueño en «La oferta tiene un solo dueño» (precio, garantía, plazo,
     capacidad, forma de pago) pasa a ser del dueño del producto, a través de Hans. Los OK en Meta siguen
     siendo de Hans, con el permiso del dueño de la cuenta.
   - «Desde cero, de verdad»: el principio queda. War Chest y la prueba de las dos campañas son solo del
     caso Hans.
   - «El cerebro» y «Con los demás departamentos»: en la máquina de Hans quedan, porque las rutas son
     absolutas. En C sirven solo para hechos de Hans (capacidad, qué cobra); los del cliente los da el
     cliente y van a `inputs/clientes/<producto>/`. Fuera de esa máquina se sacan.
   - Todo lo demás no se toca: las reglas, «Reglas que salieron de errores», «Cómo aprende», «Cómo
     trabajar con Hans» y «Cómo trabajamos».
   - Los cambios se escriben en un archivo, a Hans se le pasa una línea con el enlace, y se guardan con
     su OK.
4. **Las skills** quedan con su estado. «En prueba» o «probada» quiere decir con el caso Hans: en el
   producto nuevo, el primer uso es una prueba nueva. Algunas traen datos de la cuenta de Hans como
   ejemplo: en `lanzar-campana-business-manager`, el `page_id`, el `instagram_user_id`, la cuenta en
   colones y el tipo de cambio del BCCR; en `responder-dm-y-agendar` y `grabar-y-revisar-el-ad`, la
   palabra VENTAS y ManyChat. Al usarlas se reemplazan por los del producto nuevo, y la skill se corrige
   recién cuando el uso salga bien, como dice `CLAUDE.md`.
5. **Por dónde se empieza:** por la oferta, antes de cualquier copy. El orden que se siguió con Hans
   (`memory/proyecto.md`): `construir-oferta` → `evaluar-la-oferta` (las 6 preguntas) →
   `diagnostico-de-cliente` (con `elegir-proceso-de-ventas` en la pregunta 17) → `escribir-ad-copy` →
   `revisar-antes-de-grabar` → `grabar-y-revisar-el-ad` → `definir-presupuesto` →
   `lanzar-campana-business-manager` → `leer-los-numeros`.

## 4. La memoria automática

Claude Code guarda su memoria automática por carpeta, así que la réplica arranca sin ella. Se escribe en
la carpeta de memoria de la sesión nueva, con su línea en `MEMORY.md`:

- `replicar/memoria-automatica/feedback-criterio-propio.md`, **siempre**: es cómo quiere Hans que se le
  discuta.
- `replicar/memoria-automatica/project-oferta-definida-2026-10-11.md`, **solo en A**: es el estado del
  caso Hans.

## 5. Lo que vive fuera del repositorio

- **El `CLAUDE.md` global de Hans** (`C:\Users\hvill\.claude\CLAUDE.md`): en su máquina se carga solo.
  Lo que el media buyer necesita de ahí ya está en el `CLAUDE.md` del proyecto.
- **Los conectores de la cuenta de Claude:** Meta (anuncios), Apify (tres cuentas, en el orden del
  `CLAUDE.md` global) y el canal interno (`consultar_proyecto`). Se confirma que la sesión los ve; si
  falta uno, se le dice a Hans. ManyChat no tiene conector: lo maneja Hans.
- **Los guardrails de Meta.** `.claude/settings.json` le prohíbe al media buyer activar, editar, borrar y
  promocionar en Meta, con el nombre exacto de cada herramienta. Ese nombre lleva el identificador del
  conector (`mcp__f3d38e99-c205-4edd-b39a-95559e285e22__…`). **Si en la sesión nueva el conector de Meta
  tiene otro identificador, los guardrails no bloquean nada.** Se comparan los nombres, y si no coinciden
  se le avisa a Hans antes de cualquier otra cosa en Meta: tocar `.claude/settings*` lleva su OK.
- **El cerebro y los departamentos** (`cerebro\` y `CEO\scripts\pedir.mjs`, con las rutas de
  `CLAUDE.md`): solo existen en la máquina de Hans, dentro del Business OS.

## 6. El transcriptor (solo si hay videos nuevos)

Para las sesiones 10–16 o para otro curso.

1. **Requisitos:** Windows con una NVIDIA (probado en una GTX 1660 SUPER de 6 GB), `uv`, y `ffmpeg` y
   `ffprobe` en el PATH. Si falta algo que se instala fuera del proyecto, se le pregunta a Hans antes.
2. **El entorno, dentro del proyecto:**

   ```bash
   uv venv .venv --python 3.13
   uv pip install --python .venv/Scripts/python.exe -r scripts/requirements.txt
   ```

3. **Una sesión**, con los ajustes que caben en 6 GB (`memory/learnings.md`, 2026-10-09):

   ```bash
   .venv/Scripts/python.exe scripts/convert_resources.py "<carpeta de la sesión>" inputs/curso/sesion-NN-tema --session NN
   .venv/Scripts/python.exe scripts/transcribe.py "<video.mp4>" inputs/curso/sesion-NN-tema --model large-v3 --language es --compute-type int8_float16 --batch-size 4
   ```

   La primera vez se baja el modelo a `.cache/models` (unos 3 GB). `scripts/transcribe_queue.sh` hace
   varias seguidas, pero trae escritas adentro la ruta de los videos de Hans y la lista de sesiones.
4. **Después, el ritual de `CLAUDE.md`:** leer entera la transcripción, apuntes, manual, skills,
   autoexamen, reporte corto a Hans e índice.

## 7. Prueba de que quedó igual

Los permisos y las skills se cargan al abrir la sesión, y esta se abrió con la carpeta vacía. Antes de
seguir se escribe como primera línea de `memory/tareas-activas.md`: «Réplica: seguir `REPLICAR.md` desde
el paso 7». Hans abre una sesión nueva en la carpeta, y esa sesión hace la prueba:

1. **Las skills:** aparecen las 20.
2. **Los guardrails:** los nombres de `.claude/settings.json` coinciden con los de las herramientas de
   Meta que ve la sesión. Con el OK de Hans, como en el original el 2026-10-14: un `ads_update_entity`
   sobre un identificador que no existe tiene que salir bloqueado.
3. **El conocimiento:** cinco preguntas al azar de exámenes de sesiones distintas
   (`knowledge/curso/*.examen.md`), contestadas sin mirar la respuesta del examen, solo con el manual y
   los apuntes, con su cita `[CURSO Sx @ h:mm:ss]`. Cada una se verifica contra la transcripción. Si una
   falla, se lee entera esa sesión antes de seguir.
4. **A Hans, una línea:** qué quedó replicado, qué falló y qué falta.

Cuando pasa, se borra la línea de `tareas-activas.md` y se empieza a trabajar.

## Mantener la réplica

- Lo que la réplica aprenda y el original no sepa se le avisa a Hans como candidato para el original.
- El original sube cambios a este repositorio solo cuando Hans lo pide, en una rama con PR.
