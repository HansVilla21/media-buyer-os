# Respuesta del Mentor CRM — qué hace hoy Momentum AI CRM del primer mensaje a la llamada (2026-10-10)

**Pedido:** del media buyer, el 2026-10-10, por mensaje a la sesión «Mentor CRM» (la sesión senior del
proyecto Momentum AI CRM), después de que Hans la abriera a pedido del media buyer. Seis preguntas:
flujo del chat, montar un cliente nuevo, para qué rubro, reportes, costo y precio, Instagram.
**Cómo leerlo:** son hechos del código y de la memoria del CRM (`crm-v2 origin/main 98dfc9c`, 7 de
octubre), sin datos de clientes. Las rutas son del repo del CRM. Se cita como
`[MENTOR CRM, 2026-10-10 · ruta]`. Lo que importa para la oferta está en
`output/oferta/2026-10-09-analisis-de-la-oferta.md` (bloques 0 y 6).

**Conclusión del Mentor, en una línea:** del proceso anuncio → mensaje → califica y agenda → llamada,
Momentum hoy cubre **mensaje → califica → pasa a un humano para agendar**, en WhatsApp. No agenda solo,
no recuerda la llamada y no atiende Instagram con el bot.

---

Respuesta del Mentor CRM sobre qué hace hoy Momentum, del primer mensaje de WhatsApp a la llamada agendada: el bot califica y pasa a una persona cuando el lead quiere agendar, pero no agenda solo, no manda recordatorios y no atiende Instagram.

Fuente: crm-v2 origin/main 98dfc9c (7 oct) y su memoria. Sin datos de clientes.

## 1. El flujo del chat
- **Por cada mensaje corren dos procesos** (`src/lib/bot/LEEME.md`, ruta `src/app/api/bot/turn/route.ts`):
  - **el bot conversa** y decide si pasa la conversación a una persona;
  - **un analista** actualiza la ficha: datos, etiquetas, `calificado` sí/no, etapa y nota (`src/lib/bot/analisis.ts`).
- **Califica:** sí, con las preguntas que define el prompt de cada negocio. El analista lo marca en la ficha.
- **Agenda: NO.** No ofrece horarios ni reserva. Cuando el lead quiere agendar, el bot llama a `pasar_a_una_persona` con el motivo `scheduling` ("Quiere agendar") (`src/lib/bot/decision.ts:28`, `herramientas.ts:152`), y una persona coordina.
  - **No hay calendario externo:** no hay Google Calendar en el código. "Agenda" (migración 0078) son citas internas que se cargan a mano. Google Calendar quedó decidido el 07-09 y no está construido (backlog).
- **Recordatorios antes de la llamada: NO.** El "nurturing antes de la llamada" está anotado desde el 28-08 y no se construyó.
  - Lo que sí existe son los **Seguimientos** (`src/app/a/[slug]/seguimientos`): plantillas aprobadas por Meta para el que dejó de contestar, que se cortan si responde, y un "mensaje único" programado.
- **El pase a una persona:**
  - motivos fijos (`calificado`, `quiere agendar`, `objeción compleja`, `bot trabado`, `lo pidió`, `manual`) más reglas propias de cada negocio;
  - avisa al equipo por WhatsApp (necesita una plantilla aprobada en el WABA del cliente y el teléfono del staff cargado);
  - reparte los leads entre el equipo por porcentaje (0137).
- **Configuración, sin programar:** prompt, horario de atención (`src/lib/bot/horario.ts`), reglas de pase, objeciones, catálogo, recursos, estados y etiquetas. **Pero no es autoservicio:** el prompt lo escribe y prueba Momentum desde el panel master (`src/app/a/[slug]/admin`, "Probar bot").

## 2. Montar un cliente nuevo
- **Pasos:**
  1. Alta con preset por rubro.
  2. Cuestionario dentro del producto (8 bloques, con audios y archivos; 0067–0070).
  3. El cliente conecta **su** WhatsApp desde Canales, por Embedded Signup de Meta con **coexistencia**: sigue usando la app WhatsApp Business en el celular y se importan los chats viejos. La app de Momentum está aprobada por Meta desde el 12-09.
  4. Momentum arma y prueba el prompt.
  5. Plantillas aprobadas (aviso de pase y seguimientos) y el teléfono del staff.
  6. Se prende el bot.
