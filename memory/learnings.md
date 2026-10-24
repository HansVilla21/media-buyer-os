# Aprendizajes — Media Buyer OS

Errores cometidos y qué se aprendió. Un aprendizaje que no queda escrito se vuelve a pagar.

**Formato:**

```
## AAAA-MM-DD — Título corto
**Qué pasó:** los hechos.
**Causa raíz:** por qué pasó de verdad, no el síntoma.
**Qué hacemos distinto:** la regla nueva.
```

---

## 2026-10-09 — La transcripción secuencial era lenta y repetía frases

**Qué pasó:** la primera prueba con la sesión 2 (large-v3, ventana por ventana, condicionando
cada ventana en la anterior) tardó 4:20 por 5 minutos de audio, perdió la puntuación a mitad de
camino y cayó en un bucle («de la oferta de la oferta de la oferta…»). Además, el lector de audio
de faster-whisper 1.2.1 no funciona con la versión instalada de PyAV.

**Causa raíz:** condicionar en el texto anterior arrastra los errores en grabaciones largas; el
decodificado de una ventana a la vez desaprovecha la GPU; y la incompatibilidad era de versiones.

**Qué hacemos distinto:** `scripts/transcribe.py` carga el WAV directo (sin PyAV), transcribe por
lotes de trozos cortados por voz y sin condicionar en el texto anterior, con el vocabulario del
curso como pista (así «Media Buying» deja de salir como «Miriam Bain»). Con pesos float16 y lotes
de 8, la sesión completa se quedó sin memoria en la GPU (6 GB); con pesos int8 y lotes de 4 cabe
(pico 4,7 GB) y va más rápido: 5 minutos de audio en 0:46, sin bucles y con puntuación. Se lee
cada transcripción antes de estudiarla; si aparece un bucle, se vuelve a transcribir ese tramo.

## 2026-10-09 — La cola de transcripción se saltó cuatro sesiones

**Qué pasó:** la primera corrida de `scripts/transcribe_queue.sh` transcribió las sesiones 3, 5,
8 y 17 y falló en la 4, 7, 9 y 18 con rutas mezcladas («session ion 7»); la 6 ni apareció.

**Causa raíz:** el bucle leía la lista de sesiones por la entrada estándar y los procesos de
adentro (el transcriptor) se comían líneas de esa misma entrada. Error clásico de shell; no de
los videos ni del modelo.

**Qué hacemos distinto:** la lista se lee por un descriptor aparte y cada proceso hijo recibe
`/dev/null` como entrada. La cola es idempotente (salta lo ya hecho), así que se relanzó sin
rehacer nada. Regla: al terminar una cola, contar las carpetas con `transcripcion.json` contra la
lista, no fiarse del «queue finished».

## 2026-10-09 — Hans se pierde con mensajes largos

**Qué pasó:** el reporte de la sesión 2 y la propuesta para definir la oferta salieron largos, con
listas de cuatro pasos. Hans: «me empiezas a dar los pasos así larguísimos y me pierdo».

**Causa raíz:** quise mostrar todo el trabajo y el camino completo en el chat. La regla de
`CLAUDE.md` («corto, una cosa y una pregunta a la vez») ya existía; no la apliqué.

**Qué hacemos distinto:** en el chat, pocas líneas y un solo paso; el siguiente paso solo cuando el
anterior terminó. Los planes, los reportes y el detalle van a archivos (`memory/`, `knowledge/`,
`output/`) y en el chat va una línea con el enlace. Sin listas numeradas de pasos en el chat.

## 2026-10-09 — Un script largo metido por heredoc no llegó al shell

**Qué pasó:** las ediciones de la sesión 17 iban en un script de Python pasado por heredoc dentro
del comando de shell; el shell devolvió «unexpected EOF while looking for matching `'`» en la
línea 1 y no corrió nada.

**Causa raíz:** no confirmada; el comando llegó al shell como una sola línea y la comilla simple
del heredoc quedó sin cerrar. Da igual la causa: un script de muchas líneas con comillas de todo
tipo no es cosa de pasar por un comando.

