# IA y adquisición de clientes: quién lo vende, cómo lo nombra y qué queda libre

**Fecha de la investigación:** 2026-10-11. Todas las URL fueron vistas ese día salvo que se indique otra fecha de publicación.
**Para:** Hans (Media Buyer OS). **Tipo:** investigación de mercado en internet; no es un plan.
**Herramientas usadas:** búsqueda web general, lectura directa de páginas y un navegador remoto (Apify) para Reddit y páginas que bloquean lecturas simples. Perplexity no se pudo usar (la cuenta devolvió «quota exceeded», HTTP 401, en cada intento).

**Cómo leer las etiquetas de verificación:**
- `[PROPIO]` = lo dice el actor de sí mismo en su web, sin comprobación externa.
- `[OFICIAL]` = documentación de Meta, FTC u otra fuente primaria.
- `[TERCEROS]` = reseñas de clientes (Trustpilot, G2, Reddit) o análisis de terceros; también sin verificación independiente, pero no es autopromoción.
- `[NO VERIFICADO]` = dato que solo aparece en un fragmento de búsqueda o en una fuente secundaria y no pude confirmar en la fuente original.

---

## 1) Resumen en 10 líneas

1. Hay dos mundos que casi no se tocan: los creadores con marca técnica de IA (Liam Ottley, Nick Saraev, Agustín Medina, Denís Corral…) venden sobre todo **cómo montar una agencia de IA**; los que venden **conseguir clientes con anuncios** casi nunca tienen marca técnica. El cruce de los dos es raro y es exactamente donde Hans quiere pararse.
2. Los pocos que cruzan (LeftClick, GrowthMarketer, Single Grain, Alkimista, Chatty, Tintim) **no hablan de código: hablan de clientes, señales y decisiones**, y usan lo técnico como prueba («operamos dentro de tu cuenta», «nada que mueva plata corre sin tu OK», «cero humo, datos puros»).
3. La categoría no tiene nombre fijo. Conviven «AI Automation Agency», «AI growth partner», «AI-native growth operating partner for paid acquisition», «AI-Native Growth Operator», «setter IA», «Sistema de Adquisición de Clientes con IA», «Growth Partner», «CRM de WhatsApp que trackea todo».
4. Las promesas que se repiten son de **velocidad y disponibilidad** (respuesta en 2 s, 10 s, 90 s; 24/7; «calendario lleno»; «tú solo cierras»), y porcentajes genéricos (+30 %, +65 %, ×2,5) casi siempre `[PROPIO]`. Promesas de dinero solo las hacen los que venden formación (Imperium, creadores de YouTube) y los que terminan en Trustpilot con 1 estrella (Air.ai).
5. Casi nadie garantiza resultado. Las garantías reales son chicas y acotadas: 7 días gratis + «garantía 30 días» (Helix), «14 días reembolso» + «más citas en 30 días o no pagás» medido contra el mes anterior (CallSetter), o pago por cita calificada (LeadsNow). GrowthMarketer escribe literalmente «No guaranteed outcomes» y promete el proceso.
6. Lo que Hans cree que nadie hace —**leer conversaciones de WhatsApp y devolver señales a Meta**— ya existe como primitiva oficial de Meta (Conversions API para mensajería con `ctwa_clid` y evento `QualifiedLead`; «Automatic Events» que usan regex + NLP sobre hilos que nacen de un anuncio) y como función de herramientas (Wati, Kommo, respond.io, Chatfuel, Chatty, Tintim). Lo que **no** encontré es un servicio en español que lo venda como mecanismo con nombre, ni uno en Costa Rica, ni ninguno cuya IA lea la conversación completa y decida calidad y valor sin un humano o una frase gatillo.
7. En Brasil el tema está más maduro (Tintim: 5.800 empresas `[PROPIO]`, R$197–297/mes); en español el más cercano es Chatty (Argentina, US$150–450/mes) que ya envía «Qualified Lead» y «Purchase» a Meta desde el CRM.
8. Los clientes se quejan de lo mismo en todos lados: garantías condicionadas a un gasto en anuncios que no se dijo (Leadscape: «$300 al día» o programa de «$10k/mes»), reembolsos que no llegan (Air.ai, 1,2/5 en Trustpilot y demanda de la FTC), bots que dicen cosas que el negocio no ofrece (Appointwise), soporte que tarda horas y desaparece, y gurús que ganan más vendiendo el modelo que entregando a clientes (Reddit).
9. Riesgos concretos para Hans: la política de anuncios de Meta sobre resultados y ganancias (no prometer «X clientes en 30 días» en el anuncio), la política de WhatsApp de enero 2026 (los bots tienen que ser auxiliares de un negocio concreto, lo que a Hans le sirve), que Meta regale su propio «Business Agent» (junio 2026) y sus «Automatic Events», y la saturación del «con IA» (335.900 miembros en la comunidad de Ottley; en español, embudos de «agencia de IA» prometiendo 10–20 k€ en 90 días).
10. La oportunidad que sale de todo esto, como hipótesis: no venderse como «agencia de IA» ni como «media buyer», sino como el que **cierra el circuito** entre anuncio, conversación y venta, con proceso escrito, aprobaciones antes de gastar, un caso auditado con consentimiento, y una garantía sobre lo que controla (la lectura y el reporte), nunca sobre ingresos.

---

## 2) Tabla de actores

### 2a. Globales en inglés

