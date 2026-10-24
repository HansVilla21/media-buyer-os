---
name: responder-dm-y-agendar
description: Llevar a un prospecto que escribe desde el anuncio hasta una llamada agendada (Media Buyers HQ, sesión 5, Blueprint de Mensajes): las siete fases del chat, las reglas de oro, las objeciones por chat y la personalización de los templates con el ad copy de la oferta. Usar cuando se va a activar un ad con CTA a mensaje —para preparar los templates personalizados de Hans o de un cliente— y cuando llega un mensaje y hay que responderlo.
---

# Del DM a la llamada agendada

**Estado: del curso, sin aplicar** (sesión 5, 2026-10-09).

**Fuente:** `inputs/curso/recursos/Blueprint-de-Mensajes-DM-a-Llamada.pdf.md` (texto completo de
los templates) y `knowledge/curso/05-fusion-funnels.md`. Manual: `knowledge/manual/chat-y-llamada.md`.

## Antes de activar un ad a mensaje

1. **Personalizar los templates** con el ad copy de la oferta, para que el chat sea «la
   continuación natural» del anuncio `[CURSO S5 · DM, p. 14]`. Prompt del curso (adjuntando el
   Blueprint y pegando el ad copy):
   > Adjunto el Blueprint de Mensajes para responderle a prospectos que escriben desde anuncios.
   > Quiero que crees todos los templates de este blueprint, siguiendo exactamente las mismas
   > fases y la misma estructura, pero personalizados para mi nicho y mi oferta, con base en el
   > ad copy de mi anuncio. MI CONTEXTO: mi nicho: […]; mi oferta: […]; rango de inversión: […];
   > duración y plataforma de la llamada: […]; mi país y el de mis prospectos: […]. AD COPY DE MI
   > ANUNCIO: […]. REGLAS: usa las mismas palabras, problemas y promesas del ad copy; solo 2
   > preguntas de calificación, específicas para mi nicho (situación y problema; compromiso de
   > inversión); mensajes cortos de 1 a 3 líneas, una pregunta por mensaje, trato de usted; nunca
   > mandes link de calendario: ofrece siempre 2 horarios específicos y pide nombre, país y
   > correo; adapta la confirmación, los recordatorios y los seguimientos a mi oferta; agrega las
   > 3 a 5 objeciones más comunes de mi nicho con su respuesta; entrega todo listo para copiar y
   > pegar, organizado por fase.
   Acá, ese trabajo lo hace el media buyer con el diagnóstico y el copy a mano; el resultado va a
   `output/clientes/<cliente>/templates-chat.md`, y Hans o el cliente lo revisa para que suene a
   él.
2. **Acordar quién responde y en cuánto tiempo** (menos de 5 minutos), con qué calendario se
   agenda y el rango de precio que se puede decir por chat.

## Cuando llega un mensaje: las siete fases `[CURSO S5 · DM, pp. 2–12]`

1. **Primer mensaje**, en menos de 5 minutos: gracias por escribir + pregunta 1 de calificación.
   Si pregunta el precio: el rango, y la pregunta 1.
2. **Calificación**, una pregunta por mensaje: (1) situación actual con [tema] y qué lo ha frenado
   para [resultado]; validar y reflejar con sus palabras; (2) si está en posición de invertir ahora
   o lo ve para más adelante. No califica → paso previo y puerta abierta.
3. **Invitación:** «el siguiente paso es una llamada corta de [30] minutos por [Meet/Zoom] para
   ver su situación a fondo y ver si somos un buen fit. ¿Le queda mejor mañana a las [3pm] o el
   [día] a las [10am]?» Siempre dos opciones.
4. **Agendar uno mismo:** apartar el espacio; preguntar el país; pedir nombre completo y correo;
   crear el evento (título «Llamada [Nombre] x [Su nombre]», invitado, link, una línea de
   descripción); enviar. Nunca mandar el link del calendario.
5. **Confirmación** inmediata: llegó la invitación a [correo]; día, hora y país; «acepte la
   invitación»; «si algo cambia me avisa y lo movemos». Opcional: video corto o «piense en su
   meta».
6. **Recordatorios:** noche anterior («¿sigue en pie?»), mañana del día (con link), 1 hora antes.
7. **Seguimientos:** no llegó → 3–5 min («ya estoy conectado»), 15 min (dos horarios nuevos), día
   siguiente, 3 días (último). Dejó de responder → día siguiente, 3 días (con un resultado de
   cliente), 7 días (último: «asumo que ya no es prioridad»).

## Objeciones por chat `[CURSO S5 · DM, p. 13]`