- **Lo que pone el cliente:** número de WhatsApp Business, su portafolio de Meta (inicia sesión con Facebook y escanea un QR), las respuestas del cuestionario y, para Instagram, una cuenta profesional ligada a una página de Facebook.
- **Tiempo real: no está medido en la memoria del CRM.**
- **Dónde se atasca** (hechos registrados):
  - entrenar y ajustar el prompt con el cliente: hay bots que pasaron semanas apagados esperando la revisión del dueño;
  - la conexión de coexistencia: un error genérico de Meta resultó ser el QR sin escanear;
  - las plantillas sin aprobar o sin saldo en el proveedor, que deja sin avisos ni seguimientos;
  - un campo obligatorio de más que trabó un alta real (ya arreglado).

## 3. Para qué rubro
**Genérico.** `src/lib/onboarding/presets.ts` trae cuatro presets: **fisioterapia, inmobiliaria (estadías), SaaS/B2B y otra**. Cada uno es un embudo de etapas más los campos que extrae el analista. El catálogo se adapta por rubro. Hoy atiende 11 negocios de rubros distintos (salud, inmobiliario, inversiones, servicios). Lo específico de cada uno vive en su prompt y en su configuración, no en el código.

## 4. Reportes
- **El Resumen** (`src/components/agency/dashboard/dashboard-embudo.tsx`) muestra:
  - leads del período, tasa de conversión, tiempo de respuesta del equipo y sin atender;
  - en qué estado está cada lead (los estados los configura cada negocio), tendencia y por canal;
  - **"Por campaña"**: qué anuncio de clic-a-WhatsApp trae leads que cierran (`src/lib/atribucion/campaign.ts`);
  - exportación a CSV.
- **No hay una etapa fija "llamada realizada"**. Una venta es el estado que el negocio elija; las citas de la Agenda se marcan hechas a mano.
- **De Meta Ads no trae nada:** ni gasto ni impresiones. "Costo por cierre" dice **"Próximamente"** (`dashboard-embudo.tsx:313-321`).
- **Lo que sí hace es MANDARLE a Meta:** eventos de conversión (`LeadSubmitted`, `QualifiedLead`, `Purchase` con monto) según el estado o la etiqueta (`src/lib/meta-eventos/`, migración 0109). Está en producción, prendido en un negocio.

## 5. Costo y precio
- **IA, medido con `gpt-4.1`:** ~US$0,0025 por mensaje con caché y ~US$0,0124 por respuesta en un negocio con ~30 mensajes por día (~US$11/mes). Con Claude Sonnet, medido 2,6× más caro antes de arreglar la caché.
  - El motor guarda el costo de cada turno (`src/lib/bot/costo.ts`), así que el costo por cliente **se puede calcular, pero no está calculado**.
- **WhatsApp:**
  - por YCloud, con su margen y un saldo prepago que ya se vació una vez;
  - por Meta directo, dentro de la ventana de 24 h sin costo por mensaje. Las plantillas fuera de la ventana se cobran.
  - Las tarifas exactas no están registradas.
- **Infra, compartida entre todos los negocios:** Supabase Pro con cómputo Small, y Vercel en plan Hobby (de uso no comercial: es un riesgo anotado).
- **El precio o plan por cliente no está en el código** (no hay facturación). Es comercial y vive fuera del repo: pedíselo a Hans.