**Qué hacemos distinto:** los scripts de edición se escriben como archivo en la carpeta temporal
de la sesión y se ejecutan con `python -I ruta`. Cada reemplazo exige exactamente una
coincidencia; si no, el script para antes de tocar nada. Funcionó a la primera.

## 2026-10-09 — Un recurso en Markdown pesaba 988 KB y reventó la salida

**Qué pasó:** al imprimir los recursos de la sesión 18 de una vez, la salida fue de 1 MB: el
archivo `MB Service - Ad Copy 1.md` (232 líneas, 1.568 palabras) trae imágenes incrustadas en
base64. El conversor lo copió tal cual porque ya era Markdown.

**Causa raíz:** se asumió que «pocas líneas» era «poco peso», sin mirar el tamaño.

**Qué hacemos distinto:** antes de imprimir un recurso, `wc -c`; lo que pase de 100 KB se lee con
las líneas recortadas (`cut -c1-500`) o por tramos. Al convertir un `.md` del curso, el
conversor debería separar las imágenes incrustadas a archivos aparte (pendiente en
`scripts/convert_resources.py`).

## 2026-10-09 — Usé el contenido viejo del OSO cuando Hans quería solo el método

**Qué pasó:** Hans pidió revisar «eso del OSO». Lo leí entero y usé lo que estaba escrito ahí
—ofertas de 2024–2025, dolores, lista de conocidos— como hipótesis en el análisis de la oferta y
hasta como «hallazgo» en el chat. Hans: «esos son documentos viejos, viejos, viejos… no hay que
tomar en cuenta para nada. Es nada más la estructura».

**Causa raíz:** la regla de `CLAUDE.md` («lo existente se revisa solo cuando Hans lo pida») la leí
como permiso para usar el contenido. Hans señalaba el método. No pregunté qué quería de ese
documento antes de usarlo, y la regla «lo que no está claro se pregunta» aplicaba.

**Qué hacemos distinto:** cuando Hans señale un documento existente, primero se le pregunta si
quiere el método o el contenido; por defecto se toma solo el método. Lo que ya se escribió con
contenido viejo se borra en el mismo cambio, no se deja «marcado» como hipótesis.

## 2026-10-10 — Propuse un nicho con un solo dato

**Qué pasó:** con un cliente (un doctor que pagó más y sin pelea) propuse «médicos» como nicho, dos
veces. Hans rebatió: ese doctor ya lo conocía, es atípico (un servicio muy específico) y la mayoría
de los médicos en Costa Rica venden consultas de bajo ticket; «no tenemos evidencia para definir un
solo avatar». El curso dice lo mismo: doctores son «otro mundo» del foco del programa (sesión 3) y
el avatar del servicio se define por modelo de venta, no por industria (sesiones 2, 3, 18).

**Causa raíz:** apliqué la regla del 20 % de Hormozi sobre una muestra de uno, y confundí la
industria del cliente con lo que lo hace buen cliente (vende alto valor por conversación).

**Qué hacemos distinto:** con menos de cinco clientes, el nicho se define por modelo de negocio
(qué vende, a qué precio, cómo cierra) y la industria la decide el ad. Antes de proponer un nicho,
verificar que el dato que lo sostiene no sea un caso único y que el curso no lo marque como «otro
mundo».

## 2026-10-10 — El primer copy sonaba a un media buyer cualquiera, no a Hans

**Qué pasó:** escribí el copy 1.0 con la estructura del curso y la línea de credibilidad que Hans
eligió («construyo sistemas con IA para negocios reales»), pero sin conectarla con el servicio: la
IA quedaba como un dato suelto y el resto del video era puro ads. Hans lo vio de inmediato: su marca
es 100 % IA y el video «se iba por otro lado»; además no quiso nombrar un método que todavía no existe
al 100 %.

**Qué aprendí:** la congruencia con la marca de quien habla es un criterio de calidad del copy, igual
que el hook o el CTA, y hay que revisarla antes de entregar: ¿esta persona diría esto de sí misma, y
su audiencia lo reconocería? El puente entre lo que la persona es y lo que vende va en el bloque de
autoridad. Y un nombre de mecanismo solo se dice en cámara si quien lo dice se lo cree; si no, se
describe el mecanismo y el nombre espera.