«Mándeme la información» → cada caso es diferente; en la llamada sale con un plan; dos horarios.
«No tengo tiempo» → 30 minutos, mañana temprano o noche. «Lo voy a pensar» → ¿qué le gustaría
pensar? «¿Es estafa?» → pregunta válida; por eso la llamada; link a resultados. «¿Cuánto cuesta?»
→ rango; en la llamada lo exacto; dos horarios.

## Reglas que no se rompen

- Menos de 5 minutos; una pregunta por mensaje; 1–3 líneas; sin link de calendario; no se vende
  por chat; confirmar el país; trato de usted (salvo que el diagnóstico diga otro).
- No se inventan resultados ni clientes para contestar «¿es estafa?» o «¿cuántos clientes ha
  tenido?»: solo lo que existe.
- Cada conversación queda registrada (fecha, de qué ad, en qué fase quedó, resultado): es la
  materia prima para medir mensajes → llamadas → ventas.

## Registro

`output/clientes/<cliente>/chats.md`: una línea por prospecto: fecha · ad · fase alcanzada ·
llamada agendada (sí/no, fecha) · resultado · notas con sus palabras (sirven para el copy y para
el script).

## En este proyecto: el chat del copy 3, solo sistemas a medida (decisión de Hans, 2026-10-11)

El anuncio aprobado (`output/oferta/2026-10-11-ad-copy-3-sistemas.md`) es **solo de sistemas a medida**,
pide un mensaje con la palabra **VENTAS** y cierra con «lo vemos en dos preguntas»
(`memory/decisions.md`, entradas «El anuncio es solo de sistemas a medida; el Motor se pauta después» y
«Copy 3 (solo sistemas) aprobado, palabra clave VENTAS»). El chat del anuncio 2 (palabra LLAMADAS, dos
ofertas) queda como historia. El chat sigue el Blueprint con estos cambios:

1. **La calificación, para sistemas:** las dos preguntas del Blueprint (fase 2 de arriba), una por
   mensaje, 1–3 líneas, de usted, con las palabras del video.
   - **Situación y problema.** Tiene que sacar qué vende y a cuánto (lo necesitan el filtro de precio y
     la fuga en plata de la lectura, `leer-conversaciones` paso 5) y qué pasa hoy con los que le
     escriben, dicho con sus palabras. Para el problema, la auditoría propuso: «¿Cuántas personas le
     escriben al mes preguntando por su servicio, y qué es lo que más le ha frenado para que terminen
     comprando?» (C01, `output/diagnosticos/2026-10-11-auditoria-oferta-y-anuncio.md`, líneas 382–386).
   - **Compromiso** (la pregunta 2 del bloque genérico, que el chat del anuncio 2 había perdido): si
     está en posición de invertir en resolver esto ahora o lo ve para más adelante. Va después de
     reflejar su situación y antes de ofrecer la lectura; con un «más adelante» claro, la respuesta del
     Blueprint, sin lectura (C02, líneas 391–403).
   - La pregunta de quién contesta los mensajes pasa a la llamada (C01, línea 386). El texto exacto
     va en los templates (`memory/tareas-activas.md`, paso 2).
2. **Umbral y cantidad de preguntas: DECIDIDO por Hans el 2026-10-11, noche («dos preguntas y
   $2.000»).** El chat hace exactamente dos preguntas (situación y problema; compromiso), porque el CTA
   promete dos, y califica desde los mismos $2.000 del video. A quien vende por debajo, una respuesta
   corta y amable, sin lectura, anotada como fuera de criterio (K05, opción A, líneas 768–771).
3. **Solo a quien califica se le ofrece la lectura** de sus últimas 20 conversaciones (skill
   `leer-conversaciones`), adentro del chat; el video no la anuncia (`memory/decisions.md`, entrada
   «Ajustes al anuncio único…»). El CTA del copy 3 se cambió el 2026-10-11 (noche) para que no la
   anuncie: «Si esto le está pasando, mándeme un mensaje con la palabra VENTAS y vemos en dos preguntas si
   le sirve» (Hans: «cambialo, que no anuncie la lectura»). `[SUPUESTO]` quien no
   manda sus conversaciones no era prospecto: nadie lo midió (C04, líneas 405–420). Qué se le dice sobre
   sus conversaciones está pendiente de Hans (`leer-conversaciones`, «Datos»). Quien no califica recibe
   una respuesta amable y corta, sin lectura.
4. **Dos horarios, invitación de calendario, nunca link.** La llamada la toma Hans con la lectura en
   mano y **es de sistemas**: si lo que el prospecto necesita es gente, Hans lo anota para cuando se paute
   el Motor (`output/oferta/2026-10-11-ad-copy-3-sistemas.md`, «Lo que esto mueve después de
   aprobarlo»). En la llamada no se cobra (`script-de-cierre`, «En este proyecto»).

Los templates concretos se escriben con el copy 3 (paso 2 de `memory/tareas-activas.md`).