## 6. Instagram: qué falta
Fuente: `memory/session-handoff-2026-09-24-ig-messenger.md`.
- **Ya funciona** (en producción desde el 24-09): conectar Instagram y Messenger desde Canales, recibir y **responder a mano desde el inbox**, y el nombre de quien escribe por Instagram.
- **Falta:**
  1. **La revisión de Meta de los permisos de mensajes de Instagram y Messenger.** Sin ella, solo lo usan cuentas de prueba de la app. Hay que grabar un video por permiso. No encontré registrado que se haya mandado después del 24-09.
  2. **Que el bot atienda Meta.** `BOT_ESCUCHA_META = false` en `supabase/functions/meta-webhook/procesar.ts:51`, y aunque se prenda, hoy solo pasaría WhatsApp por Meta al bot: **Instagram y Messenger van a una persona** (`:54`).
  3. **Comentarios y comment-to-DM** (lo que hace ManyChat): no están construidos; necesitan otra revisión de Meta.

**Para tu decisión:** de tu proceso (anuncio → mensaje → califica y agenda → llamada), Momentum hoy cubre **mensaje → califica → pasa a un humano para agendar**, en WhatsApp. No agenda solo, no recuerda la llamada y no atiende Instagram con el bot. Ese es el hueco.

---

# Segunda respuesta del Mentor CRM — qué funciona con el bot apagado (2026-10-10)

**Pedido:** del media buyer, el mismo día, cuando Hans propuso incluir Momentum sin bot en el servicio
(idea que Hans estacionó después). **Lectura del media buyer:** sin bot, Momentum es inbox + CRM
manual + dashboard: la ficha no se llena sola, nadie recibe aviso por WhatsApp, no hay vista
consolidada para quien lleva varios negocios (solo la cuenta master de Momentum) y el reporte al
cliente es un CSV manual. Lo que sí queda: leer los chats, estados, «por campaña» (solo anuncios de
clic a WhatsApp), seguimientos, eventos a Meta cuando el equipo cambia el estado, y el rol `viewer`
en solo lectura. «Resp. del equipo» es un promedio que cuenta 24/7 si el negocio no cargó horario;
«sin atender» son conversaciones sin dueño, no sin respuesta.

Respuesta del Mentor CRM sobre Momentum con el bot apagado: el inbox y los números funcionan, pero el analista que llena la ficha solo no corre.

Fuente: crm-v2 origin/main 98dfc9c (7 oct). Sin datos de clientes.

## 1. Qué sigue funcionando con el bot del negocio APAGADO
- **Inbox y respuestas a mano: sí** (`src/app/a/[slug]/inbox`, `src/lib/inbox/deliver.ts`). Las conversaciones nuevas nacen "Sin asignar", no "Bot" (migración 0064). Con coexistencia, lo que el equipo contesta desde la app del celular también aparece en el CRM.
- **El analista: NO.** `src/lib/bot/analista.ts:8-9`: *"con el bot del negocio apagado no se analiza (paridad con n8n, 2026-09-16)"*.
  - Solo corre si el bot del negocio está prendido, aunque esté pausado para un contacto o la conversación la lleve una persona.
  - **Sin bot, `calificado`, etapa, etiquetas y nota son manuales.**
  - **Un modo "solo analista, sin bot" no existe.**
- **Las notas de voz, fotos y PDF no se transcriben.** Los traduce el turno del bot, y los portones lo cortan antes (`src/lib/bot/lazo.ts:242-254`). En el inbox se ven y se escuchan igual.
- **Estados y Resumen: sí**, con los estados que mueva el equipo (`src/lib/dashboard/funnel.ts`).
- **Seguimientos: sí.** Cron + plantillas de Meta; en el mensaje único se elige "contesta el equipo" (`src/app/a/[slug]/seguimientos`).
- **"Por campaña": sí.** Sale del dato del anuncio que trae el webhook, sin bot (`src/lib/atribucion/campaign.ts`). Solo para anuncios de clic-a-WhatsApp.
- **Eventos a Meta: sí** (0109, `src/lib/meta-eventos/`), pero salen solo cuando el equipo cambia el estado o la etiqueta.
- **Reparto: sí.** La conversación nace con dueño por porcentaje (0138).
- **Avisos:**
  - **en el CRM, sí:** la campana avisa de conversación nueva, asignada y ventana de 24 h por cerrarse (0022/0027);
  - **por WhatsApp al staff, NO:** solo se dispara con un pase del bot. Sin bot, nadie recibe un WhatsApp por un lead nuevo; el equipo tiene que mirar el CRM.