**Cómo se aplica:** control de calidad del copy suma dos casillas: «congruente con la marca de quien
habla» y «todo lo que promete existe hoy o se dice como promesa, no como hecho». Skill
`escribir-ad-copy`, paso 5.

## 2026-10-11 — Le atribuí a Hans una lista de 24 conocidos que nunca tuvo

**Qué pasó:** la metodología del OSO trae el paso «las primeras 24 personas conocidas que encajan». Lo
puse en el plan del fin de semana y en el OSO como tarea de Hans («arma la lista»), y lo repetí varias
veces como si fuera un hecho suyo. Hans: «eso de la lista no sé de dónde lo haya sacado, pero en
realidad no tengo una lista».

**Qué aprendí:** un paso del método no es un dato del cliente. Antes de convertir un paso en tarea,
preguntar si existe la materia prima («¿tenés gente conocida que encaje?»), igual que se verifica un
número de memoria. Y decir siempre de dónde sale cada paso que se propone.

**Cómo se aplica:** en los planes, cada tarea que depende de algo que Hans tiene que tener (lista,
material, acceso, plata) se formula primero como pregunta. Bloque 9 del OSO ajustado a lo que sí hay.

## 2026-10-11 — Usé la oferta de septiembre del cerebro como base para cerrar los términos de sistemas

**Qué pasó:** para evaluar «pautar sistemas a medida» con las 6 preguntas, leí en el cerebro la nota de
la oferta de septiembre (de War Chest, que Hans no aprobó) y tomé sus términos —60/40, garantía de uso,
cuota anual de $1.200, precio único— como el punto de partida para «cerrar lo abierto». Hans: «esa
oferta está malísima… no la tomemos… el precio no puede estar definido cuando es un sistema custom».

**Qué aprendí:** del cerebro se toman hechos (qué cobró, qué entregó, qué dijo Hans), no las ofertas ni
los análisis de otros departamentos, aunque estén guardados como notas con afirmaciones. Una propuesta
que Hans no aprobó no es un término abierto: no existe. Y en una oferta custom el precio no se fija; se
dice cómo se cotiza.

**Cómo se aplica:** antes de usar una nota del cerebro sobre oferta, nicho o avatar, revisar el campo
«autor» y si Hans la aprobó; si es de War Chest u otro proyecto, solo se extraen los hechos con fuente
propia de Hans. Las decisiones de hoy (50/50 a la entrega aceptada; 4–6 semanas desde los insumos;
frase del mecanismo; sin agentes) siguen válidas porque las tomó Hans sobre opciones del método.


## 2026-10-11 — Declaré «~245 palabras ≈ 90 s» sin contar: el copy 2.2 tenía 378

**Qué pasó:** el copy 2.2 se aprobó y se mandó a grabar con la nota «~245 palabras ≈ 88–92 s». La
auditoría de la noche contó 378 palabras (verificado con herramienta): unos 135 s. Más de 90 s Instagram
lo sube como post y se pierde el Boost. Hans habría grabado un video inservible.

**Qué aprendí:** un número que decide si el entregable sirve (duración, palabras, costo) se mide, no se
estima. Y una versión que crece por correcciones (2.0 → 2.1 → 2.2 sumó frases en tres rondas) se vuelve
a contar en cada ronda.

**Cómo se aplica:** la skill `escribir-ad-copy` exige contar con herramienta antes de declarar la
duración; la propuesta 2.3 trae el conteo por bloque y el orden de cortes si el cronómetro de Hans se pasa.

## 2026-10-11 — El copy aprobado al mediodía no se revisó contra la decisión de la tarde

**Qué pasó:** a las 12 Hans aprobó la 2.2 con el RESULTADO «que ningún cliente se le pierda entre el
mensaje y el pago». En la tarde él mismo bajó esa frase a «el cómo se ve» («no hay mucho dolor ahí») y
la promesa de sistemas pasó a «más ventas con los mismos mensajes». Escribí en la decisión «el copy 2.2
no cambia» sin releerlo: el hook era compatible, pero el bloque RESULTADO y el de DESEOS seguían
vendiendo la frase descartada. Diez auditores lo marcaron.

