# Respuesta de `pm` — fases de los sistemas del doctor y del asesor (2026-10-10)

**Pedido:** del media buyer, el 2026-10-10, por el canal de pedidos entre departamentos (solo
lectura). Hans sugirió preguntarle al PM por las fases (2026-10-10).
**Pregunta:** qué incluye cada fase en los dos sistemas, qué es común y qué es custom, si algo toca
leads antes de la venta, con qué herramientas están hechos, y qué dijeron los clientes de sus leads.
**Cómo leerlo:** la memoria de `pm` es una foto (mapa del CEO): lo que dice se verifica con Hans
antes de construir encima. Las rutas citadas son archivos del proyecto `Momentum PM OS`. Lo que
importa para la oferta está en `output/oferta/2026-10-09-analisis-de-la-oferta.md` (bloques 2, 3 y 6).

---
  → pm · D:\Antigravity\0. Proyectos Personales\Momentum PM OS

No uso el cerebro: no tiene nada sobre cómo están armados estos dos sistemas. Todo sale de los archivos de este proyecto (pm).

**Antes de empezar:** la descripción de Hans («fase 1 centralizar datos, automatizar el onboarding y el envío del contrato; fase 2 el camino del cliente por etapas») coincide con el sistema del doctor (AIKUS). Con el del asesor (Josué Miranda) no coincide: el suyo fue un sistema para conseguir clientes, o sea lo que pasa antes del sí. Ya se entregó, y la automatización de contratos quedó fuera a propósito (`clients/josue-miranda/scope.md:39`). El sistema con firma de contratos se hizo para otro cliente que también es asesor de inversiones, Grandir (`clients/dr-carlos-hernandez/CONTEXTO-para-auditoria.md:32`), y ese cliente está cerrado (`memory/tareas-activas.md:121`). Conviene confirmar con Hans a cuál de los dos se refiere.

## 1. Qué incluye cada fase

**AIKUS (doctor):** se está construyendo; la entrega es el 2 de noviembre.
- **Fase 1** (las partes A a L): registrar cada venta, armar el contrato solo y firmarlo desde el celular, el recordatorio de firma, los pagos en cuotas y los saldos, las comisiones por producto y por rol, una cuenta para cada vendedor, las finanzas en dólares y colones, los leads que llegan de Go High Level, un tablero con 7 indicadores, la migración desde Airtable y 2 capacitaciones (`requerimientos-aikus-fase-1.md:95-298`).
- **Fase 2:** las etapas de cada producto después de la venta, los mensajes, las alertas por fecha, los envíos y los referidos. **Fase 3:** un portal para el paciente. Las dos se cotizan aparte (`requerimientos-aikus-fase-1.md:307`).

**Josué:** entregado el 7 de agosto.
- **Lo construido:** una web, 3 landing pages, un CRM (pipeline, ficha de cada lead con análisis de IA, agenda propia, correos masivos, comisiones, metas, tablero), prospección automática en LinkedIn, Instagram vía ManyChat y la lectura de los anuncios de Meta (`outputs/josue-offboarding/OFFBOARDING-josue-final.md:12-62`).
- **Fase 2:** solo se le presentó como posibilidad, nunca se contrató (`outputs/josue-offboarding/fase2-potencial-upsell.md`).

**Lo que tienen en común** y se puede volver estándar:
- El mismo stack y la misma plantilla base de Hans.
- Las comisiones por producto y por rol (AIKUS las toma del CRM de Josué).
- Los usuarios con roles.
- El tablero de indicadores.
- La carga de una base que ya existe (`ARQUITECTURA.md:4,21`).

**Lo específico de cada uno:**
- AIKUS: los contratos por producto con sus complementos, las cuotas en dos monedas con el tipo de cambio y la ficha de tratamiento del paciente.
- Josué: LinkedIn, las landings por producto y las metas de colocación.

## 2. ¿Toca a los leads antes de la venta?

- **AIKUS: no.** Los anuncios, la captación y las llamadas siguen en Go High Level. El sistema solo recibe los leads para medirlos, y «ninguna automatización contesta conversaciones» (`requerimientos-aikus-fase-1.md:32,71,306`). El chatbot quedó fuera por decisión (`CONTEXTO-para-auditoria.md:26`).
- **Josué: sí, pero sin bot.** Capta leads por LinkedIn, Instagram y las landings, y tiene agenda propia. WhatsApp nunca se conectó (`OFFBOARDING-josue-final.md:62`). Responder, calificar con IA y llevar al lead hasta la cita por WhatsApp es justamente lo que se le propuso como Fase 2 (`fase2-potencial-upsell.md:25-28,67-75`).

## 3. Herramientas

- **AIKUS:** Next.js, Supabase (base de datos, usuarios y archivos), Cloudflare Workers, Resend para el correo y WhatsApp por Evolution o por la API de Meta (todavía sin decidir). Los leads y la agenda quedan en Go High Level. El tablero lo arma el propio sistema (`ARQUITECTURA.md:19-37`).
- **Josué:** Supabase, Vercel, Cloudflare (solo el dominio), PROSP para LinkedIn, ManyChat, Google Calendar como motor de la agenda, Fathom, Resend, OpenAI y la conexión con Meta Ads. Para WhatsApp se recomendó YCloud, pero no está activo (`OFFBOARDING-josue-final.md:53-62,72-85`).

## 4. Lo que dijeron sobre sus leads y sus números

- **Cuánto invierten en anuncios:** no quedó registrado para ninguno de los dos.
- **Doctor:** «El Go High Level lo estamos utilizando como una plataforma para tanto la generación de leads, los anuncios y también para el proceso de ventas… ahí es donde ya entonces se está complicando un poquito el asunto porque ahora tenemos que hacer cálculos de comisiones» (`CONTEXTO-para-auditoria.md:52`).
- **Tania, la consultora de procesos de AIKUS:**
  - «Hay números que me trae una persona y números que me trae otra persona y esos números no cierran» (`:67`).
  - «Yo necesito poder calcular los porcentajes de los cierres… cuántos leads están en seguimiento» (`:70`).
  - «yo necesito saber cuándo hacerle un upsell a las personas» (`:77`).
- **Números de AIKUS que no salen de sus palabras:**
  - «~$35.000 al mes», ticket de unos $3.000 y 10 a 12 ventas al mes. El archivo no dice quién dio esa cifra (`CONTEXTO-para-auditoria.md:17`).
  - Según el Airtable que revisó Hans: entre 46 y 123 personas al mes llenan el cuestionario, y en Airtable nadie anota qué pasó con la llamada (`MODULOS-del-sistema.md:145`). El Airtable registra unos 10 a 35 leads al mes (`:34`). Es un piso, porque los leads hoy viven en Go High Level.
- **Josué:**
  - Su meta es «15–20 citas/llamadas calificadas al mes» y su frase fue «poné la maquinita a bretear» (`clients/josue-miranda/scope.md:11`). Son notas de Hans, no una transcripción.
  - Cuántos mensajes recibe y qué le molesta de sus leads no quedó registrado. Lo más cercano: su pipeline tenía 8.022 leads (`memory/tareas-activas.md:100`).

Las tres preguntas que le querías hacer al doctor y a Josué (volumen, qué les molesta, qué probaron) todavía no tienen respuesta. Hans las tenía en el plan de hoy para mandárselas (`outputs/planes/2026-10-10-sabado.md:15-23`).

  ✓ pedido 47db6a66-926a-4af5-a1e6-b2cbae1be4f2