## 2. ¿Alguno corre así hoy?
- **La memoria registra al menos dos casos:**
  - **uno que estuvo días con el bot apagado en agosto:** de ahí salió la 0064, porque las conversaciones decían "Bot" y había leads de noche sin respuesta hasta 6,5 h;
  - **uno que se conectó el 16-09 con el bot apagado a propósito**, hasta entrenarlo.
- **El estado de hoy de los 11 no está en la memoria:** se ve en la configuración de cada negocio.
- **Qué cambia en el día a día:** todo entra "Sin asignar" o al dueño del reparto, nadie recibe WhatsApp, y la ficha no se llena sola.

## 3. Montar un cliente sin bot
- **Queda:**
  1. el alta, con el preset por rubro, que trae las etapas y los campos (`src/lib/onboarding/presets.ts`);
  2. conectar su WhatsApp desde Canales (Embedded Signup con coexistencia);
  3. invitar al equipo;
  4. dejar `bot_enabled = false` **explícito**.
- **Se salta:** el prompt, "Probar bot", el cuestionario (opcional) y la plantilla del aviso de pase.
- **Plantillas solo si** van a usar seguimientos, o escribir fuera de la ventana de 24 h.
- **Lo mínimo para ver chats y números:** pasos 1 a 4.

## 4. Vista de agencia
- **Para el que lleva varios negocios no hay vista consolidada.** Un usuario miembro de varios entra a `src/app/page.tsx`, que **lista sus negocios para elegir uno**, sin métricas juntas.
- **Lo consolidado existe solo para master** (la cuenta de Momentum), y ve **a todos los clientes de la plataforma**:
  - `/master` (`src/app/master/page.tsx`): clientes activos, leads totales y conversaciones de hoy;
  - `/master/clientes`: leads, conversaciones activas, última actividad y estado de la puesta en marcha (RPCs de la 0018).
- **No sirve para un media buyer externo.** Lo que sí existe es el rol **`viewer`** por negocio: ve todo, chats incluidos, en solo lectura, y no recibe avisos (`src/lib/auth/agency-roles.ts`).

## 5. "Resp. del equipo" y "Sin atender"
- **Resp. del equipo** (`src/lib/inbox/response-time.ts`, `funnel.ts:124-175`):
  - **es un PROMEDIO** (no una mediana) de los minutos entre el primer mensaje del lead y la primera respuesta de una persona;
  - descuenta las horas fuera de horario **solo si el negocio cargó su horario**; si no, cuenta 24/7;
  - se ve por el período del Resumen (hoy, 7 d, 30 d o un rango), y por lead en la ficha (Insights: promedio y la respuesta más lenta, `src/lib/contactos/insights-types.ts`).
  - **Cuidado:** una noche de espera sube mucho el promedio.
- **Sin atender** (`funnel.ts:115-116,187`):
  - **son los leads del período cuya conversación sigue `unassigned` (nadie la tomó), no "sin respuesta"**;
  - uno que alguien tomó y nunca contestó ya no cuenta.

## 6. Qué le falta para un media buyer externo
Además de la agenda, los recordatorios y el gasto de Meta:
- una vista consolidada de varios negocios que no sea master;
- un reporte automático al cliente (semanal, por correo o WhatsApp): hoy solo hay **CSV manual** del Resumen;
- un modo "analista sin bot", para que la ficha se llene sola;
- la transcripción de audios sin bot;
- las llamadas como métrica estándar (tomadas, no-show, show rate): hoy **solo existen como estados que arma cada negocio**, y uno ya los usa así.

**Ninguno de estos está en el backlog con fecha.** Lo único con registro es lo que ya te dije:
- el gasto de anuncios: "Costo por cierre: Próximamente", sin fecha;
- el nurturing antes de la llamada: anotado el 28-08;
- Google Calendar: decidido el 07-09, sin construir.