**Qué aprendí:** cuando cambia la promesa, se relee cada pieza que la repite (copy, chat, guion, paquetes,
handoff) bloque por bloque, no por recuerdo. «No cambia» es una afirmación que hay que verificar.

**Cómo se aplica:** en cada decisión que toque promesa, precio, garantía o entrada, la Consecuencia lista
los archivos releídos y qué se cambió en cada uno; la auditoría dejó la lista (hallazgos K) para hacerlo.

## 2026-10-11 — Convertí «anuncio de sistemas con un giro» en «un anuncio para dos ofertas»

**Qué pasó:** Hans propuso pautar sistemas a medida con un giro hacia «más clientes» y, con uno o dos
proyectos, apagar y pasar al Motor. Yo lo leí como una oportunidad de servir a las dos ofertas con un solo
video y lo propuse así; él aceptó pensando en que alguno podía terminar en el Motor. Tres versiones de copy
después, el mecanismo había quedado en el mínimo común de las dos y no sonaba a servicio. Hans: «¿por qué
estamos mezclando las dos ofertas si habíamos quedado…?».

**Qué aprendí:** cuando el cliente pide una cosa con un matiz («sistemas, con un giro»), el matiz es un
ajuste de la promesa, no una segunda oferta en el mismo anuncio. «Una oferta, un tema» `[CURSO S5]` aplica
también a las ideas del propio media buyer.

**Cómo se aplica:** antes de ampliar el alcance de un pedido de Hans, repetirle en una línea lo que pidió y
lo que se propone sumar, y que elija.

## 2026-10-11 — No ejercí el contrapeso del curso: dos días y medio en la oferta y ningún anuncio

**Qué pasó:** el plan del fin de semana (2026-10-10) ponía el Boost el domingo o el lunes y decía «el primer
ad es un test». Hans había dicho «necesitamos generar dinero urgentemente». Terminamos el 2026-10-11 en la
noche con 29 decisiones, unas diez versiones de copy, una auditoría, y el anuncio sin grabar: paso 5 de 12
de la entrega del curso, $0 invertidos, 0 datos. Parte del retraso vino de giros pedidos por Hans
(investigación, sistemas en vez del Motor, auditoría), pero el curso dice que el media buyer «pone su
sistema» `[CURSO S17 @ 0:33:15]`, que se valida con un solo video `[CURSO S5 @ 0:40:30]` y que todo va ASAP
`[CURSO S17 @ 1:07:07]`. Nunca le dije a Hans lo que cada giro costaba en días. Y el tramo que no dependía de
él (templates, presupuesto, P&L, instrucciones de grabación) no lo avancé en paralelo.

**Qué aprendí:** definir la oferta no es lanzar. Cada vez que algo nuevo atrasa el primer anuncio, se le
dice a Hans cuánto lo atrasa, y él elige. Lo que es del media buyer se hace en paralelo mientras Hans decide.

**Cómo se aplica:** en cada pedido que no sea del camino al Boost, una línea: «esto atrasa el anuncio X días;
¿lo hacemos ahora o después del primer dato?». `tareas-activas.md` separa lo que es de Hans de lo que es
mío.

## 2026-10-11 — Comillas que no eran textuales y citas del curso imprecisas

**Qué pasó:** la auditoría encontró una cita de Josué en el copy que empalmaba dos frases suyas, dolores sin
fuente dichos como palabras del avatar, «48 horas» citado a la página equivocada, y una frase atribuida al
curso que el recurso no dice («ahorrar tiempo y ordenar no lo busca nadie»; el recurso solo habla de
«optimización de embudos»).

**Qué aprendí:** «no se inventan palabras de clientes» no alcanza: también se inventan por condensar. Entre
comillas va solo lo textual; una cita al curso se confirma en la transcripción o el recurso.

**Cómo se aplica:** regla nueva en `CLAUDE.md`; casilla nueva en el control de calidad de `escribir-ad-copy`.

## 2026-10-11 — Términos «decididos» que no aguantaban las preguntas de un cliente

**Qué pasó:** el Motor tenía precio, garantía y trato de prueba decididos desde el 2026-10-10, pero nadie
había escrito el IVA, sobre qué se calcula el 10 %, qué pasa si el primer mes falla, desde cuándo corren
los 30 días ni cuál es el documento de arranque. Hubo que tomar siete decisiones más la noche del 2026-10-11.

