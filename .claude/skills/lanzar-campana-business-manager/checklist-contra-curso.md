# Lista de chequeo contra el curso, antes de publicar

Cada punto se compara con lo que **se lee de vuelta en Meta**, no con lo que se mandó. Se marca ✓ si coincide.
Si difiere y hay una razón anotada, se marca «a propósito». Si no hay razón, se marca ✗.
- Un ✗ se arregla o se le dice a Hans una vez, con el riesgo, y decide él.
- El resultado va a `output/diagnosticos/AAAA-MM-DD-revision-<campaña>-contra-curso.md`.
- Modelo: `output/diagnosticos/2026-10-14-revision-campana-1-contra-curso.md`.

## Cuenta

- [ ] Zona horaria del país y moneda en dólares `[CURSO S7 @ 0:24:38]`. La cuenta de Hans está en Los Ángeles y
      colones, de antes: a propósito.
- [ ] Método de pago cargado: `has_payment_method` en `ads_get_ad_accounts` `[CURSO S7 @ 0:39:00]`.
- [ ] Teléfono y correo verificados `[CURSO S7 @ 0:45:52]`. No se puede leer desde la conexión.
- [ ] Segunda cuenta de respaldo `[CURSO S7 @ 0:25:47]`. No frena una campaña.
- [ ] Columnas «Media Buyer Columns» `[CURSO S8 @ 0:49:37]`. Hacen falta si Hans va a mirar los números en la
      pantalla.

## Creativo

- [ ] Hasta 90 s, vertical, una persona a cámara `[CURSO S6 @ 0:12:54]`, `[CURSO S4 @ 0:32:47]`.
- [ ] Sin música mientras se prueba (medirlo) `[CURSO S6 @ 0:14:17]`.
- [ ] Con subtítulos `[CURSO S6 @ 0:16:05]`.
- [ ] Sin clickbait, emojis ni animaciones `[CURSO S6 @ 0:18:31]`.
- [ ] Portada sin clickbait `[CURSO S6 @ 0:17:47]`.
- [ ] Texto del anuncio corto, con la palabra clave para el mensaje `[CURSO S6 @ 0:21:11–0:24:27]`.
- [ ] CTA del video y del texto alineado con el proceso de ventas `[CURSO S7 @ 0:34:26]`.
- [ ] Políticas de Meta revisadas (`knowledge/referencias/`).

## Campaña

- [ ] Nombre «Campaign N – negocio – creativo» `[CURSO S7 @ 0:52:00–0:52:30]`.
- [ ] Un video por campaña `[CURSO S7 @ 0:53:15]`.
- [ ] Auction, campaña manual `[CURSO S7 @ 0:48:41, 0:51:01]`.
- [ ] Sin categorías especiales, salvo crédito, empleo, vivienda o política `[CURSO S7 @ 0:53:15]`.
- [ ] Objetivo:
  - Clientes potenciales para mensajes a Instagram `[CURSO S7 @ 0:50:31]`, `[CURSO S8 @ 0:48:39]`.
  - Tráfico solo para WhatsApp o para el perfil `[CURSO S8 @ 0:40:14]`.
  - Con ManyChat: Interacción + conversaciones, a propósito.
- [ ] Presupuesto de campaña por día, el monto del Protocolo convertido a la moneda de la cuenta
      `[CURSO S7 @ 0:55:04]`.
- [ ] Puja y lo demás por defecto `[CURSO S7 @ 0:56:06]`.

## Conjunto

- [ ] Nombre «Ad set N – país – género edad» `[CURSO S7 @ 0:57:45–0:58:15]`.
- [ ] Destino: mensajes en Instagram con la página `[CURSO S7 @ 0:58:15–0:58:46]`.
- [ ] Sin la audiencia automática de Meta: `advantage_audience 0` `[CURSO S7 @ 1:01:08, 1:04:07]`.
- [ ] Un país `[CURSO S6 @ 0:46:43]`.
- [ ] Edad y género del avatar `[CURSO S6 @ 0:47:13]`, `[CURSO S6 @ 1:09:09]`.
- [ ] Sin intereses `[CURSO S7 @ 1:01:51]`.
- [ ] Idioma en blanco `[CURSO S7 @ 1:03:40]`.
- [ ] «Reach people beyond your detailed targeting» `[CURSO S7 @ 1:02:41]`: sin intereses, no aplica.
- [ ] Ubicaciones manuales, sin in-stream, search, audience network ni marketplace `[CURSO S7 @ 1:05:33]`.
- [ ] Con presupuesto bajo, una sola plataforma `[CURSO S8 @ 1:34:34]`.

## Anuncio

- [ ] Nombre «Ad N» `[CURSO S7 @ 1:06:31]`.
- [ ] Página y cuenta de Instagram conectadas `[CURSO S7 @ 1:07:05]`.
- [ ] Post existente o video subido: el curso acepta los dos `[CURSO S7 @ 1:08:38]`.
- [ ] Multi-advertiser apagado `[CURSO S7 @ 1:09:09–1:09:42]`.
- [ ] Botón «Send message» / Enviar mensaje `[CURSO S6 @ 0:32:15]`.
- [ ] Vista previa revisada en cada ubicación `[CURSO S6 @ 0:55:47]`.

## Lo que el curso no trata

La plantilla de mensaje de Meta, ManyChat u otros bots, las mejoras automáticas (Advantage+ creative), la fase de
aprendizaje y los errores de publicación. Para eso manda lo decidido con Hans, la documentación oficial y la
tabla de errores de `SKILL.md`. Del curso, lo más cercano a ManyChat es esto: primero se valida la oferta del
anuncio y después se suman automatizaciones `[CURSO S5 @ 0:45:31]`. Por eso ManyChat manda solo el primer
mensaje.