| # | Actor (país) | Qué vende y cómo lo nombra | Promesa | Qué hace la IA / qué hacen humanos | Precio público | Garantía | Cómo consigue clientes · CTA | Fuente |
|---|---|---|---|---|---|---|---|---|
| 1 | **Liam Ottley / Morningside AI / AI Automation Agency Hub** (NZ/Dubai; clientes AU-NZ-US) | Morningside: «AI Strategy, Upskilling & Custom Development» (no vende anuncios ni leads). Hub en Skool: «Build AI solutions, land clients & get paid. Taught by an agency that ships AI for Fortune 500 companies». Accelerator pago. | «You'll typically see a working pilot within weeks, not months». Hub: aprender el modelo AAA. | Humanos planifican y desarrollan; no separa. | Morningside: no público. Accelerator: US$5.000–7.150 según reseña de terceros (precio solo en llamada). | Ninguna en Morningside. Accelerator: reembolso condicionado a «esfuerzo significativo» `[TERCEROS]`. | YouTube (13,4 M vistas `[PROPIO]`), comunidad gratis de 335.900 miembros → llamada de «alineación». | [morningside.ai](https://www.morningside.ai/) `[PROPIO]`; [skool.com/learn-ai](https://www.skool.com/learn-ai); [marksinsights.com, 2026-02-23](https://marksinsights.com/liam-ottley-review/) `[TERCEROS]` |
| 2 | **LeftClick AI — Nick Saraev** (EE. UU./Canadá) | «The definitive AI growth partner for fast-moving B2B companies». Servicios: AI Automation, **AI Lead Generation**, Custom AI Agents, CRM & Sales Automation, AI Workshops. No gestiona pauta. | Sistemas que «generate leads, close deals, and scale operations». | Humanos construyen, prueban, despliegan y enseñan; la IA es el entregable. | «typically start at $5K»; la mayoría US$10K–50K; precio fijo, sin horas; retainer opcional. | Ninguna («Fixed price, no surprises»). | YouTube 400K+ y 1 M+ seguidores `[PROPIO]` → «Book a free growth call» (30 min) → propuesta con alcance y precio fijos. | [leftclick.ai](https://leftclick.ai/) `[PROPIO]` |
| 3 | **GrowthMarketer — Robbie Jack** (Boulder, EE. UU.) | «The AI-native growth operating partner for paid acquisition». Opera Meta y Google «as one system» (medios, creativo, conversión, medición). | «We can promise the process on this page, not the result». Decisiones por escrito; «nothing that moves money runs without approval by default». | IA: investigación, análisis, producción, implementación. Un operador senior decide y responde: «AI removes layers, not judgment». | No público; llega en una evaluación escrita a 48 h. Mes a mes, 30 días de aviso, sin comisión sobre pauta. | **«No guaranteed outcomes».** | Formulario de 6 preguntas («See if we're a fit»), sin calendario; respuesta escrita en 48 h. Resultados «client-reported» (Coop +32 % ROAS, Kanter 0→US$1 M en 6 meses). | [growthmarketer.com](https://growthmarketer.com/) `[PROPIO]` |
| 4 | **Single Grain — Eric Siu** (EE. UU.) | «AI-Native Growth Operator». «Revenue Marketing Agency». Paid media, SEO/AEO, creativo, «SingleBrain · Managed Revenue Agent Layer». | «We Don't Advise on AI. We Run It.» «Operators in your accounts, not advisors on the sidelines». «3.2x Avg Client ROI», «500+ Companies» `[PROPIO]`. | IA desplegada «inside your team»; estrategas senior operan. | No público. | Ninguna. | Podcasts (Marketing School 140 M+ descargas `[PROPIO]`), YouTube, newsletter → «Talk to an Expert» (estratega responde en 24 h). | [singlegrain.com](https://www.singlegrain.com/) `[PROPIO]` |
| 5 | **OmniFusion AI** (EE. UU., no confirma) | «AI Sales System for High-Ticket Coaches» que venden por DM de Instagram; reemplaza setters humanos. | «Every lead gets a reply in under 90 seconds. 24/7/365». «Handles 1,000+ conversations per day». En vivo en 2–4 semanas. | IA responde, califica, hace seguimiento. Humanos extraen la oferta y la psicología de venta, construyen, monitorean y ajustan; el cliente cierra. | No público («a fraction of the cost» de setters a US$10–20K/mes). | Ninguna; el cliente aprueba conversaciones reales antes del lanzamiento. Pie: «do not represent typical results». | «See If You Qualify →» (cuestionario). Testimonios: «$30K to $125K months in 90 days», «120+ active clients», «$35M+» `[PROPIO]`. | [omnifusion.ai](https://omnifusion.ai/) `[PROPIO]` |
| 6 | **LeadsNow AI** (Australia) | «Lead Generation for High-Ticket Coaches & Consultants»; «AI Booked-Call Engine»; «Pay-Per-Result Pricing». Solo ofertas de US$3k+. | «AI Agents Fill Your Calendar with Pre-Qualified High Ticket Buyers». | IA: llamadas, SMS, email, DM, reactivación de bases, calificación, recordatorios, no-show. Humanos: «Award-Winning Marketers», ingenieros, funnel «done-WITH-you». El cliente cierra. | **US$40–220 por llamada calificada agendada**, o revenue share 5–25 %, o mezcla; «small scope-based setup fee»; cancelación con 14 días de aviso. | «If the appointment does not land qualified, you do not pay for it». Pie: «No results or return on investment is guaranteed». | «Book a Free Strategy Session»; lead magnet «6-Step AI Sales Engine Roadmap». «50,769+ AI-booked appointments» `[PROPIO]`. | [leadsnow.ai/coaches](https://leadsnow.ai/coaches/) `[PROPIO]` |
| 7 | **Imperium Acquisition — Charlie Morgan** (no indica país) | Formación: Imperium Academy (gratis), **EasyGrow 2.0** («Organic, AI based systems»), Acquisition Nirvana, High Ticket Heaven. Para agencias, coaches, consultores. | «hundreds of qualified appointments every month»; «first client in 6 weeks»; «Grow to: 6 & Multi 6 Figures». | No lo explica. | No público (Academy «FREE now. Might be paid soon»). | «We guarantee real, clean-cut business transformation for all students» (sin términos; enlaza «Earnings disclaimer»). | YouTube → «growth call». «2,000+ students», «300+ millionaire students» `[PROPIO]`. | [imperiumacquisition.com](https://www.imperiumacquisition.com/) `[PROPIO]` |
| 8 | **Serge Gatari — ClientAcquisition.io** (Montreal) | «builds client acquisition systems for online service businesses»; programas en Whop: Growth Creator Incubator, Accelerator, Webinar Infrastructure Build; «Build & Release AI» (agencia de IA). | Según reseña de terceros, centrado en cold email. | — | Whop: US$5.800 (de 7.250), US$9.800, US$10.000 `[NO VERIFICADO: lista de Whop]`; «$15k System Blueprint» según ippei.com. | No encontrada. | YouTube («The NEW Way to Start an AI Agency in 2026 (from a $15M Founder)»). | [ippei.com](https://ippei.com/build-release-ai/) `[TERCEROS]`; [whop.com](https://whop.com/joined/clientacquisitionio/products/growth-creator-incubator-6b/) |
| 9 | **Needle** (EE. UU.) | «(AI platform + Human experts)» que «replaced marketing agencies, freelancers, and tools for 200+ DTC brands». | «AI speed, with senior judgment»; «Protect from AI slop». «+177 %» ingresos anualizados, «6-40x Meta ROAS» `[PROPIO]`. | IA analiza la marca, crea campañas y recomienda; estrategas y diseñadores revisan todo antes de salir. | No público («a fraction of a comparable agency»). | Ninguna; «You approve absolutely everything before it goes live». | «Connect Store» / «Book a demo». | [askneedle.com](https://www.askneedle.com/) `[PROPIO]` |
| 10 | **AdAmigo.ai** (Delaware, EE. UU.) | «an AI media buyer that runs your ad accounts on Meta and Google». SaaS + servicio gestionado con media buyer humano supervisando. | «30% uplift in 30 days» (titular). Casos: ROAS +28 %, +223 % `[PROPIO]`. | IA diseña anuncios, lanza, optimiza a diario, vigila anomalías; modo chat o autopilot con aprobación manual o automática. | US$99/mes (cuentas < US$2.000 de gasto), US$349/mes, precio agencia, gestionado sin precio; 7 días gratis. | Ninguna. | «Try for free & get your first audit in minutes»; G2 4,9/5 `[PROPIO]`. | [adamigo.ai](https://www.adamigo.ai/) `[PROPIO]` |
| 11 | **CallSetter.ai** (EE. UU.; home services, voz) | «Done-for-you AI appointment setting» por teléfono/SMS/email para HVAC, plomería, techos, solar. | «answers every lead in under 60 seconds»; «Book More in 30 Days or You Do Not Pay». | IA contesta, califica y agenda; humanos construyen todo (una llamada de 30–60 min con el cliente), soporte y revisiones. | Starter US$497/mes + US$997 setup; Growth US$997 + US$1.497; Enterprise US$1.997 + US$1.997; add-ons SMS/email US$499 + US$149/mes. | «Cancel within the first 14 days for a full refund»; «If your booked appointments from your existing lead flow do not increase within your first 30 days live… you do not pay», medido contra el mes anterior en los registros de llamadas. | Página de precios directa; mes a mes. | [callsetter.ai/pricing](https://callsetter.ai/pricing) `[PROPIO]` |
| 12 | **Setter AI (trysetter.com)** (no indica país) | «Text AI Appointment Setter» por WhatsApp, SMS y web; «replace slow SDRs». Especializado en leads de Meta ads y formularios. | «following up with every lead in 10 seconds»; «In 99.7% of cases, the AI qualifies & books the lead correctly» `[PROPIO]`. | IA califica y agenda; «Onboarding done for you» en planes medios. | Planes por créditos: US$497/mes (1.000 cr.), US$2.297, US$3.497; anual US$397, 1.997, 2.997. DFY si > 500 leads/mes (precio no público). | Ninguna. | Precios en página; «book a call» para DFY. | [trysetter.com/pricing](https://www.trysetter.com/pricing) `[PROPIO]` |
| 13 | **Setor AI** (Lublin, Polonia) | «AI appointment setter for Instagram»; «Verified Meta Tech Partner». | «books more calls than your whole team»; en autopilot a los 14 días. | IA responde DMs, califica, sigue, agenda, procesa notas de voz y reels; humanos onboarding y success manager; el equipo del cliente vende. | US$299 / 499 / 1.000 por mes (1.000 / 2.500 / 10.000 respuestas). | Ninguna; sin prueba gratis (contradice un «Free test drive»). | Demo personalizada con el handle de Instagram → onboarding call. | [setor.ai](https://setor.ai/) `[PROPIO]` |
| 14 | **Appointwise** (no indica país) | «AI appointment setter» para agencias, coaches y consultores; multicanal; «done-for-you setup» opcional. | «books 30-40% of leads on average» `[PROPIO]`. | IA responde y agenda; setup DFY opcional. | Desde US$97/mes; 14 días gratis. | No encontrada. | Prueba gratis. Trustpilot 4,3/5 con 101 reseñas. | [appointwise.io](https://www.appointwise.io/) `[PROPIO]`; [Trustpilot](https://dk.trustpilot.com/review/www.appointwise.io) `[TERCEROS]` |
| 15 | **Air.ai** (EE. UU.) | IA conversacional de voz + «Access Card» + licencias para revender. | Según la FTC: recuperar «tens of thousands of dollars within days or months». | — | — | Prometía reembolso si no ganabas 2–3× la inversión `[OFICIAL: alegación FTC]`. | Trustpilot 1,2/5 (83 reseñas, 98 % de 1 estrella). Demandada por la FTC el 2025-08-25 (≈US$19 M, Business Opportunity Rule). | [Trustpilot](https://ca.trustpilot.com/review/air.ai) `[TERCEROS]`; [FTC, 2025-08-25](https://www.ftc.gov/news-events/news/press-releases/2025/08/ftc-sues-stop-air-ai-using-deceptive-claims-about-business-growth-earnings-potential-refund) `[OFICIAL]` |
| 16 | **Hyros** (EE. UU.; Alex Becker) | «AI tracking» / atribución para anunciantes de alto gasto; call tracking hasta el closer. | Comparativas propias: «under $25K/mo: AnyTrack wins on price». | — | Business desde US$230/mes anual; tiers por ingreso rastreado. | — | Contenido de Becker + comparativas. Sin WhatsApp en lo encontrado. | [hyros.com/pricing-ai-tracking](https://hyros.com/pricing-ai-tracking) `[PROPIO]` |
| 17 | **AcquiSync** | «an AI team that builds your personal brand» (contenido), con «DM qualification» en el plan Growth. Marginal para Hans. | «First content live in 72 hours». | Agentes «Iris», «Ink», «Atlas». | US$125/mes; Growth US$349 «Coming Soon». | Ninguna. | Auditoría de marca gratis. | [acquisync.agency](https://www.acquisync.agency/) `[PROPIO]` |
| 18 | **Icon.com / Arcads** (EE. UU./Francia) | Creativos de anuncios con IA («AI admaker», actores IA). Compiten entre sí. | — | — | Icon US$399 / 999 por mes según rastreador de precios; Arcads desde ≈US$110/mes `[NO VERIFICADO: fuentes de terceros discrepan]`. | Icon: «money-back guarantee» en una página de prueba. | SaaS. | [pricingsaas.com/companies/icon](https://pricingsaas.com/companies/icon); [eesel.ai](https://www.eesel.ai/en/blog/arcads-ai-pricing) `[TERCEROS]` |
| 19 | **Herramientas que cierran WhatsApp → Meta** (ver §5): Chatfuel, respond.io, Wati, Kommo, Infobip, 360dialog, AWS | SaaS, no servicio. | — | Reglas, etapas de pipeline o plantillas; no leen la conversación con un LLM para decidir. | Variable. | — | — | Ver §5 |

### 2b. Español, Latinoamérica y Brasil

| # | Actor (país) | Qué vende y cómo lo nombra | Promesa | Qué hace la IA / qué hacen humanos | Precio público | Garantía | Cómo consigue clientes · CTA | Fuente |
|---|---|---|---|---|---|---|---|---|
| 20 | **Helix — Alejandro Bonet** (España) | «setter IA, CRM y agenda para conseguir clientes». Para coaches, mentorías, clínicas, agencias que cierran por llamada con leads de Meta Ads, WhatsApp o Instagram. | «Helix contesta a cada lead en WhatsApp e Instagram, lo cualifica y te agenda la llamada. Tú solo cierras.» | IA responde, cualifica, agenda, recuerda, hace seguimiento; «Helix Agent» propone acciones y «Siempre te pide permiso antes». Humanos cierran; el fundador «sigue detrás de cada despliegue». | Starter 297 €/mes (500 leads), Pro 597 € (2.000), Agency 1.497 € (10.000; GoHighLevel). IVA incl., sin permanencia. | **7 días gratis** + **«Garantía de los primeros 30 días»**. | «Pruébalo gratis»; simulador «Ver una conversación real»; «Cuéntanos tu caso». Resultados: «Negocio fitness high-ticket · España · 30 días auditados (may-jun 2026) · ~100 leads de Meta Ads»: 88 % responden, 2,5 min mediana, 24 % con cita, ×2,5 agendado `[PROPIO, un solo negocio]`. | [gethelix.es](https://gethelix.es/) `[PROPIO]` |
| 21 | **Alkimista Digital** (Buenos Aires; sirve AR, MX, CO, LatAm) | «Agencia de marketing digital y MarTech»; se llama **Growth Partner** frente a «una agencia tradicional». «Meta Ads Performance», «Automatización y Agentes IA», GTM server-side, GA4, Looker, software propio **cerraloOnline** (agente de ventas IA) y Glance. Para «empresas de servicios de alto valor». | «Sin métricas de vanidad». «Cero humo, datos puros». «Multiplicamos tu equipo de ventas sin sumar costos operativos». Casos: Medicus «99,2 % trazabilidad», Plástica Siglo 21 «82 % de leads filtrados antes de ventas» `[PROPIO]`. | Agentes IA califican y venden; humanos operan pauta y medición. | Sin tarifas; requisito «mínimo $1.000 USD/mes en publicidad digital». | Ninguna. | «Pedir una Auditoría de Crecimiento»; herramientas gratis (auditor AEO, calculadoras de ROAS y de pérdida de tracking). ES/EN/PT. | [alkimistadigital.com](https://alkimistadigital.com/) `[PROPIO]` |
| 22 | **Chatty (letschatty.com)** (Argentina; Gualda Experience) | «CRM de WhatsApp que trackea todo». Registra «canal, campaña, conjunto y anuncio» de cada consulta y avisa a Meta por Conversions API «quién fue un lead calificado y quién terminó comprando» (eventos *Qualified Lead* y *Purchase*). Agente IA opcional. | Que el algoritmo «deja de optimizar por 'mensaje' y empieza a optimizar por venta». Casos: Gualda Training «+33 % ROAS», «+151 % facturación» `[PROPIO]`. | IA responde, califica y hace seguimiento (no en Starter); humanos del cliente venden; Chatty implementa y capacita en PRO/Growth. | Starter US$150/mes; PRO US$225; Growth US$450; agente IA +US$50 + créditos; descuentos 10–30 % por pago adelantado. Cobra aparte la Cloud API de Meta. | Ninguna. | «Agendar videollamada»; escasez «Solo tomamos 15 clientes nuevos al mes»; programa de partners (+90 agencias, 10 % recurrente 12 meses). | [letschatty.com](https://letschatty.com/) `[PROPIO]` |
| 23 | **NexoSmart — Maximiliano Rodríguez** (Bahía Blanca, AR + Valencia, ES; sirve AR, CL, CO, MX, ES, UY, VE, US) | «Agente conversacional IA para leads en WhatsApp» con GPT-4 o Claude + LangChain; calificación BANT, agenda en Calendly/Google, handoff humano, CRM. Para equipos que reciben leads de campañas pagas. | «responde y califica leads en WhatsApp en menos de 10 segundos». «Resultados esperados»: +65 % conversión a reunión, −80 % tiempo de primera respuesta `[PROPIO, etiquetado como esperado]`. | IA califica; humanos venden. Entrega 3–6 semanas. | Setup US$1.000–2.000 + US$100–400/mes. | Ninguna. | «Consultá sin cargo»; cotizador en 3 pasos. No menciona Conversions API ni atribución. Página actualizada octubre 2026. | [nexosmart.com.ar](https://www.nexosmart.com.ar/soluciones/agente-ia-leads-whatsapp/) `[PROPIO]` |
| 24 | **Impulso Digital** (Colombia, prefijo +57) | «Sistemas de adquisición de clientes con IA»: Meta/Google Ads + landing + WhatsApp + agentes IA + CRM + remarketing + reportes. Para restaurantes, clínicas, inmobiliarias, academias, gimnasios, servicios. | Aumentar ingresos «entre un 30% y un 150%», aclarando «Son objetivos de optimización, no promesas absolutas». | IA atiende WhatsApp; humanos pauta, embudos, seguimiento. | No público; «Sin permanencia». | Ninguna (la FAQ hace la pregunta; la respuesta no aparece). | «Diagnóstico gratuito» por WhatsApp. | [impulsodigital.io](https://impulsodigital.io/) `[PROPIO]` |
| 25 | **Scalia Marketing** (Chihuahua, MX) | **«Sistema de Adquisición de Clientes»**: Sistema de Atracción, de Conversión, de Escalamiento + agente IA que «responde, califica y agenda citas de forma automática — 24/7». CRM y dashboard incluidos. | Prospección predecible; excluye a quien busca «resultados inmediatos sin proceso ni inversión». | IA atiende; humanos pauta. | No público. | Ninguna. | «Agenda tu llamada gratuita» (30 min, TidyCal). «15+ años de experiencia comercial». | [scaliamkt.com](https://scaliamkt.com/) `[PROPIO]` |
| 26 | **Clienteli** (Colombia; producto de WebmasterA) | «Agente IA para WhatsApp que vende y agenda citas». «Tech Provider aprobado por Meta». | «Responde en 2 segundos»; «93 %» de conversaciones resueltas sin el equipo (caso Fabripets, 11–30 sep 2026: 3.485 de 3.758) `[PROPIO]`. «No inventa». | IA atiende y agenda; humano toma la conversación cuando hace falta. | COP 119.900 / 189.900 / 299.900 por mes (≈US$35 / 55 / 89); WhatsApp aparte, a Meta. Sin tarjeta, sin permanencia. | Ninguna. | «Comenzar gratis»; demo por WhatsApp. No conecta con anuncios ni CAPI. | [clienteli.com.co](https://clienteli.com.co/) `[PROPIO]` |
| 27 | **SoyAgentia — Alejandro Díaz** (La Estrella, Antioquia, CO) | «agentes de IA» por canal (WhatsApp, Instagram, Messenger, TikTok, web, Shopify) con una base de conocimiento; «proveedor tecnológico autorizado por Meta con Embedded Signup habilitado». | El agente «prefiere decir que consulta con un asesor antes que inventar un precio o un plazo». | IA cotiza, registra pedidos, agenda, envía links de pago, transfiere a humano. | En /pricing (no leído); WhatsApp aparte. | Ninguna. | «Prueba el agente ahora por WhatsApp»; tutoriales YouTube; testimonios en video. | [soyagentia.com](https://www.soyagentia.com/) `[PROPIO]` |
| 28 | **Peper La Agencia — Fanny y Vane** (Heredia, Costa Rica) | «Agencia de marketing digital e inteligencia artificial en Costa Rica». Cuatro caminos: cursos, «agencia on demand» (diseño, redes, ads, agentes de IA), consultorías, programas ejecutivos. | «Hacemos crecer tu negocio con marketing e IA que sí venden». «No hacemos informes bonitos. Instalamos crecimiento». Casos: 38× ROAS clínica dental, 40× retail hospitalario, 40 leads high-ticket/mes en construcción `[PROPIO]`. | No separa. | No público. | Ninguna. | «Agenda tu llamada gratuita» (según etapa del negocio); WhatsApp. IG @pepercr. «Desde 2016». | [pepercr.com](https://pepercr.com/) `[PROPIO]` |
| 29 | **Nubo** (Costa Rica, +506; «SOCIEDAD ANONIMA») | «IA que entiende tu negocio»: chatbot IA («Tu vendedor estrella en WhatsApp, Instagram, Facebook y más»), agentes de voz, automatización, consultoría. No vende anuncios. | «De la idea a los resultados en semanas»; «Recupera el 30 % de tus citas perdidas» (salud) `[PROPIO]`. | IA atiende; equipo implementa en semanas 2–4. | No público. | Ninguna. | «Agenda una consulta gratis» (30 min). Contadores de la web en «0» (sin completar). | [nubocr.com](https://nubocr.com/) `[PROPIO]` |
| 30 | **Magnetis Lab** (Rohrmoser, San José, CR) | Chatbots WhatsApp + CRM (partner Bitrix24 CR/SV/PA), asignación de leads, «conexión con campañas digitales», reportes. | — | — | Artículo del 2026-06-16 sobre precios **sin cifras**: «puede iniciar desde rangos mensuales bajos», «puede existir un costo de implementación inicial»; Meta cobra mensajes aparte. | — | «Cotizar Chatbot» por WhatsApp. | [magnetislab.com](https://www.magnetislab.com/precio-chatbot-whatsapp-costa-rica) `[PROPIO]` |
| 31 | Otros en Costa Rica (solo búsqueda, no leídos): SmartizaLatam, Automaxia, Runia, Bluemedia, Click Digital, ToGrow | Chatbots/agentes IA para WhatsApp, automatización, marketing con IA. | — | — | — | — | — | [smartizalatam.com](https://www.smartizalatam.com/), [automaxia.com](https://automaxia.com/), [runia.ar/cr](https://runia.ar/cr/chatbot-whatsapp), [togrowagencia.com](https://togrowagencia.com/servicios-de-ia-para-whatsapp-en-san-jose/) `[NO VERIFICADO]` |
| 32 | **BEOFFON** (Valencia/Madrid/Barcelona, ES) | «Motor de Crecimiento & Inteligencia Artificial 2026» / «BEOFFON ENGINE»: «Funnels & Campañas de Alta Conversión» en Meta y Google + «Agente de Inteligencia Artificial 24/7» por WhatsApp/IG/web + SEO local. Sector referencia «Clínica / Salud / Estética (Ticket Alto)». | «Multiplicamos tus ventas y captamos 10+ nuevos clientes para tu empresa este año»; «Tiempo estimado de Captación: 60 a 90 Días»; simulador 10 clientes × 1.500 € (es simulación). | Agente IA responde «< 5 sec»; humanos hacen campañas y SEO. | No público; «Coste Fraccionado». | «ROI Garantizado» / «Garantía de Resultados» **sin condiciones, plazos ni compensación en la web**. | «Recibir Auditoría Gratuita» (< 24 h); urgencia «Solo quedan 2 plazas». «+500 PYMES» `[PROPIO]`. | [beoffon.com](https://beoffon.com/index.html) `[PROPIO]` |
| 33 | **HazloFácil Citas** (España; equipo Bumpho) | «agente de IA que atiende a tus clientes por WhatsApp y en tu web» y deja la cita en el calendario del comercial. Para negocios que cierran en reunión. | «Medimos citas, no mensajes». Caso real con consentimiento (International Experience, 9 sep–8 oct 2026): 88 conversaciones, 51 leads con email, 29 citas (33 %), «menos de 7 € por cita» `[PROPIO]`. | IA atiende; humanos validan con 10 tests antes de producción y optimizan 3 h/mes. | **199 €/mes** (hasta 600 conversaciones, 3 h de optimización; hora extra 90 €); puesta en marcha «a consultar»; **permanencia 6 meses**. | Ninguna explícita. | «Pide una demo» por WhatsApp; «Ver caso real». No conecta con anuncios. | [hazlo-facil.es](https://hazlo-facil.es/) `[PROPIO]` |
| 34 | **Beyond The Big** (Barcelona) | «sistema propio de captación»: **Método BeyondLeads™** y plataforma **BeyondLeads™ Studio** (captación, seguimiento, CRM, conversaciones, automatización). Google Ads, Meta Ads, «Automatizaciones y agentes de IA». | «Consigue hasta un 30% más de leads cualificados y convierte hasta un 50% más en clientes en menos de 90 días». «+2M € al año» gestionados `[PROPIO]`. | — | No público. | Ninguna. | «1ª consultoría estratégica GRATUITA» (30 min); auditoría gratis. | [beyondthebig.com](https://beyondthebig.com/) `[PROPIO]` |
| 35 | **Flowmatic / Aivara** (España) | «Automatización inteligente para empresas» con n8n; chatbots IA. Artículo sobre leads de Meta Ads con IA. | Casos: «−94 % errores», «+52 % conversiones» `[PROPIO]`; contadores en «0». | — | No público. | Ninguna. | «Solicita una reunión». | [flowmatic.es](https://flowmatic.es/) `[PROPIO]` |
| 36 | **Sinteqia** (sin país; ES/FR) | «Sistema inteligente de leads»: landing + automatización + CRM + agente IA. | «+35 % más conversión de leads», «−10 s respuestas» `[PROPIO]`. | — | No público. | Ninguna. | «Agendar mi sesión gratuita» (Tally). | [sinteqia-landing.webflow.io](https://sinteqia-landing.webflow.io/) `[PROPIO]` |
| 37 | **Agencia IA Solutions — Jorge Luján Montes** (València) | «Captar Clientes con IA: Automatiza tu Pipeline» (prospección B2B, cold email, LinkedIn, nurturing, agenda). Meta Ads y WhatsApp en otras páginas. | Primeros leads «en las primeras 2 o 3 semanas». | — | No público. | Ninguna. | Formulario; WhatsApp. | [agenciaiasolutions.com](https://agenciaiasolutions.com/captar-clientes-con-ia/) `[PROPIO]` |
| 38 | **Javadex — Javier Santos Criado** (Vigo) | Consultor IA (Cortex by Javadex, agentes 24/7, RAG, back-office, GEO, formación Claude Code). No vende leads ni anuncios. | «Te implemento un sistema de IA que te ahorra tiempo, reduce costes y aumenta tus ingresos». | — | «Desde 5.000 €, en 4-8 semanas, llave en mano». | Ninguna. | Formulario de contacto. Ranqueado #1 por Upliora (que vende lo suyo; conflicto de interés). | [javadex.es](https://www.javadex.es/) `[PROPIO]`; [upliora.es](https://www.upliora.es/comparativas/mejores-canales-youtube-ia-espana-2026) `[TERCEROS]` |
| 39 | **Xavier Mitjana — IA en acción** (España) | Consultoría y formación en IA; programa AcademIA. | — | — | AcademIA 895 € según un artículo promocional `[NO VERIFICADO]`. | — | YouTube/LinkedIn. | [iaenaccion.com](https://iaenaccion.com/sobre-nosotros/) `[PROPIO]` |
| 40 | **Creadores de YouTube en español que venden «cómo montar tu agencia de IA»**: Agustín Medina «AI Agency Academy» (@agustinmedinaIA; CEO de LambdaIA, fundador de AILink), Denís Corral (@deniscorral), Nexum AI (@NexumAI), Claudio Conde (@condeclaudioad) | Videos: «Cómo crear una Agencia de IA Rentable en 2026 (El Método 4D)», «Cómo Escalé mi Agencia de IA a $10k/mes», «las agencias de IA desaparecerán este 2026.» (descripción promete 10–20 k€ en < 90 días `[NO VERIFICADO]`), «14 Formas de Conseguir Clientes Para tu Agencia de IA en 2026», «Así voy a llegar a 100k/mes…». | Ingresos de la agencia del creador: Medina «más de 32.000 € al mes» según descripción de un video ajeno `[NO VERIFICADO]`. | — | No público. | — | YouTube → comunidad de pago. CreatorDB le atribuye a Medina ≈160 K seguidores `[TERCEROS]`. | oEmbed de YouTube para autoría; [creatordb.app](https://creatordb.app/creatorstats/agustinmedinaia/); [lilys.ai (resumen de video)](https://lilys.ai/es/notes/ai-automation-20260304/ai-agency-32k-month-free) |
| 41 | **Perfiles de Instagram en español detectados en fragmentos de búsqueda** (no pude abrir Instagram): @sanmunoz.ia (~179 K; «agentes IA y Claude Code… casos de éxito y una comunidad»), @laingeniela (~109 K), @_rubenandres19 (~63 K; «ayuda a emprendedores y empresas a escalar su facturación con marketing y sistemas con IA»), @hackeatutiempo (~62 K), @valentin_ayesa (~15 K; «Embajador de N8N en España») | — | — | — | — | — | — | Fragmentos de búsqueda `[NO VERIFICADO]` |
| 42 | **Tintim** (Brasil; Codevance) | SaaS para «gestores de tráfego» y agencias: «rastreie suas conversas»; «descobrir, de forma automática, qual a campanha, conjunto e anúncio que originou aquela conversa»; detecta venta y valor y los envía a Meta «de forma 100% automática». No es CRM ni bot. | «Mais de 5.800 empresas confiam» `[PROPIO]`. | Detección de venta: frase gatillo escrita por el vendedor, tarjeta Kanban, o «Inspetor de Vendas» con IA (desde fines de julio 2026: corre una vez al día, muestra confianza y contexto, **requiere aprobación humana**, solo texto) según un competidor `[TERCEROS: Chatfuel, 2026-08-17]`. Con API oficial no hay captura nativa: usa un mensaje rastreable en la plantilla del anuncio `[PROPIO: base de conocimiento]`. | R$197 (Inicial) / R$297 (Escala) por mes; agencias a consultar; 7 días gratis. | Ninguna. Cancelación anticipada paga el saldo restante `[TERCEROS]`. | «Teste Grátis»; programa de partners; descuento de reventa «desde 65 %» `[TERCEROS]`. | [tintim.app](https://www.tintim.app/) `[PROPIO]`; [chatfuel.com/blog/chatfuel-vs-tintim](https://chatfuel.com/blog/chatfuel-vs-tintim) `[TERCEROS]`; [base de conocimiento Tintim](https://tintim.app/base-de-conhecimento/integracao-do-whatsapp-com-o-tintim-via-api-oficial-como-configurar-o-rastreio-correto-de-campanhas-de-mensagem/) |
| 43 | **UTMify / UTMizey** (Brasil) | Atribución server-side y CAPI para infoproductos y e-commerce; sin WhatsApp en lo encontrado. | — | — | — | — | — | [utmpixel.com/ferramentas/utmify](https://utmpixel.com/ferramentas/utmify) `[TERCEROS]` |
| 44 | **Integradores Meta en LatAm**: Latin Meta Services; iTechDev (México, «Meta Tech Provider»); DINOLABS (Colombia, API WhatsApp COP 200.000–600.000/mes) | Integración CRM/ERP ↔ WhatsApp Business Platform, Marketing API, Conversions API. | — | — | — | — | — | [latinmetaservices.com](https://latinmetaservices.com/), [itechdev.com.mx](https://itechdev.com.mx/en/servicios/whatsapp-business-api), [dinolabs.dev](https://www.dinolabs.dev/agentes-ia) `[NO VERIFICADO]` |
| 45 | **Media Buyers HQ (mediabuyers.ai) — Sebastián Gómez** | El curso que lleva Hans. | — | — | — | — | — | No apareció en ninguna búsqueda y la web no respondió (ECONNREFUSED) el 2026-10-11. `[NO VERIFICADO]` |

**Conteo:** 45 filas; 36 actores con ficha propia leída en su web o en reseñas (`[PROPIO]`/`[TERCEROS]`), el resto solo por fragmentos de búsqueda.

---

## 3) Fichas de los 10 más relevantes para Hans

### 3.1 Helix (España) — el «setter IA» que más se parece al cliente de Hans
- **Qué es:** SaaS con servicio detrás, de Alejandro Bonet, nacido de un negocio fitness high-ticket. Público explícito: «si el servicio se cierra con una llamada y los leads llegan por Meta Ads, WhatsApp o Instagram». Excluye a quien no tiene leads, vende barato o quiere vender sin ninguna persona.
- **Cómo lo nombra:** «setter IA, CRM y agenda para conseguir clientes».
- **Promesa:** «Helix contesta a cada lead… lo cualifica y te agenda la llamada. Tú solo cierras.» Sin promesas de dinero.
- **IA vs humano:** la IA responde, cualifica, agenda, recuerda y sigue; «Helix Agent» propone y «Siempre te pide permiso antes». El fundador «sigue detrás de cada despliegue y de cada cliente».
- **Precio y garantía:** 297 / 597 / 1.497 €/mes; 7 días gratis; «Garantía de los primeros 30 días»; sin permanencia.
- **Prueba que muestra:** un único negocio, «30 días auditados (may-jun 2026), ~100 leads de Meta Ads»: 88 % responden, mediana de primera respuesta 2,5 min, 24 % terminan con cita, ×2,5 tasa de agendado. Otro dato: «el 51 %» de los leads escribe fuera de horario (624 leads, mayo–septiembre 2026).
- **Embudo:** prueba gratis → simulador de conversación → «Cuéntanos tu caso» para que lo monten por ti. No hay demo con llamada.
- **Por qué importa:** es el formato de prueba más honesto que encontré en español (un caso, ventana cerrada, cifras de proceso y no de ingresos) y la garantía más concreta. Fuente: [gethelix.es](https://gethelix.es/) `[PROPIO]`.

### 3.2 LeftClick AI — Nick Saraev (EE. UU./Canadá) — marca técnica que vende leads
- **Qué es:** agencia del creador de contenido Nick Saraev (400 K+ suscriptores en YouTube `[PROPIO]`), conocido por tutoriales de Make y n8n.
- **Cómo lo nombra:** «The definitive **AI growth partner** for fast-moving B2B companies». Servicios: AI Automation, **AI Lead Generation**, Custom AI Agents, CRM & Sales Automation, AI Workshops. No gestiona pauta.
- **Promesa:** sistemas que «generate leads, close deals, and scale operations». «We don't just advise. We build.»
- **Precio:** «typically start at $5K», la mayoría US$10K–50K, precio fijo, retainer opcional. Sin garantía.
- **Embudo:** llamada gratis de 30 min (auditoría del embudo) → propuesta con alcance, plazo y precio fijos → construcción con actualizaciones semanales → retainer opcional.
- **Congruencia:** el contenido enseña a construir; la agencia vende resultados de negocio. Los logos (Anthropic, MrBeast, Notion, Wix) aparecen «sin relación descrita». Caso propio: Maker School US$250K/mes (negocio de Nick, no cliente).
- **Por qué importa:** demuestra que una marca técnica puede vender adquisición si en la web habla de clientes y precio fijo, no de herramientas. Fuente: [leftclick.ai](https://leftclick.ai/) `[PROPIO]`.

### 3.3 GrowthMarketer — Robbie Jack (Boulder, EE. UU.) — el modelo más parecido al que Hans describe
- **Qué es:** un operador senior con IA que corre la adquisición paga de empresas que gastan US$50K–500K/mes.
- **Cómo lo nombra:** «The **AI-native growth operating partner** for paid acquisition». Meta y Google «as one system».
- **Promesa (literal):** «We can promise the process on this page, not the result». Entrega: «Signal Audit», «Growth Memory», decisiones semanales por escrito, «Experiment Record». «Nothing that moves money runs without approval by default».
- **IA vs humano:** «AI removes layers, not judgment»; la IA investiga, analiza, produce e implementa; el operador decide y responde.
- **Precio y términos:** no público; evaluación escrita en 48 h con alcance, precio y tiempos; mes a mes; 30 días de aviso; sin comisión ni markup sobre pauta; las plataformas facturan al cliente.
- **Garantía:** «No guaranteed outcomes».
- **Embudo:** formulario de 6 preguntas, sin calendario; decisión por escrito en 48 h.
- **Por qué importa:** es casi la regla de Hans («nada se activa ni se gasta sin OK») convertida en propuesta de valor, y vende proceso en vez de resultado. Fuente: [growthmarketer.com](https://growthmarketer.com/) `[PROPIO]`.

### 3.4 Single Grain — Eric Siu (EE. UU.) — cómo una agencia de toda la vida se volvió «AI-native»
- **Cómo lo nombra:** «AI-Native Growth Operator»; «Revenue Marketing Agency»; capa de agentes «SingleBrain».
- **Promesa:** «We Don't Advise on AI. We Run It.» «Operators in your accounts, not advisors on the sidelines». «3.2x Avg Client ROI», «500+ Companies» `[PROPIO]`.
- **Congruencia:** el fundador escribe que «The Last Two Have Been the Most Disruptive» y que construyeron agentes «already running inside client accounts». El contenido (dos podcasts, YouTube, newsletter) muestra «the AI systems, playbooks, and campaigns we're running for clients and ourselves».
- **Embudo:** «Talk to an Expert» → auditoría + quick wins en el mes 1 → roadmap de 90 días.
- **Por qué importa:** la prueba de IA se muestra operando en cuentas reales, no en demos. Fuente: [singlegrain.com](https://www.singlegrain.com/) `[PROPIO]`.

### 3.5 LeadsNow AI (Australia) — pago por cita calificada
- **Cómo lo nombra:** «AI Booked-Call Engine», «Pay-Per-Result Pricing». Solo ofertas de US$3k+ (engagements «$3k–$25k+»).
- **Precio:** US$40–220 por llamada calificada agendada por la IA, o revenue share 5–25 %, o mezcla; «small scope-based setup fee»; sin retainer; 14 días de aviso.
- **Garantía:** «If the appointment does not land qualified, you do not pay for it». Y en el pie: «No results or return on investment is guaranteed».
- **IA vs humano:** IA en llamadas, SMS, email, DM, reactivación, calificación, recordatorios, no-show; humanos en estrategia y construcción del funnel («Done-WITH-you»).
- **Cifras propias con inconsistencias:** «50,769+ AI-booked appointments», «no setup fee gates» junto a «small scope-based setup fee», y una «matemática de embudo» que no cierra (1–20 % por etapa «= 300 %»).
- **Por qué importa:** muestra el tope de la escala de riesgo compartido y lo que hay que definir por escrito (qué es «calificada»). Fuente: [leadsnow.ai/coaches](https://leadsnow.ai/coaches/) `[PROPIO]`.

### 3.6 OmniFusion AI — «AI Sales System» para coaches en Instagram
- **Promesa:** respuesta en < 90 s, 24/7, «1,000+ conversations per day»; en vivo en 2–4 semanas.
- **IA vs humano:** el equipo extrae la oferta, la psicología de venta y las objeciones del cliente y construye; monitorea y ajusta; el cliente revisa conversaciones reales y firma antes del lanzamiento; el cliente cierra.
- **Precio:** no público. **Garantía:** ninguna; el sistema no sale si el cliente no lo aprueba.
- **Embudo:** «See If You Qualify →» (cuestionario de calificación), no llamada abierta.
- **Advertencia:** «Results shown are from real clients but do not represent typical results»; el «99 % of leads have no idea they're talking to AI» no tiene soporte.
- **Por qué importa:** el embudo de calificación y la aprobación previa de conversaciones son dos piezas copiables; las cifras de ingresos de los testimonios son lo que Meta no deja poner en anuncios (ver §8). Fuente: [omnifusion.ai](https://omnifusion.ai/) `[PROPIO]`.

### 3.7 Alkimista Digital (Argentina) — «Growth Partner» con medición como bandera
- **Cómo lo nombra:** «Agencia de marketing digital y MarTech», «Growth Partner» frente a «una agencia tradicional». Para «empresas de servicios de alto valor» (SaaS, agencias, high-ticket, franquicias, clínicas, estudios jurídicos y contables, construcción).
- **Qué vende:** Meta Ads Performance, Google Ads, «Automatización y Agentes IA», GTM server-side, GA4, dashboards, SEO/AEO, email; software propio cerraloOnline (agente IA de ventas) y Glance.
- **Promesa:** «Sin métricas de vanidad», «Cero humo, datos puros», «Multiplicamos tu equipo de ventas sin sumar costos operativos». Casos con nombre: Medicus «99,2 % trazabilidad», ManpowerGroup «0 % gasto desperdiciado», Vidrear «+2.900 leads/mes» `[PROPIO]`.
- **Requisito:** «mínimo $1.000 USD/mes en publicidad digital». Sin precios, sin garantía.
- **Embudo:** «Pedir una Auditoría de Crecimiento»; herramientas gratis (auditor AEO, calculadora de ROAS y de pérdida de tracking).
- **Por qué importa:** es el actor en español que más cerca está de vender «trazabilidad» como mecanismo, aunque no lo liga a conversaciones de WhatsApp. Fuente: [alkimistadigital.com](https://alkimistadigital.com/) `[PROPIO]`.

### 3.8 Chatty (Argentina) — el CRM de WhatsApp que ya devuelve señales a Meta
- **Cómo lo nombra:** «CRM de WhatsApp que trackea todo».
- **Qué hace:** registra «canal, campaña, conjunto y anuncio» de cada consulta (Meta, Google, TikTok, mail, influencers, web) y envía por Conversions API «quién fue un lead calificado y quién terminó comprando» (*Qualified Lead*, *Purchase*). Objetivo: que el algoritmo «deja de optimizar por 'mensaje' y empieza a optimizar por venta». Agente IA opcional que «Entiende la respuesta del cliente y responde como si fuese un humano».
- **Precio:** US$150 / 225 / 450 por mes según contactos nuevos; agente IA +US$50 + créditos; Cloud API aparte.
- **Embudo:** videollamada de diagnóstico; «Solo tomamos 15 clientes nuevos al mes»; partners: +90 agencias, 10 % recurrente 12 meses.
- **Qué no hace:** no vende el servicio de pauta ni el análisis; el «lead calificado» lo marca el flujo o el equipo del cliente.
- **Por qué importa:** confirma que en español el circuito WhatsApp → Meta ya existe como producto; Hans podría integrarlo o competir con algo que lea la conversación entera. Fuente: [letschatty.com](https://letschatty.com/) `[PROPIO]`.

### 3.9 Tintim (Brasil) — lo más parecido a «leer la conversación para saber qué anuncio vende»
- **Qué hace (propio):** «descobrir, de forma automática, qual a campanha, conjunto e anúncio que originou aquela conversa», detectar venta y valor, clasificar por etapa y enviar a Meta «de forma 100% automática». Para gestores de tráfico y agencias. R$197–297/mes. «Mais de 5.800 empresas».
- **Cómo detecta la venta (según un competidor que lo probó, Chatfuel, 2026-08-17):** frase gatillo tipeada por el vendedor (falla con emoji o signo de exclamación), tarjeta Kanban movida a mano, o «Inspetor de Vendas» con IA desde fines de julio 2026: corre una vez por día, de noche, da un índice de confianza con contexto y **un humano aprueba a la mañana siguiente**; solo lee texto, no audios ni fotos de comprobantes. Envía por CAPI y pixel; también conversiones offline de Google.
- **Limitación con API oficial (propio):** «não há como fazer a captura nativa dos dados»; usa un mensaje rastreable en la plantilla del anuncio.
- **Por qué importa:** el mercado más maduro de LatAm en esto todavía resuelve la detección con reglas y aprobación humana; la lectura real de la conversación con IA, en tiempo real, con valor y calidad, sigue abierta. Fuentes: [tintim.app](https://www.tintim.app/) `[PROPIO]`; [Chatfuel vs Tintim](https://chatfuel.com/blog/chatfuel-vs-tintim) `[TERCEROS]`; [base de conocimiento](https://tintim.app/base-de-conhecimento/integracao-do-whatsapp-com-o-tintim-via-api-oficial-como-configurar-o-rastreio-correto-de-campanhas-de-mensagem/) `[PROPIO]`.

### 3.10 Peper La Agencia (Heredia, Costa Rica) — el competidor local que ya dice «marketing e IA»
- **Cómo lo nombra:** «Agencia de marketing digital e inteligencia artificial en Costa Rica». Cuatro entradas: cursos y bootcamps de IA/marketing/ventas; «agencia on demand» (diseño, redes, ads, agentes de IA); consultorías; programas ejecutivos de 8 semanas a 1 año.
- **Promesa:** «marketing e IA que sí venden»; «No hacemos informes bonitos. Instalamos crecimiento»; un sistema que «atrae y califica clientes».
- **Cifras propias:** 38× ROAS clínica dental («Por cada $1 invertido, $38 de retorno»), 40× retail hospitalario, «40 leads calificados high-ticket al mes» en construcción, «Desde 2016».
- **Precio y garantía:** no público; ninguna.
- **Embudo:** llamada gratis según etapa («Estoy empezando», «Quiero más clientes», «Necesito ordenar mi estrategia», «Quiero un plan a la medida»); WhatsApp +506 7045-8259; IG @pepercr.
- **Por qué importa:** en Costa Rica el «marketing + IA» ya se vende, pero como catálogo de servicios y con cifras de ROAS sin ventana ni método. No encontré a nadie en el país que venda atribución de conversaciones o devolución de señales a Meta. Fuente: [pepercr.com](https://pepercr.com/) `[PROPIO]`.

---

## 4) Patrones

### 4.1 Cómo nombran la categoría
| Etiqueta | Quién la usa | Nota |
|---|---|---|
| «AI Automation Agency (AAA)» | Liam Ottley (comunidad de 335.900) y los creadores en español que lo replican | Es la etiqueta más saturada y la que Reddit asocia a gurús (ver §6). |
| «AI growth partner» | LeftClick (Saraev) | Único uso literal encontrado en una agencia con nombre; el resto son taglines de empresas pequeñas (Groovy Web, Growth Partner AI). |
| «AI-native growth operating partner for paid acquisition» | GrowthMarketer | La descripción más cercana al servicio de Hans. |
| «AI-Native Growth Operator» | Single Grain | Agencia grande reposicionada. |
| «AI platform + Human experts» | Needle | Hace explícita la mezcla. |
| «AI media buyer» | AdAmigo; también Creatify («AI Media Buyer: el agente de IA que gestiona tus anuncios») | Software que compite con el oficio de Hans por el lado barato. |
| «AI Sales System» / «AI Booked-Call Engine» / «AI appointment setter» | OmniFusion / LeadsNow / Setor, Appointwise, CallSetter, Setter AI | Nombran la pieza, no la agencia. |
| «setter IA» | Helix, ZeroChats (MLM) | Traducción española del anterior. |
| «Sistema de Adquisición de Clientes [con IA]» | Scalia (MX), Impulso Digital (CO), Sinteqia («Sistema inteligente de leads») | Fórmula estándar en LatAm; nadie es dueño de ella. |
| «Growth Partner» | Alkimista (AR) | En español, con ads + agentes IA + medición. |
| «Motor de Crecimiento & IA», «Método BeyondLeads™», «BEOFFON ENGINE» | Beoffon, Beyond The Big (ES) | Mecanismo con marca registrada en la web. |
| «CRM de WhatsApp que trackea todo» | Chatty (AR) | Nombra la función, no la categoría. |
| «Agente IA para WhatsApp que vende y agenda citas» | Clienteli (CO), HolDi (MX), Uniamos, Orchesta (CO) | Commodity en 2026: decenas de proveedores por país. |

### 4.2 Promesas que se repiten
1. **Velocidad de respuesta:** «2 segundos» (Clienteli), «10 segundos» (Setter AI, NexoSmart), «< 60 s» (CallSetter), «< 90 s» (OmniFusion), «2,5 min mediana» (Helix). Es la promesa más medible y más común.
2. **Disponibilidad:** «24/7», «fuera de horario» (Helix: 51 % de leads escriben fuera de horario; Clienteli: 42 %).
3. **«Calendario lleno» / «tú solo cierras»:** LeadsNow, Helix, OmniFusion, Setor.
4. **Porcentajes de mejora sin ventana ni base:** «+30 a +150 %» (Impulso), «+35 %» (Sinteqia), «+65 %» (NexoSmart, etiquetado «esperado»), «hasta 30 % más leads y 50 % más clientes en 90 días» (Beyond The Big), «+240 % leads» (Beoffon).
5. **Plazos:** «en semanas» (Nubo, Morningside), 2–4 semanas (OmniFusion), 3–6 semanas (NexoSmart), 60–90 días (Beoffon), 90 días (Single Grain, Beyond The Big).
6. **Dinero:** solo en formación (Imperium «6 & Multi 6 Figures»; videos en español «10k/mes», «100k/mes», «10–20 k€ en 90 días») y en el caso que terminó en la FTC (Air.ai). Las agencias serias **evitan cifras de ingresos** o las ponen como testimonio con disclaimer (OmniFusion).

### 4.3 Mecanismos con nombre
EasyGrow 2.0 (Imperium), Método 4D (Agustín Medina), Método BeyondLeads™ y BeyondLeads™ Studio (Beyond The Big), BEOFFON ENGINE, Helix Agent, SingleBrain (Single Grain), Signal Audit / Growth Memory / Experiment Record (GrowthMarketer), AI Booked-Call Engine (LeadsNow), Inspetor de Vendas (Tintim), cerraloOnline (Alkimista). Patrón: el nombre va sobre **el proceso o la pieza de software**, no sobre la IA en abstracto.

### 4.4 Rangos de precio (públicos)
| Tipo | Rango | Ejemplos |
|---|---|---|
| Agente/setter IA SaaS en LatAm | US$35–89/mes | Clienteli (COP 119.900–299.900) |
| Agente/setter IA SaaS en España/EE. UU. | 199–1.497 €/mes; US$97–1.000/mes | HazloFácil 199 € (permanencia 6 meses); Helix 297–1.497 €; Appointwise desde US$97; Setor US$299–1.000; Setter AI US$397–3.497 |
| Agente IA a medida con setup | US$1.000–2.000 setup + US$100–400/mes | NexoSmart |
| Voz DFY (home services) | US$497–1.997/mes + US$997–1.997 setup | CallSetter |
| CRM WhatsApp con atribución | US$150–450/mes; R$197–297/mes | Chatty; Tintim |
| «AI media buyer» SaaS | US$99–349/mes | AdAmigo |
| Agencia/sistemas con IA, proyecto | US$5K–50K; «desde 5.000 €» | LeftClick; Javadex |
| Pago por resultado | US$40–220 por cita calificada; 5–25 % revenue share | LeadsNow |
| Guías de pricing de agencias de automatización (`[TERCEROS]`) | setup US$2.000–10.000 + retainer; o US$1.200 base + US$45 por lead calificado; chatbots 1.500–5.000 € + 300–800 €/mes | [taskip.net](https://taskip.net/ai-automation-agency-pricing/); [tribuclaw.com](https://tribuclaw.com/blog/montar-agencia-automatizacion-ia/) |
| Formación «monta tu agencia» | US$5.000–7.150 (AAA Accelerator); US$5.800–10.000 (Gatari, Whop) | ver tabla |
| Requisitos de pauta mínima | US$1.000/mes (Alkimista); 300–600 €/mes «mínimo recomendado para pymes en España» (`[TERCEROS]` guía engrana.es); 800–1.200 US$/mes (guía colombiana fabipers.com) | — |

### 4.5 Garantías
- **Lo normal es ninguna.** GrowthMarketer la niega por escrito («No guaranteed outcomes»); LeadsNow la niega en el pie mientras cobra por resultado.
- **Las que existen son chicas y sobre lo controlable:** 7 días gratis + 30 días (Helix); 14 días de reembolso + «más citas que el mes anterior en 30 días o no pagás» (CallSetter); pago por cita calificada (LeadsNow).
- **Las que suenan grandes no tienen términos:** «ROI Garantizado» (Beoffon), «We guarantee real, clean-cut business transformation» (Imperium).
- **Las que generan quejas:** garantías condicionadas a gasto en pauta no informado (Leadscape: «$300 per day», «$10k/mo minimum program»), o reembolsos prometidos y no pagados (Air.ai; HighDrop). Ver §6.

### 4.6 Cómo resuelven la congruencia entre marca técnica de IA y servicio comercial
1. **Hablan de clientes, no de código.** LeftClick: «generate leads, close deals»; Single Grain: «pipeline», «revenue»; GrowthMarketer: «decisions», «signals». La herramienta aparece como prueba, no como tema.
2. **Muestran la IA operando en cuentas reales.** Single Grain: «Proprietary AI systems already running in client accounts — not pitched in decks»; «Operators in your accounts, not advisors on the sidelines». Helix: simulador «Ver una conversación real».
3. **Convierten la transparencia técnica en control para el cliente.** GrowthMarketer: todo por escrito y con aprobación antes de mover plata; Helix Agent «siempre te pide permiso antes»; Needle: «You approve absolutely everything before it goes live»; OmniFusion: el cliente firma las conversaciones antes del lanzamiento.
4. **Separan enseñar de vender.** Ottley y Saraev enseñan el modelo en YouTube y venden el servicio en otra web; en español, los creadores (Medina, Corral, Conde, Nexum) se quedaron en «cómo montar tu agencia» y no encontré que ninguno venda adquisición para dueños de negocio.
5. **La entrada es una auditoría, no una demo del bot.** «Signal Audit» (GrowthMarketer), «Auditoría de Crecimiento» + calculadora de pérdida de tracking (Alkimista), auditoría gratis (Beyond The Big, Beoffon, Single Grain), «funnel map audit» (LeftClick).
6. **Lo que dice Reddit sobre esto (`[TERCEROS]`):** «sell the solution not the tech. Clients typically don't understand AI» (r/agency); «What clients pay for is judgment and distribution» (r/automation); «Setting up an AI agent for most businesses is pretty straightforward so what you need to do is figure out what you can do for businesses… that save them either time, money, or both» (r/automation).

---

## 5) Huecos: qué no hace nadie o casi nadie (y qué sí existe)

### 5.1 Lo que ya existe y hay que saber antes de decir «nadie lo hace»
| Capacidad | Existe | Evidencia |
|---|---|---|
| Devolver a Meta eventos que ocurren dentro de WhatsApp, atados al anuncio exacto | **Sí, oficial.** Conversions API for Business Messaging: `ctwa_clid` es «a required field for sending events»; eventos soportados: Purchase, LeadSubmitted, **QualifiedLead**, InitiateCheckout, AddToCart, ViewContent, OrderCreated… con `action_source: business_messaging` y `messaging_channel: whatsapp`; Meta no deduplica; «enables access to purchase optimization for ads that click to… WhatsApp». Requiere app de desarrollador, acceso avanzado a `whatsapp_business_management` y `whatsapp_business_manage_events`, tier de Marketing API (el banner dice 500 llamadas exitosas en 15 días) y Embedded Signup o Facebook Login for Business. | [developers.facebook.com — CAPI Business Messaging](https://developers.facebook.com/docs/marketing-api/conversions-api/business-messaging) `[OFICIAL]` |
| **Meta leyendo la conversación** para detectar lead y compra | **Sí, oficial y opt-in.** «Automatic Events API»: Meta analiza hilos nuevos que nacen de un anuncio click-to-WhatsApp con «a combination of regex and natural language processing» y emite `LeadSubmitted` y `Purchase` por webhook `automatic_events`; el negocio opta en Embedded Signup o con los toggles «Automatically identify» en Business Suite. Limitaciones: «won't see or use automatic events reported via Conversions API in Meta surfaces until 2026»; «not available to business customers in the European Union, United Kingdom, or Japan» (Costa Rica no está excluida). Embedded Signup v2 «will be deprecated on October 15, 2026». | [developers.facebook.com — Automatic Events API](https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/automatic-events-api) `[OFICIAL]` |
| Herramientas que envían «lead calificado»/«compra» desde WhatsApp a Meta | **Sí, varias**, con mecanismos de reglas: **Wati** (marcás una plantilla como «lead calificado» o «compra» y su envío dispara el evento); **Kommo** (widget CAPI: mover el lead a la etapa «Calificado» o «Cerrado-Ganado» con monto; «Solo mejora los anuncios Click-to-Message»); **respond.io** (paso de workflow «Send Conversions API Event», detecta el `ctwa_clid` solo; eventos Lead y Purchase); **Chatfuel** (umbral de calificación por preguntas; artículo 2026-09-15); **Chatty** (Qualified Lead/Purchase desde el CRM); **Tintim** (frase gatillo/Kanban/«Inspetor»); **Infobip**, **360dialog**, **AWS End User Messaging** (`LeadSubmitted` con `ctwa_clid`). | [wati.io](https://www.wati.io/click-to-whatsapp-ads/); [kommo.com CAPI](https://www.kommo.com/es/recursos/apps-de-mensajeria/capi-configurar/); [respond.io help](https://respond.io/help/workflows/step-send-conversions-api-event); [chatfuel.com, 2026-09-15](https://chatfuel.com/blog/whatsapp-conversions-api-ctwa-ads); [letschatty.com](https://letschatty.com/); [infobip docs](https://www.infobip.com/docs/integrations/meta-ads-reporting-for-business-messaging); [AWS docs](https://docs.aws.amazon.com/social-messaging/latest/userguide/conversions-api.html) `[PROPIO/OFICIAL]` |
| Detalle técnico útil | Un proyecto abierto reporta que Meta rechaza el evento genérico «Lead» para WhatsApp y acepta `LeadSubmitted`/`QualifiedLead`; guarda un libro de eventos enviados para no duplicar. `[TERCEROS, probado contra la API según el autor]` | [github.com/oussch702/whatsapp-conversions-api](https://github.com/oussch702/whatsapp-conversions-api) |
| Reportes de anuncios con IA | Sí, para métricas de anuncios: AdAmigo (agente en chat), Madgicx («Official Meta Business Partner»), Hyros (atribución). Ninguno conecta con el contenido de conversaciones de WhatsApp. | [adamigo.ai](https://www.adamigo.ai/); [madgicx.com](https://madgicx.com/) `[PROPIO]` |
| El propio Meta vendiendo el bot | **Meta Business Agent** (anunciado en Conversations 2026, Londres; artículo 2026-06-04): atiende, recomienda, agenda, califica y cierra en WhatsApp, Messenger e Instagram; «Free at launch», suscripciones pagas «en los próximos meses». | [marketing4ecommerce.net, 2026-06-04](https://marketing4ecommerce.net/en/meta-business-agent/) `[TERCEROS]` |

### 5.2 Lo que no encontré (los huecos reales)
1. **Un servicio —no un SaaS— que venda «te digo qué anuncio trae a los que compran» como mecanismo con nombre, en español.** Busqué con «API de conversiones» + WhatsApp + agencia + «leads calificados» en ES/MX/CO/AR y no apareció ninguna agencia que lo prometa; aparecen proveedores de software (Chatty, Kommo, Wati) e integradores (Latin Meta Services, iTechDev). Alkimista habla de «trazabilidad» y GTM server-side, pero no de conversaciones.
2. **Una IA que lea la conversación completa y decida calidad y valor sin humano ni frase gatillo.** Lo más avanzado que encontré: Tintim (batch diario + aprobación humana + solo texto, según competidor), Chatfuel (umbral por preguntas), Wati (plantilla), Kommo (etapa manual), Chatty (etapa en CRM). Meta lo hace con regex + NLP solo para «lead» y «compra», no para «encaja con la oferta» ni «cuánto vale».
3. **Un reporte semanal que una anuncio → conversación → llamada → venta, escrito por IA y leído por el dueño.** GrowthMarketer tiene «weekly decisions» y «Growth Memory» por escrito, pero para cuentas de US$50K+/mes y sin WhatsApp. En español no lo encontré.
4. **Costa Rica:** ninguna agencia encontrada vende atribución de conversaciones, CAPI para WhatsApp o devolución de señales; venden chatbots (Nubo, Magnetis, SmartizaLatam, Automaxia) y pauta (Peper, Click Digital) por separado.
5. **Pago por resultado en español.** Ninguno de los actores en español publica precio por cita calificada; LeadsNow (Australia) sí.
6. **Casos auditados con consentimiento y ventana cerrada en LatAm.** Solo Helix («30 días auditados») y HazloFácil («caso real con consentimiento», 9 sep–8 oct 2026) en España. En LatAm, Clienteli publica un caso con fechas (11–30 sep 2026) de un cliente de ventas, no de high-ticket.

---

## 6) Qué dicen los clientes

### 6.1 Reddit (hilos leídos completos)
**r/agency — «Has anyone running an AI automation agency?»** (enero 2024; comentarios hasta 2025). URL: https://www.reddit.com/r/agency/comments/198xcw8/has_anyone_running_an_ai_automation_agency/ `[TERCEROS]`
- rtguk: «We went down this route and, quite honestly, it's nowhere near as attractive as the YouTubers make it. The market is small, adoption is tough and there are still alot of negative perceptions about AI in the market. We spent 9 months last year really hitting this hard and went nowhere.»
- rtguk (más abajo): «sell the solution not the tech. Clients typically don't understand AI, so just sell the incredible benefits they will have.»
- mtbcouple: «Don't look at new tech and force a solution because it's shiny and a bunch of YouTube gurus are claiming you can make 6 figures a month after buying their course. Provide real value.»
- Inept-Expert: «The maintenance and fixing issues that crop up is the main problem I think. If one of your automations goes down for a pharmacy client on a Sunday at 1am, it's an absolute emergency.»
- SprayAnnual5726 (el único con anuncios): «I started an ai agency mainly marketed through Meta ads selling SAAS and ai employees to car dealers. First month we did 30k cost per booked call at $23 - the lowest of 3 split tested videos. Started with static creatives getting a $48 cost per booked call.» (cifras propias, sin verificar)
- Melodic-Ad-1248: revende recepcionistas IA «for $55 from AI Front Desk and resell them for around $255 per month» (el margen del «wrapper»).
- Pretend_Guide2323: «DONT join Liam Evans network community. He scammed me and is not replying to my messages anymore.» (Liam **Evans**, no Ottley; acusación sin verificar)
- ggildner: «An AI automation agency only works if you can provide value that a user can't get from doing it themselves.»

**r/automation — «Is starting an AI agency (AAA) a good idea?»** (2024-09-30; comentarios hasta hace 27 días). URL: https://www.reddit.com/r/automation/comments/1ft3wvn/is_starting_an_ai_agency_aaa_a_good_idea/ `[TERCEROS]`
- OP: «business owners already know how easy it is to set up an AI agent. Do you still think it's a good market, or is it already saturated?»
- CurlyAce84: «The "AI automation agencies" I've seen are all 20yo YouTubers who make more money off of convincing others of this business model rather than actual client delivery work.»
- Wow-zer: «it's really giving me 2018's Drop Shipping/Social Media Marketing Agency guru vibes… If the agent gets a lead, have it save that lead in their CRM and trigger an automation that handles follow-up, appointment booking, etc.»
- Plus_Worldliness_431: «Only if you anchor it to real business outcomes like pipeline or support deflection. The tool stack is the easy part. What clients pay for is judgment and distribution.»
- 99_Silverado: «a large part of the value still is… the human element of engaging with a business and it's stakeholders to understand their business/challenges.»
- sundeckstudio (hace 27 días): «niche down into something that you do with AI. AI is merely a 'tool'… What you do with it, becomes your 'service'.»
- Key-Reporter-515 sobre un «AI Agency Starter Kit» promocionado en el hilo: «I just wasted $1 to get early access, only to get a message saying i'll be emailed in several weeks when they have a product to ship. Very misleading.»

Otros dos hilos (r/n8n «Are AI and automation agencies lucrative…», r/automation «Anyone having success with an AI automation…») devolvieron el muro «Prove your humanity» y no se pudieron leer.

### 6.2 Trustpilot y FTC
- **Air.ai** — TrustScore 1,2/5, 83 reseñas (98 % de 1 estrella), ninguna marcada «Verified». Quejas: «I paid them $10,000. Requested a refund within the first week.» (Zane, 2025-01-17); «I lost $15,000 and they do not deliver their promise, they lied about their refund guarantee.» (Ryan Lugo, 2024-10-06); «There's no support at all and it's full of bugs.» (Kingdom Content Agency, 2025-07-05). La **FTC** demandó a Air AI Technologies y sus dueños el **2025-08-25**: alega promesas de recuperar «tens of thousands of dollars within days or months», garantías de reembolso de 2–3× la inversión «rarely honored», violaciones a la Telemarketing Sales Rule y a la Business Opportunity Rule, consumidores que pierden «as much as $250,000». Cita del director de la FTC: evitar que «the promise of new technology isn't misused as a means to mislead consumers». [Trustpilot](https://ca.trustpilot.com/review/air.ai); [FTC](https://www.ftc.gov/news-events/news/press-releases/2025/08/ftc-sues-stop-air-ai-using-deceptive-claims-about-business-growth-earnings-potential-refund) `[OFICIAL]`.
- **Leadscape.au** (agencia de pauta con «garantía» para coaches/agencias; web cerrada según Trustpilot) — 15 reseñas en 12 meses, ninguna verificada. Quejas: «the requirement to spend $300 per day on ads to qualify for that guarantee» no fue informado (Vinny FX, 2025-04-10); la garantía aplica solo con un «$10k/mo minimum program» no dicho antes, tras una llamada de venta de «an hour and a half» (Norman Hayman, 2026-01-09); «refundable deposit» usado para llevar a otra llamada y no devuelto (Jonathon, 2025-12-15); reembolso negado al parar por metas no cumplidas (Gabriel Matatov, 2026-01-27). A favor: «first of four agencies to deliver results, though only at the minimum guarantee level» (Jack Kees, 2025-11-15). [Trustpilot](https://ca.trustpilot.com/review/leadscape.au) `[TERCEROS]`.
- **Appointwise** (setter IA SaaS) — 4,3/5 con 101 reseñas. Quejas: «the bot quoted a $199/month program that his company doesn't offer» (John Lopez, 2026-08-31); «Appallingly bad support. Two days of waiting for something of substance, nothing.» (Ben M, 2026-05-21); «the product genuinely could be great - but inconsistency and a lack of adequate support is letting it down» (Nick, 2026-05-11); «The support team takes 2–3 hours to respond and then disappears» (CA Ajay, 2026-02-21). Elogios: «Lead response time is now instant» (Ben, 2025-06-24). [Trustpilot](https://dk.trustpilot.com/review/www.appointwise.io) `[TERCEROS]`.
- **HighDrop / Faceless CEO** (programas «hazlo con IA») — «no refunds at all» por mensaje de texto; cobros dobles de US$27 y US$227 por programas no pedidos; «no contract no guarantee in writing». [Trustpilot HighDrop](https://ca.trustpilot.com/review/highdrop.co); [Faceless CEO](https://ca.trustpilot.com/review/faceless.ceo) `[TERCEROS]`.
- **AAA Accelerator (Ottley)** — según reseña de terceros (2026-02-23): Trustpilot ≈500 reseñas, ≈4 estrellas; negativas: «Restrictive refund policy that puts all risk on the student», «The sales call felt pressured, with urgency tactics», «overpriced for what you get», proceso de reembolso «intentionally made difficult». El autor vende su propio negocio de lead gen en el mismo artículo. [marksinsights.com](https://marksinsights.com/liam-ottley-review/) `[TERCEROS]`.
- **España — «Setter Digital» (curso de appointment setting):** denuncias de deuda con financiera no avisada: «Te hacen aceptar una política de empresa sin avisarte que adquieres una deuda con una financiera». [alarmadefraude.com](https://www.alarmadefraude.com/scam/view/662309) `[TERCEROS, no verificado]`. No encontré reseñas de agencias de «citas garantizadas con IA» en español.

### 6.3 Resúmenes de terceros (secundarios, con interés comercial)
- Ciela (2026-07-02): lo que mata un trato es «the prospect not believing the automation will work for their specific business»; churn cuando «The automation does not move a number the client cares about»; «Burnout comes from breadth»; «the space is drowning in people selling the idea of starting an agency rather than the service itself». [ciela.ai](https://ciela.ai/blogs/is-starting-an-ai-automation-agency-worth-it-reddit) `[TERCEROS]`.
- Otro resumen cita como quejas recurrentes: «vague scoping, retainers that outlive the work, tools rented back to you at a markup, and 'automations' that are a Zapier zap someone charged four figures for». `[NO VERIFICADO: fragmento de búsqueda]`.
- Cannatract («Reddit's Verdict») no cita hilos ni usuarios; es la propia agencia opinando. [cannatract.co](https://cannatract.co/ai-automation-agency-reddit).

### 6.4 Las promesas que se rompen (síntesis)
1. Garantía que depende de un gasto en pauta no dicho (Leadscape).
2. Reembolso prometido y no pagado (Air.ai, HighDrop).
3. El bot dice cosas que el negocio no ofrece (Appointwise).
4. Soporte que tarda horas y se va (Appointwise, Air.ai).
5. Mucho dinero adelante sin entregable definido (Air.ai; «retainers that outlive the work»).
6. Vender el modelo en vez del servicio (Reddit sobre los YouTubers).
7. Mantenimiento: cuando se cae un domingo a la 1 a. m. es emergencia (Reddit).

---

## 7) Ideas para Hans (todas son hipótesis; cada una con la fuente que la inspira)

1. **Nombrar el mecanismo por el circuito, no por la IA.** Algo del tipo «circuito cerrado: anuncio → conversación → llamada → señal a Meta». Inspirado en Chatfuel («Closing the Loop»), Chatty («deja de optimizar por 'mensaje' y empieza a optimizar por venta») y GrowthMarketer («Signal Audit»). Hipótesis: el nombre sobre el proceso envejece mejor que «con IA».
2. **Prometer el proceso y no el resultado, por escrito.** Copiar la postura de GrowthMarketer («We can promise the process on this page, not the result»; «nothing that moves money runs without approval by default»). Es exactamente la regla del proyecto y, frente a Leadscape y Air.ai, es una diferencia que el cliente quemado entiende.
3. **Entrada = auditoría de señales, no «llamada gratis» ni demo del bot.** GrowthMarketer responde por escrito en 48 h sin calendario; Alkimista regala una calculadora de «pérdida de tracking»; LeftClick audita el embudo. Hipótesis: una «auditoría de lo que Meta no está viendo de tus conversaciones» calza con la marca técnica y filtra curiosos.
4. **Un caso con ventana cerrada y consentimiento, con cifras de proceso.** Como Helix («30 días auditados», ~100 leads: % que responde, mediana de respuesta, % con cita) y HazloFácil («caso real con consentimiento», 88 conversaciones → 29 citas, < 7 €/cita). Nunca ingresos. Hipótesis: el primer cliente de Hans (o su propia campaña) se documenta así desde el día uno.
5. **Contenido que muestre el sistema operando en una cuenta real.** Single Grain: «Proprietary AI systems already running in client accounts — not pitched in decks»; LeftClick: «We don't just advise. We build». Hipótesis: reels donde el pipeline lee una conversación, la etiqueta y aparece el evento en el Events Manager; eso es congruente con una marca que habla de sistemas, Claude y repositorios, y vende adquisición sin decir «agencia de IA».
6. **Enseñar el método y vender el servicio en dos puertas distintas.** Ottley y Saraev enseñan en YouTube y venden la agencia aparte; los creadores en español solo enseñan «cómo montar tu agencia». Hipótesis: Hans puede enseñar el circuito (para otros media buyers o dueños técnicos) sin caer en el embudo de «agencia de IA en 90 días» que Reddit asocia a gurús.
7. **Precio con dos piezas: alcance fijo + pieza variable sobre lo medible.** LeftClick (precio fijo, retainer opcional) y LeadsNow (US$40–220 por cita calificada; «if the appointment does not land qualified, you do not pay»). Referencias de mercado para no competir con el bot barato: Clienteli ≈US$35–89/mes, NexoSmart US$1–2K setup + US$100–400/mes, Helix 297–1.497 €/mes. Hipótesis: el precio de Hans se ancla en el valor de la llamada y el gasto en pauta, no en el agente.
8. **Garantizar solo lo que controla.** Helix (7 días + 30 días), CallSetter («Book More in 30 Days or You Do Not Pay», medido contra el mes anterior en los registros). Hipótesis: «si en 30 días no puedo decirte qué anuncio trae a los que compran, ese mes no se cobra», sin tocar ingresos ni cantidad de clientes (ver §8.1).
9. **Usar las primitivas de Meta como prueba de seriedad.** Activar «Automatic Events» (opt-in) y enviar `QualifiedLead`/`Purchase` con `ctwa_clid`; Meta mismo dice que eso habilita «purchase optimization for ads that click to WhatsApp». Hipótesis: «lo que Meta construyó y casi nadie en Costa Rica cableó» es un argumento técnico que un dueño entiende.
10. **No construir todo: integrar o asociarse.** Chatty (partners +90 agencias, 10 % recurrente), Tintim (reventa «desde 65 %»), Kommo/Wati/respond.io ya envían eventos. Hipótesis: Hans pone la lectura con IA y el criterio encima de un CRM que ya resuelve `ctwa_clid` y CAPI, y lo que aprenda lo vende después a otros media buyers (el partner program de Chatty muestra que ese canal existe).

---

## 8) Riesgos

1. **Políticas de anuncios de Meta sobre resultados y ganancias.** La página «Unrealistic Outcomes» del Transparency Center aparece listada en búsqueda (cubre salud, pérdida de peso y «economic opportunity», con ejemplos de «unrealistic results within set timeframes») pero devolvió 404 en todas sus versiones (en, en-gb, de-de, es-la) el 2026-10-11, así que no pude leer el texto. La de «Unacceptable Business Practices» sí abrió: prohíbe «deceptive pricing, unauthorized endorsements, and guaranteed investment returns» y exige cumplir el estándar de prácticas comerciales prohibidas. Lectura práctica de un tercero (Stackmatix, 2026-09-02): «you cannot imply a specific financial result from a product, service, or opportunity»; «Guaranteed $5k per month» se rechaza; recomendación «show the work, not the wallet». **Implicación:** las garantías del §7 van al contrato y a la página, no al anuncio; nada de «X clientes garantizados en 30 días» ni cifras de ingresos en creativos. Fuentes: [transparency.meta.com — Unacceptable Business Practices](https://transparency.meta.com/policies/ad-standards/fraud-scams/unacceptable-business-practices/) `[OFICIAL]`; [URL listada de Unrealistic Outcomes (404)](https://transparency.meta.com/policies/ad-standards/deceptive-content/unrealistic-outcomes); [stackmatix.com, 2026-09-02](https://www.stackmatix.com/blog/meta-ads-income-claims-policy) `[TERCEROS]`.
2. **Política de WhatsApp Business Platform sobre IA (vigente desde 2026-01-15).** «Meta will prohibit general-purpose AI chatbots on the WhatsApp Business Platform (API)»; el bot tiene que ser «ancillary to a legitimate business service»; «Bookings and sales» están permitidos. Para Hans juega a favor (bots de un negocio concreto), pero cualquier agente «genérico» o revendido como asistente general queda fuera. Fuente: [respond.io, 2025-10-27](https://respond.io/blog/whatsapp-general-purpose-chatbots-ban) `[TERCEROS, cita los términos]`.
3. **Meta regala la pieza barata.** Business Agent (junio 2026, gratis al lanzar) atiende, califica, agenda y cierra; Automatic Events detecta lead y compra con NLP; Advantage+ automatiza la pauta. Un blog de traffickers lo resume: el que «solo configura campañas y sube creativos corre más riesgo». **Implicación:** el valor de Hans no puede estar en el bot ni en «subir la campaña», sino en el criterio, la lectura de calidad y el reporte. Fuentes: [marketing4ecommerce.net, 2026-06-04](https://marketing4ecommerce.net/en/meta-business-agent/); [Automatic Events API](https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/automatic-events-api) `[OFICIAL]`; [felipevergara.co](https://felipevergara.co/blogs/freelance/trafficker-digital-que-es-y-que-hace/) `[TERCEROS]`.
4. **Saturación del «con IA» y desconfianza del comprador.** 335.900 miembros en el Hub de Ottley; en español, canales que prometen «10k/mes», «100k/mes» y «10–20 k€ en < 90 días»; Reddit: «2018's Drop Shipping/SMMA guru vibes», «business owners already know how easy it is to set up an AI agent». **Implicación:** evitar las palabras «agencia de IA» y «automatización» en el nombre del servicio; vender por el resultado que el dueño reconoce (conversaciones con dueños que encajan) y por el proceso.
5. **«AI-washing» y reglas de oportunidad de negocio.** La FTC lanzó «Operation AI Comply» en septiembre 2024 y seguía activa en octubre 2025; el caso Air AI (2025-08-25) castiga promesas de ganancias y reembolsos no honrados a pequeños negocios. Costa Rica no está bajo la FTC, pero el patrón (promesa de retorno + garantía de reembolso + licencias para revender) es el que destruye reputación en cualquier mercado. Además, leer conversaciones de clientes con un modelo exige consentimiento y cumplimiento de la ley local de datos; una guía de WhatsApp marketing lo recuerda: la comunicación debe «contar con el consentimiento del usuario, cumpliendo con las políticas de Meta y las leyes de protección de datos locales». Fuentes: [beneschlaw.com (Operation AI Comply, 2025-10)](https://www.beneschlaw.com/insight/one-year-in-ftcs-operation-ai-comply-continues-under-new-administration-signaling-enduring-enforcement-focus.html); [FTC Air AI](https://www.ftc.gov/news-events/news/press-releases/2025/08/ftc-sues-stop-air-ai-using-deceptive-claims-about-business-growth-earnings-potential-refund) `[OFICIAL]`; [nexgenpixels.com](https://www.nexgenpixels.com/blog/automatizacion-marketing-whatsapp-guia-2026) `[TERCEROS]`.
6. **Dependencia técnica de Meta.** CAPI para mensajería exige acceso avanzado a dos permisos, un tier de Marketing API (500 llamadas exitosas en 15 días según el banner actual) y Embedded Signup o Facebook Login for Business; Embedded Signup v2 se desactiva el 2026-10-15; Meta no deduplica eventos; con API oficial, Tintim reconoce que «não há como fazer a captura nativa dos dados» y usa mensajes rastreables. **Implicación:** el circuito tiene costo de construcción y de mantenimiento (recordar el «domingo a la 1 a. m.» de Reddit) que hay que presupuestar antes de prometerlo. Fuentes: [CAPI Business Messaging](https://developers.facebook.com/docs/marketing-api/conversions-api/business-messaging) `[OFICIAL]`; [Tintim base de conocimiento](https://tintim.app/base-de-conhecimento/integracao-do-whatsapp-com-o-tintim-via-api-oficial-como-configurar-o-rastreio-correto-de-campanhas-de-mensagem/) `[PROPIO]`.

---

## 9) Fuentes (todas vistas el 2026-10-11; fecha de publicación entre paréntesis cuando la página la indica)

### Documentación oficial (Meta, FTC)
- https://developers.facebook.com/docs/marketing-api/conversions-api/business-messaging — Conversions API for Business Messaging (eventos, `ctwa_clid`, requisitos, optimización por compra en CTWA).
- https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/automatic-events-api — Automatic Events API (regex + NLP, opt-in, exclusiones EU/UK/Japón, deprecación Embedded Signup v2 2026-10-15).
- https://transparency.meta.com/policies/ad-standards/fraud-scams/unacceptable-business-practices/ — Unacceptable Business Practices.
- https://transparency.meta.com/policies/ad-standards/deceptive-content/unrealistic-outcomes — Unrealistic Outcomes (listada en búsqueda; 404 en en, en-gb, de-de y es-la al intentar leerla).
- https://www.ftc.gov/news-events/news/press-releases/2025/08/ftc-sues-stop-air-ai-using-deceptive-claims-about-business-growth-earnings-potential-refund — FTC vs Air AI (2025-08-25).
- https://www.beneschlaw.com/insight/one-year-in-ftcs-operation-ai-comply-continues-under-new-administration-signaling-enduring-enforcement-focus.html — Operation AI Comply, un año después (2025-10).

### Actores globales (inglés)
- https://www.morningside.ai/ — Morningside AI.
- https://www.skool.com/learn-ai — AI Automation Agency Hub (335,9 k miembros).
- https://marksinsights.com/liam-ottley-review/ — reseña del AAA Accelerator (2026-02-23).
- https://leftclick.ai/ — LeftClick AI (Nick Saraev).
- https://growthmarketer.com/ — GrowthMarketer (Robbie Jack).
- https://www.singlegrain.com/ — Single Grain (Eric Siu).
- https://omnifusion.ai/ — OmniFusion AI.
- https://leadsnow.ai/coaches/ — LeadsNow AI.
- https://www.imperiumacquisition.com/ — Imperium Acquisition (Charlie Morgan).
- https://ippei.com/build-release-ai/ — reseña de Build & Release AI (Serge Gatari).
- https://whop.com/joined/clientacquisitionio/products/growth-creator-incubator-6b/ — precios en Whop de ClientAcquisition.io.
- https://www.askneedle.com/ — Needle.
- https://www.adamigo.ai/ — AdAmigo.ai.
- https://callsetter.ai/pricing — CallSetter.
- https://www.trysetter.com/pricing — Setter AI.
- https://setor.ai/ — Setor AI.
- https://www.appointwise.io/ — Appointwise.
- https://www.acquisync.agency/ — AcquiSync.
- https://hyros.com/pricing-ai-tracking — Hyros.
- https://pricingsaas.com/companies/icon — precios de Icon (terceros).
- https://www.eesel.ai/en/blog/arcads-ai-pricing — precios de Arcads (terceros).
- https://madgicx.com/ — Madgicx.
- https://creatify.ai/es/blog/introducing-ai-media-buyer-the-ai-agent-that-runs-your-ads — Creatify «AI Media Buyer».

### Actores en español, LatAm y Brasil
- https://gethelix.es/ — Helix (España).
- https://alkimistadigital.com/ — Alkimista Digital (Argentina).
- https://letschatty.com/ — Chatty (Argentina).
- https://www.nexosmart.com.ar/soluciones/agente-ia-leads-whatsapp/ — NexoSmart (Argentina/España; actualizado 2026-10).
- https://impulsodigital.io/ — Impulso Digital (Colombia).
- https://scaliamkt.com/ — Scalia Marketing (México).
- https://clienteli.com.co/ — Clienteli (Colombia).
- https://www.soyagentia.com/ — SoyAgentia (Colombia).
- https://pepercr.com/ — Peper La Agencia (Costa Rica).
- https://nubocr.com/ — Nubo (Costa Rica).
- https://www.magnetislab.com/precio-chatbot-whatsapp-costa-rica — Magnetis Lab (Costa Rica; 2026-06-16).
- https://www.smartizalatam.com/ , https://automaxia.com/ , https://runia.ar/cr/chatbot-whatsapp , https://togrowagencia.com/servicios-de-ia-para-whatsapp-en-san-jose/ , https://clickdigitalcr.com/en/ — otros proveedores en Costa Rica (solo búsqueda).
- https://beoffon.com/index.html — BEOFFON (España).
- https://hazlo-facil.es/ — HazloFácil Citas (España).
- https://beyondthebig.com/ — Beyond The Big (España).
- https://flowmatic.es/ y https://flowmatic.es/automatizacion/leads-meta-ads-ia/ — Flowmatic (España).
- https://sinteqia-landing.webflow.io/ — Sinteqia.
- https://agenciaiasolutions.com/captar-clientes-con-ia/ — Agencia IA Solutions (España).
- https://www.javadex.es/ — Javadex (España).
- https://www.upliora.es/comparativas/mejores-canales-youtube-ia-espana-2026 — lista de canales (conflicto de interés).
- https://iaenaccion.com/sobre-nosotros/ — Xavier Mitjana.
- https://www.youtube.com/@agustinmedinaIA , https://www.youtube.com/@deniscorral , https://www.youtube.com/@NexumAI , https://www.youtube.com/@condeclaudioad — canales en español (autoría confirmada por oEmbed de YouTube; descripciones no leídas).
- https://creatordb.app/creatorstats/agustinmedinaia/ — estadísticas de terceros de Agustín Medina.
- https://lilys.ai/es/notes/ai-automation-20260304/ai-agency-32k-month-free — resumen de un video de Emprende Aprendiendo con Agustín Medina (claim de 32.000 €/mes, no verificado).
- https://www.tintim.app/ — Tintim (Brasil).
- https://tintim.app/base-de-conhecimento/integracao-do-whatsapp-com-o-tintim-via-api-oficial-como-configurar-o-rastreio-correto-de-campanhas-de-mensagem/ — Tintim con API oficial.
- https://chatfuel.com/blog/chatfuel-vs-tintim — Chatfuel vs Tintim (2026-08-17; competidor).
- https://utmpixel.com/ferramentas/utmify — UTMify (terceros).
- https://latinmetaservices.com/ , https://itechdev.com.mx/en/servicios/whatsapp-business-api , https://www.dinolabs.dev/agentes-ia — integradores en LatAm (solo búsqueda).
- https://orchestaai.io/soluciones/agentes-ia-whatsapp/ , https://holosdigital.com/agentes-ia/ , https://uniamos.com/whatsapp-business-ia , https://porcontar.com/agentes-de-ia-whatsapp-colombia/ — agentes IA WhatsApp en Colombia/México (solo búsqueda).
- https://www.digitalnovasas.com/es — DigitalNova (Colombia; solo búsqueda).
- https://agenciaia.us/ , https://agenciaia.ai/ , https://automatizapyme.com/automatizacion-con-ia/agencia — «agencia IA» genéricas (solo búsqueda).

### Herramientas que cierran WhatsApp → Meta
- https://chatfuel.com/blog/whatsapp-conversions-api-ctwa-ads — Chatfuel, «Closing the Loop» (2026-09-15).
- https://respond.io/help/workflows/step-send-conversions-api-event — respond.io, paso «Send Conversions API Event».
- https://www.wati.io/click-to-whatsapp-ads/ y https://www.wati.io/en/blog/set-up-click-to-whatsapp-ads/ — Wati.
- https://www.kommo.com/es/recursos/apps-de-mensajeria/capi-configurar/ y https://www.kommo.com/whatsapp/whatsapp-conversion-api/ — Kommo.
- https://www.infobip.com/docs/integrations/meta-ads-reporting-for-business-messaging — Infobip.
- https://docs.aws.amazon.com/social-messaging/latest/userguide/conversions-api.html — AWS End User Messaging Social.
- https://docs.360dialog.com/360pilot/integrations-and-optimization/meta-pixel-and-ctwa-optimization — 360dialog.
- https://github.com/oussch702/whatsapp-conversions-api — validador abierto de eventos CAPI para WhatsApp.
- https://www.letschatty.com/blog/trackeo-completo-en-whatsapp-c%C3%B3mo-usar-utms-y-medir-eventos-con-la-api-de-conversiones-de-meta — Chatty, guía de trackeo.
- https://cangrejodigital.com/meta-ads/campanas-whatsapp-meta-ads/ — guía en español sobre CTWA + CAPI.
- https://www.abcsales.ai/resources/news/meta-conversion-api-whatsapp — ABC Sales AI.
- https://metricfixer.com/publications/analytics-conversion-tracking/track-click-to-whatsapp-ads-campaign-ad-creative-without-website — atribución CTWA sin web.
- https://www.leaddistro.ai/blog/meta-conversions-api-lead-generation — CAPI para agencias de pago por lead.
- https://salesgem.io/blog/conversion-leads-optimization-crm/ — Conversion Leads optimization.

### Quejas y reseñas
- https://www.reddit.com/r/agency/comments/198xcw8/has_anyone_running_an_ai_automation_agency/ — r/agency (2024-01; leído completo).
- https://www.reddit.com/r/automation/comments/1ft3wvn/is_starting_an_ai_agency_aaa_a_good_idea/ — r/automation (2024-09-30; leído completo).
- https://www.reddit.com/r/n8n/comments/1je8p3a/are_ai_and_automation_agencies_lucrative/ y https://www.reddit.com/r/automation/comments/1iuwnuh/anyone_having_success_with_an_ai_automation/ — no se pudieron leer (captcha).
- https://ca.trustpilot.com/review/air.ai — Air.ai.
- https://ca.trustpilot.com/review/leadscape.au — Leadscape.
- https://dk.trustpilot.com/review/www.appointwise.io — Appointwise.
- https://ca.trustpilot.com/review/highdrop.co y https://ca.trustpilot.com/review/faceless.ceo — HighDrop, Faceless CEO.
- https://www.alarmadefraude.com/scam/view/662309 — «Setter digital» (España).
- https://ciela.ai/blogs/is-starting-an-ai-automation-agency-worth-it-reddit — Ciela (2026-07-02; vendedor).
- https://ciela.ai/blogs/ai-automation-agency-scam-reddit — Ciela, «scam» (vendedor).
- https://cannatract.co/ai-automation-agency-reddit — Cannatract (agencia; sin citas de Reddit).

### Políticas, mercado y contexto
- https://respond.io/blog/whatsapp-general-purpose-chatbots-ban — política de WhatsApp sobre chatbots de propósito general (2025-10-27).
- https://marketing4ecommerce.net/en/meta-business-agent/ — Meta Business Agent (2026-06-04).
- https://www.stackmatix.com/blog/meta-ads-income-claims-policy — lectura práctica de income claims (2026-09-02).
- https://www.nexgenpixels.com/blog/automatizacion-marketing-whatsapp-guia-2026 — guía WhatsApp marketing (consentimiento).
- https://felipevergara.co/blogs/freelance/trafficker-digital-que-es-y-que-hace/ y https://fabipers.com/desafios-trafficker-digital-ia/ — el trafficker frente a la IA de Meta (opinión).
- https://fabipers.com/mejores-traffickers-digitales-colombia/ — pauta mínima sugerida en Colombia.
- https://engrana.es/agenda-de-citas-por-whatsapp — pauta mínima sugerida en España.
- https://taskip.net/ai-automation-agency-pricing/ y https://tribuclaw.com/blog/montar-agencia-automatizacion-ia/ e https://iasincodigo.com/agencia-automatizacion-ia/ — guías de precios de agencias de automatización.
- https://setsmart.io/blog/best-ai-setters y https://www.revenueflow.com/blog/ai-appointment-setter — comparativas de setters IA (vendedores).
- https://www.marketingbrew.com/stories/2026/04/07/meta-ai-ad-creation — Meta y la creación de anuncios con IA (2026-04-07).

### Lo que no pude verificar
- El texto de la política «Unrealistic Outcomes» de Meta (404 en todas las versiones).
- Dos de los cuatro hilos de Reddit (captcha) y cualquier hilo de r/Entrepreneur (la búsqueda no los devolvió).
- Precios de Single Grain, OmniFusion, Needle, Morningside, Peper, Nubo, Scalia, Impulso Digital, Beoffon, Beyond The Big (no públicos).
- Las cuentas de Instagram en español (no se pueden abrir sin sesión); los datos vienen de fragmentos de búsqueda.
- Las promesas de ingresos de los videos en español (solo títulos; las descripciones no se cargaron).
- Cómo funciona por dentro el «Inspetor de Vendas» de Tintim (fuente: un competidor).
- Si Leadsales o Simla.com envían eventos a Meta (no encontré documentación); Kommo, Wati y respond.io sí.
- Media Buyers HQ / mediabuyers.ai (sin resultados de búsqueda; la web no respondió).
- Todas las cifras marcadas `[PROPIO]` (ROAS, porcentajes, cantidad de clientes).