**Qué aprendí:** una oferta está cerrada cuando contesta los casos borde que un cliente pregunta antes de
pagar, no cuando tiene precio y garantía.

**Cómo se aplica:** la lista de casos borde quedó en la skill `construir-oferta` (paso de cerrar términos).

## 2026-10-11 — «Anuncios que corrían desde abril» eran anuncios creados en abril

**Qué pasó:** al mapear a Felipe Carvajal le dije a Hans que siete anuncios «corrían desde abril» por su
fecha de creación; estaban inactivos y habían corrido tres días. Hasta hoy estaba anotado solo en la skill
`mapear-competidor`.

**Qué aprendí:** creado no es activo; el estado se verifica antes de decir que algo funciona. Es el mismo
patrón que contar palabras: medir antes de afirmar.

## 2026-10-11 — Un acento grave en un `python -c` ejecutó un archivo como comando

**Qué pasó:** al registrar una decisión con `python -c "…"` dentro del shell, el texto llevaba una ruta entre
acentos graves (`` `output/oferta/…md` ``). El shell los tomó como sustitución de comando: intentó ejecutar el
archivo Markdown (falló en la línea 3, sin daño) y dejó la ruta vacía en `memory/decisions.md`. Se corrigió.

**Qué aprendí:** dentro de comillas dobles del shell, los acentos graves se ejecutan.

**Cómo se aplica:** los scripts de edición van en un heredoc con delimitador entre comillas
(`python -I - <<'PY'`) o en un archivo de la carpeta temporal; nunca en `python -c "…"` con texto Markdown.

## 2026-10-13 — El actor de reels de Apify no devuelve anuncios, y el saldo es uno solo para todos

**Qué pasó:** Hans pasó un video de Cristina Cali para transcribir. `apify/instagram-reel-scraper` devolvió
«vacío o privado» dos veces: era un anuncio (`productType: ad`), no un reel. `apify/instagram-scraper` con
`directUrls` sí trajo los datos, y `steadyfetch/instagram-reel-transcript-scraper` la transcripción (unos 2
centavos, sin bajar el video). En el medio, el saldo del ciclo de Apify se agotó: la conexión es a nivel
usuario y todos los proyectos gastan de la misma cuenta.

**Qué aprendí:** antes de transcribir, mirar el tipo de publicación; y no dar por hecho que hay saldo.

**Cómo se aplica:** quedó en la skill `mapear-competidor`; y la regla de las dos cuentas de Apify, en el
`CLAUDE.md` global.

## 2026-10-14 — Le mandé a Hans una vuelta por Chrome que no hacía falta

**Qué pasó:** la subida del video desde la computadora falló, y le propuse a Hans entrar desde su Chrome a armar
el anuncio. La respuesta de War Chest que yo mismo había pedido ese día ya decía cómo se resolvía: subir desde un
link temporal. Hans: «¿por qué tienes que entrar al Chrome? … para algo tenemos la conexión».

**Causa raíz:** contesté con el primer error en la mano, sin releer lo que ya tenía sobre ese mismo paso.

**Qué hacemos distinto:** antes de decir «no se puede» o de proponer un camino más largo, se busca cómo lo
resolvió otro departamento o una corrida anterior (respuestas en `output/pedidos/`, runbooks), y se separa lo
que de verdad no se puede (elegir ManyChat en el anuncio) de lo que solo falló de una manera (subir el video).

## 2026-10-14 — Cargué ₡5.000 «≈ $10» sin medir el tipo de cambio, y el video final se subió con música

**Qué pasó:** en la revisión contra el curso que pidió Hans antes de publicar salieron dos fallas mías.
- El presupuesto de la campaña quedó en ₡5.000 al día y ₡150.000 de tope, copiados de septiembre. Con el tipo de
  cambio del BCCR del día (₡454,56) eso da $11 al día y $330 en total, cuando Hans aprobó $10 y $300.
- El video final tiene música de fondo, medido en el audio. La revisión del video había dejado «confirmar sin
  música» como pendiente, y el pendiente no se cerró antes de subirlo.

**Causa raíz:** dos reglas que ya existían no se aplicaron en el paso de cargar. Una es medir antes de afirmar:
un monto en otra moneda es un número que decide. La otra es cerrar los pendientes de una revisión antes del
paso siguiente.

**Qué hacemos distinto:** antes de cargar plata en Meta, el monto se convierte con el tipo de cambio del día y
la fuente queda anotada en `campanas.md`. Antes de subir un creativo, se releen los pendientes de su revisión, y
lo que se pueda medir (música, duración, peso) se mide.

## 2026-10-16 — Usé como palabras de cliente unas respuestas que había redactado Hans

**Qué pasó:**
- **Lo que llegó:** el 2026-10-10 Hans pegó en el chat las respuestas de Josué a las tres preguntas, y se guardaron
  y citaron como `[AVATAR · Josué]`.
- **Hasta dónde llegaron:** sostuvieron la garantía, el «prospecto», el dolor del Motor, una línea del copy 3 y el
  guion. Se usaron en 20 archivos.
- **La corrección:** el 2026-10-16 Hans aclaró que las había redactado él.
- **Otra falla en la misma revisión:** una cita del curso, «es un dolor enorme» `[S6 @ 1:41:47]`, no era textual.
  Lo que dice el curso es «un dolor demasiado grande», en 1:42:05.

**Causa raíz:** un texto pegado en primera persona se tomó como transcripción, sin preguntar de dónde salía.
Además, nadie sospechó de unas respuestas demasiado ordenadas, que ya traían cifras y frases listas para un copy.

**Qué hacemos distinto:**
- **Palabras de cliente pegadas en el chat:** antes de guardarlas como `[AVATAR]`, una pregunta: «¿esto lo dijo él
  textual, o lo escribiste vos con lo que sabés de él?». Lo que no venga de una grabación, un chat o un mensaje
  del cliente va como `[SUPUESTO de Hans]`.
- **Fuentes de cliente:** se prefieren las grabaciones y transcripciones, como la de Fathom.
- **Citas del curso:** cada cita entre comillas se confirma contra el minuto, como ya pide `CLAUDE.md`.

## 2026-10-23 — Propuse cobrar un % de lo que gana Josué sin mirar de qué gana

**Qué pasó:** con Hans se cerró «10 % de lo que Josué gana con cada cliente del anuncio». La auditoría de cinco
revisores mostró lo que el media buyer tenía delante en la transcripción: hoy Josué gana con copy trading apalancado
x24 por un «IB Trading» (53:19, 56:00, 1:03:44). Ese producto, Meta casi seguro no lo deja anunciar, y cobrar sobre
él puede ser intermediación sin licencia `[INCIERTO]`. La votación dio riesgo 2/10 y broker 3/10.

**Causa raíz:** el cobro se armó copiando la regla del Motor, que es un porcentaje de lo que el cliente cobra. No se
preguntó qué produce ese ingreso. En un cliente de inversiones, la base del porcentaje es parte del riesgo legal.

**Qué hacemos distinto:**
- Antes de proponer un cobro variable, se pregunta de qué productos sale el ingreso, quién los regula y si se puede
  compartir.
- Con clientes financieros, ningún porcentaje se cierra sin esa respuesta y sin abogado.
- La auditoría por miradas se hace antes de que Hans apruebe una página, no después.

## 2026-10-23 — El primer clon de prueba del repositorio quedó incompleto

**Qué pasó:** al probar el repositorio de GitHub con un clon limpio en una carpeta temporal, git falló a mitad
de camino: llegaron las 20 skills y solo 5 de las 10 transcripciones, y ningún examen ni nota del manual.

**Causa raíz:** la carpeta tenía 190 caracteres y la ruta más larga del repositorio tiene 95. Windows no abre
rutas de más de 260. El original no lo sufre porque su carpeta tiene 85.

**Qué hacemos distinto:** `REPLICAR.md` pide una carpeta de menos de 150 caracteres, clona con
`core.longpaths=true` y, después de clonar, cuenta skills, transcripciones, exámenes y notas antes de seguir.
Un clon se da por bueno recién cuando las cuentas dan.

