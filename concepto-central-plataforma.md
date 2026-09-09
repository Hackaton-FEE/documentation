# Idea Central y Propuesta: Aplicacion Movil de Defensa de Reputacion, Desindexacion y Borrado de Huella Digital

> **Documento Central de Trabajo:** Este archivo sirve como la propuesta rectora y arquitectura conceptual del proyecto. Ha sido ajustado formalmente para conceptualizar la solucion como una **Aplicacion Movil (iOS / Android)**, aprovechando las capacidades nativas del smartphone (Share Sheet, biometria, camara, push notifications y computo local zero-knowledge).

---

## 1. El Problema Real del Usuario Final y la Asimetria de Poder

Hoy en dia, un individuo común o un profesionista enfrenta una vulnerabilidad abrumadora:
1. **Exposicion Involuntaria en el Smartphone:** En mas del 90% de los casos, la victima descubre una filtracion personal (*doxxing*), fotos/videos no consentidos o campanas de difamacion mientras navega en redes sociales (Instagram, TikTok, Facebook, X, WhatsApp) **directamente desde su telefono movil**.
2. **Dano Reputacional Inmediato:** Una busqueda en Google con contenido danino puede destruir la carrera profesional, las finanzas o la vida personal de una persona en cuestion de horas.
3. **El Calvario Burocratico (Dias a Semanas):**
   * Las grandes plataformas tecnologicas (**Big Tech**) no cuentan con una "API publica de borrado" para usuarios.
   * Disenan laberintos de soporte (*dark patterns*), formularios ocultos y exigencias probatorias complejas.
   * La respuesta depende de revisiones humanas lentas, donde los reclamos comunes son ignorados o archivados sin explicacion clara.
4. **La Falencia de las Herramientas Actuales y el Origen de "Osisn't":**
   * Las herramientas OSINT tradicionales (como Sherlock o Holehe) solo le entregan al usuario una lista cruda o un volcado de consola: *"Estas en 80 sitios"*.
   * Esto genera **ansiedad sin solucion**: el usuario sabe que esta expuesto, pero no tiene el conocimiento tecnico ni legal para resolverlo.
   * **Nuestra Respuesta ("Osisn't"):** Una interfaz intuitiva y digestible que humaniza el OSINT, traduce los datos a un lenguaje comprensible, calcula un *Exposure Score* y ofrece botones de remediación directa (1-clic a JustDelete.me, cartas a data brokers y desindexación). Ver detalle completo en [`osisnt-interfaz-huella-digital.md`](./osisnt-interfaz-huella-digital.md).

---

## 2. Alineacion con los Valores de FEE y Universidad de la Libertad

* **Propiedad Privada del Nombre, Imagen y Datos (FEE):** La identidad y la reputacion de un individuo son parte indiscutible de su propiedad privada. Nadie tiene derecho a explotar, mercantilizar o difamar la imagen de una persona sin su consentimiento voluntario.
* **Soberania Individual frente a Monopolios (FEE):** Reequilibrar la balanza entre el ciudadano individual y las megacorporaciones tecnologicas o corredores de datos.
* **Innovacion Emprendedora y Resolucion Práctica (UL):** No conformarse con el diagnostico pasivo; construir una solucion orientada a la ejecucion, reduciendo procesos dolorosos de semanas a pocos clics gracias a la tecnologia.
* **Gestion del Riesgo y Antifragilidad (UL):** Dotar al usuario de herramientas directivas para gestionar su reputacion personal y mitigar crisis digitales como un verdadero lider.

---

## 3. Investigacion Técnica: ¿Como Funcionan Realmente los Procesos en Google y Meta?

Para disenar una herramienta de automatizacion, primero debemos entender las tripas operativas y legales de Google y Meta:

```mermaid
graph TD
    subgraph Origen del Contenido Dañino
        A[Sitio Web / Perfil de Meta / Foro] -->|Indexado por| B[Buscador Google (SERP)]
    end

    subgraph Proceso de Mitigación Dual
        C[1. Eliminación en Origen: Meta / Webmaster] -->|Takedown Legal / Reporte| A
        D[2. Desindexación en Google] -->|Resultados sobre ti / Outdated Content| B
    end

    E[Intermediario Automatizado / Agente Autorizado] -->|Acción Paralela| C
    E -->|Acción Paralela| D
```

### A. El Ecosistema de Google: Desindexacion vs. Eliminacion
Google **no es el dueno de Internet ni aloja el contenido de terceros**, solo lo indexa. Por ende, existen dos caminos obligados:

1. **Desindexacion Legal Directa (Google Legal Removal):**
   * Aplica para: Datos personales sensibles (Doxxing, INE/CURP/SSN, cuentas bancarias), imagenes explicitas no consentidas (NCII) y difamacion respaldada por legislacion local o mandatos judiciales.
   * *Mecanismo:* Se tramita mediante formularios especificos en `support.google.com/legal`.
   * *Por que tarda:* Google cuenta con equipos de cumplimiento legal que sopesan el "interes publico y libertad de expresion" frente al "derecho a la privacidad".
2. **Herramienta "Results about you" (Resultados sobre ti):**
   * Diseñada para usuarios individuales para solicitar el retiro de resultados que contienen telefonos, domicilios o correos.
   * *Limitacion:* Es un flujo manual asistido por app; no cuenta con API publica de consumo B2B/B2C.
3. **Herramienta de Contenido Desactualizado (*Remove Outdated Content Tool*):**
   * Si el contenido ya fue borrado de Facebook o de la web de origen pero sigue apareciendo en el *snippet* o cache de Google, se puede forzar al robot de Google a verificar el codigo `404/410` para purgar la URL de los resultados en 24-48 horas.

### B. El Ecosistema de Meta (Facebook e Instagram)
1. **Suplantacion de Identidad (*Impersonation*):**
   * Requiere someter un formulario aportando documento de identificacion oficial (ID con fotografia).
2. **Difamacion y Vulneracion de Derechos al Honor:**
   * Meta cuenta con el formulario especializado de *Defamation / Rights Violation*. Exige citar los articulos de ley del pais del afectado y el enlace exacto de la publicacion o comentario.
3. **Imagenes Intimas No Consentidas (NCII / Porno Venganza):**
   * Integracion con iniciativas como **StopNCII.org** y **Take It Down** (de NCMEC).
   * *Como funciona la tecnologia:* La imagen nunca se sube a los servidores; se genera un **hash criptografico local (perceptual hash / PhotoDNA)** en el dispositivo del usuario. Ese hash se comparte con Meta, Google, TikTok y Reddit para bloquear la subida o eliminar copias existentes en segundos.

---

## 4. ¿Como puede Intervenir un Intermediario? (El Modelo del "Agente Autorizado")

El cuello de botella de estos procesos es que estan deliberadamente disenados para cansar al usuario individual. Un intermediario de software puede intervenir mediante las siguientes figuras tecnicas y legales:

```mermaid
sequenceDiagram
    autonumber
    actor Usuario as Usuario Afectado
    participant Plataforma as Nuestra Herramienta (Intermediario)
    participant Meta as Meta / Facebook
    participant Google as Google Legal
    participant Brokers as Data Brokers (700+)

    Usuario->>Plataforma: Otorga Mandato Digital (LPOA / Agente Autorizado)
    Plataforma->>Plataforma: Preserva Evidencia Criptográfica (Hash + Screenshot + Timestamps)
    par Despacho Automatizado
        Plataforma->>Meta: Envío de Reclamo Formal de Difamación / Privacidad
        Plataforma->>Google: Solicitud de Desindexación por Doxxing / Retiro Legal
        Plataforma->>Brokers: Opt-Out Masivo amparado en GDPR / CCPA
    end
    Note over Plataforma: Monitoreo Activo de SLAs (Recordatorios a los 7 y 14 días)
    Plataforma-->>Usuario: Dashboard con Estado de Resolucion en Tiempo Real
```

### 1. La Figura Juridica: "Authorized Agent" y Poder Limitado (LPOA)
* Bajo normativas modernas como la **CCPA** (California Consumer Privacy Act) y el **Articulo 80 del GDPR** (y normativas analogas de proteccion de datos en Latinoamerica), una persona puede designar formalmente a un **"Agente Autorizado"** para que actue en su representacion.
* **El Intermediario Digital:** Al registrarse, el usuario firma electronicamente un mandato de representacion limitado (*Limited Power of Attorney* exclusivamente para la gestion de privacidad y derechos ARCO / eliminacion). Con este poder, la plataforma puede emitir notificaciones legales validas a nombre del afectado.

### 2. Preservacion Forense de la Evidencia (Paso Critico)
* Antes de reportar, el infractor suele borrar o modificar el contenido si sospecha algo, perdiendo la prueba.
* El intermediario realiza un **archivado forense automatico**:
  * Captura de pantalla certificada.
  * Extraccion de codigo fuente HTML y metadatos.
  * Hash criptografico (SHA-256) con sellado de tiempo (*timestamping*) para que tenga validez legal en caso de litigio.

### 3. Orquestador de Envio y Despacho Automatizado
* **Canales Directos a Registered Agents:** En lugar de utilizar los formularios web lentos que atienden bots, las empresas tienen direcciones de correo legales y agentes registrados dedicados a recepcion de notificaciones judiciales y reclamos DMCA/GDPR.
* El intermediario genera documentos formales con terminologia juridica precisa, anexando la evidencia forense y enviandolos via correo certificado / API de notificaciones legales.
* **Navegadores Headless Asistidos:** Para aquellos formularios que no tienen API y requieren completar campos web, el software utiliza automatizaciones (Playwright / Puppeteer) supervisadas por el usuario para pre-rellenar y enviar solicitudes complejas en segundos.

### 4. Motor de Seguimiento y Escalacion por SLAs
* La ley establece plazos maximos para que las empresas respondan (por ejemplo, 15 a 30 dias bajo legislaciones de privacidad).
* Si Meta o Google no responden en 7 dias, el intermediario envia automaticamente un recordatorio formal con advertencia de escalamiento a la autoridad de proteccion de datos correspondiente (ej. INAI en Mexico, AEPD en Espana, FTC en EE. UU.).

### 5. Verificador Continuo de Desindexacion
* Un bot en segundo plano monitorea periodicamente:
  * Codigo de respuesta HTTP de la URL infractora (verificando si ya es `404 Not Found` o `410 Gone`).
  * Consultas recurrentes a las SERPs (Search Engine Result Pages) de Google para certificar que el enlace ha sido desindexado.

---

## 5. Mapeo de Tecnologias y APIs Existentes (No reinventar la rueda)

Para construir una plataforma escalable y viable en tiempos de hackathon o desarrollo ágil, se deben apalancar herramientas y APIs ya consolidadas en dos frentes: **Legal/Logístico** y **Tecnológico**.

```mermaid
graph TD
    subgraph Ecosistema de APIs y Herramientas Existentes
        subgraph Frente Legal & Logístico
            L1[Firma de Mandato LPOA: Dropbox Sign / DocuSign / Mifiel]
            L2[Verificación de Identidad KYC: Stripe Identity / Veriff]
            L3[Notificación Certificada: Lob API / Correos Certificados eIDAS]
            L4[Directorio Legal DPO: datenanfragen/data / Privacy-Opt-Out]
        end
        subgraph Frente Tecnológico
            T1[Preservación Forense: OpenTimestamps en Bitcoin / Archive.today]
            T2[Auditoría SERP: SerpApi / ZenRows / ValueSERP]
            T3[Hashing Perceptual: imagehash Python / StopNCII / PhotoDNA]
            T4[Automatización Web: Playwright con Stealth Plugin]
            T5[Mapeo de Huella OSINT: Holehe / Sherlock / Maigret APIs]
        end
    end
```

### A. Apartado Legal y Logistico (APIs & Herramientas Existentes)

1. **Firma Electronica del Mandato Digital (LPOA):**
   * **Herramientas:** `Dropbox Sign API (HelloSign)`, `DocuSign API`, o `Mifiel API` (firma electrónica avanzada con constancia de conservación NOM-151 para México/Latam) / `eIDAS` para Europa.
   * **Funcion:** Permite que el usuario firme legalmente en su teléfono un poder de representación limitado (*Limited Power of Attorney*) en 15 segundos sin imprimir papeles.
2. **Verificacion de Identidad (KYC Anti-Abuso y Anti-Censura):**
   * **Herramientas:** `Stripe Identity API`, `Persona API` o `Veriff API`.
   * **Funcion:** Garantiza que quien solicita el retiro de una foto o dato es verdaderamente el titular legítimo, impidiendo que un atacante use la herramienta para sabotear o censurar a terceras personas.
3. **Despacho Legal Certificado (Notificaciones Fehascientes):**
   * **Herramientas:** `Lob API` (para envío físico automatizado de cartas certificadas legales a los Agentes Registrados de Meta y Google en EE.UU.) y proveedores de correo electrónico certificado con fe pública (ej. `Lleida.net API`, `Docaposte` o `Certified Mail APIs`).
   * **Funcion:** Entrega acuse de recibo legal vinculante que activa los plazos perentorios de respuesta legal (15 a 30 días) bajo amenaza de multas de los reguladores.
4. **Directorio Colaborativo de Data Brokers y DPOs:**
   * **Herramientas:** Base de datos de código abierto de `datenanfragen/data` y repositorio `The-Osint-Toolbox/Privacy-Opt-Out`.
   * **Funcion:** Directorio con más de 2,000 correos de contacto directo de Oficiales de Protección de Datos (DPO) y formularios de opt-out sin tener que investigar uno por uno.

### C. Superpoderes y Capacidades Nativas de la Aplicacion Movil (La Gran Ventaja Competitiva)

El giro hacia una **aplicacion movil nativa (iOS / Android)** transforma radicalmente la experiencia y resuelve el mayor obstaculo en situaciones de crisis:

1. **Integracion con el "Share Sheet" Nativo (Compartir en...):**
   * *El problema:* En la web, el usuario tiene que copiar un enlace largo en Instagram/TikTok, abrir un navegador, iniciar sesion y pegarlo.
   * *La solucion movil:* El usuario esta en Instagram, TikTok o Facebook, ve el contenido difamatorio, toca **"Compartir" -> Selecciona el icono de la App**.
   * Mediante una extension nativa (*iOS Share Extension* / *Android Send Intent*), la app intercepta la URL al instante, extrae el identificador del post y activa el caso sin salir de la red social.
2. **Zero-Knowledge Image Hashing Local (Privacidad Absoluta):**
   * Cuando una persona es victima de imagenes intimas no consentidas (NCII) o extorsion, **siente terror de subir la foto a la nube de un tercero**.
   * En la app movil, el algoritmo de *Perceptual Hashing* (pHash / PhotoDNA) se ejecuta **directamente en el procesador del smartphone**. La imagen sensible nunca sale del dispositivo; solo viaja el hash matematico cifrado para cotejar y solicitar el bloqueo.
3. **Firma Tactil y Biometria In-App (LPOA en 15 segundos):**
   * Firma del poder limitado (LPOA) deslizando el dedo o con Face ID / Touch ID mediante `expo-local-authentication` o `react-native-signature-canvas`.
4. **Push Notifications para Seguimiento de SLAs:**
   * Notificaciones en tiempo real directo al lockscreen:
     * ⏱️ *"Meta ha recibido tu requerimiento legal. Plazo perentorio: 15 dias."*
     * ⚠️ *"Dia 7: Recordatorio formal enviado al Agente Registrado de Google."*
     * ✅ *"¡Exito! La URL ha sido purgada del indice de Google (confirmado por SERP)."*

---

## 6. Modulos Propios que SI se tienen que Implementar (Custom Built)

Todo el software propio a programar se centrará en la **orquestación, la lógica de negocio, la experiencia móvil y la preservación forense**:

```mermaid
graph TD
    subgraph Experiencia Móvil del Usuario
        A[Navegando en Instagram/TikTok/X] -->|Botón Compartir / Share Sheet| B[App Móvil: Interceptor de Enlace]
        B --> C[Firma Táctil LPOA + Face ID]
        C --> D[Hashing Local en Dispositivo Zero-Knowledge]
    end

    subgraph Backend & Workers
        D --> E[Módulo Evidence Vault: Captura & OpenTimestamps]
        E --> F[Módulo Legal Synthesizer: Plantilla Jurídica Automática]
        F --> G[Módulo Big Tech Dispatcher: Playwright & Correo Legal]
        G --> H[Módulo SLA Watchdog: Seguimiento a 7, 14, 30 días]
        H --> I[Módulo SERP Sentinel: Auditor de Desindexación]
    end

    I -->|Push Notification en Tiempo Real| J[Pantalla de Bloqueo del Usuario]
```

### Modulo 0: Osisn't (Interfaz Digestible de Huella Digital y Diagnóstico Preventivo)
* **Que hace:** Dashboard visual interactivo que ejecuta escaneos no intrusivos (Sherlock, Holehe, Maigret, HIBP) y presenta la huella digital en un grafo comprensible con *Exposure Score* (0-100), tarjetas pedagógicas y botones de remediación inmediata (enlaces directos vía JustDelete.me y cartas a data brokers).
* **Por que es propio:** Porque no existe en el mercado una herramienta que traduzca el OSINT técnico a un lenguaje empático para el usuario común y le ofrezca soluciones de baja en un solo clic. Consulta la especificación completa en [`osisnt-interfaz-huella-digital.md`](./osisnt-interfaz-huella-digital.md).

### Modulo 1: Cliente Movil & Interceptor Share Sheet (*Mobile Panic Button*)
* **Que hace:** Aplicacion movil con interfaz minimalista y extension de compartir (*Share Extension*). Permite crear un caso en 3 toques: capturar post, firmar LPOA y despachar escudo legal.
* **Por que es propio:** Reduce la friccion de 30 minutos a 45 segundos en el momento exacto en que la victima sufre la agresion.

### Modulo 2: Motor Forense de Captura y Sellado (*Evidence Vault*)
* **Que hace:** Worker en segundo plano que navega a la URL compartida, realiza un volcado completo de headers, captura de pantalla de resolución completa, renderiza el DOM, calcula el hash SHA-256 y ejecuta `ots stamp` con OpenTimestamps en Bitcoin.
* **Por que es propio:** Debe garantizar la cadena de custodia digital y generar un PDF con dictamen técnico forense que se anexará al reclamo legal.

### Modulo 3: Sintetizador Juridico y Clasificador de Infracciones (*Legal Matrix Engine*)
* **Que hace:** Analizador de reglas que clasifica la infracción:
  * *Ruta A:* Difamación / Daño moral -> Cita artículos del Código Civil local.
  * *Ruta B:* Imagen íntima no consentida -> Vía penal (ej. Ley Olimpia en México / Art. 197 CP en España).
  * *Ruta C:* Doxxing / Datos financieros -> Vía de derechos ARCO / GDPR Art. 17 / CCPA.
  * *Ruta D:* Suplantación de identidad -> Violación de Términos de Servicio de Meta.
* **Por que es propio:** Las plantillas deben redactarse en lenguaje legal riguroso y amenazante para los equipos legales de las Big Tech, citando plazos perentorios y precedentes judiciales.

### Modulo 4: Orquestador de Despacho Multi-Canal (*Big Tech & Broker Dispatcher*)
* **Que hace:** Gestiona las colas de envío:
  * Despacha correos certificados a las direcciones legales de Google y Meta.
  * Ejecuta scripts de Playwright para someter los formularios web de Google Legal (`support.google.com/legal`).
  * Dispara peticiones de opt-out masivo hacia la lista curada de data brokers.
* **Por que es propio:** Requiere el manejo de reintentos, resolución de campos dinámicos de formularios y rotación de proxies residenciales.

### Modulo 5: Guardian de SLAs y Escalador Legal Automatico (*Legal SLA Watchdog*)
* **Que hace:** Motor de base de datos que computa los plazos legales (7, 14, 20, 30 días hábiles).
  * Día 7: Si no hay acuse o respuesta, reenvía una notificación de apercibimiento con marcado de urgencia.
  * Día 15/30: Si la plataforma ignora el requerimiento, redacta y prepara la queja formal lista para firmar ante las autoridades reguladoras (INAI, AEPD, FTC).
* **Por que es propio:** Este seguimiento automatizado es exactamente lo que ningún usuario hace por falta de tiempo o conocimiento.

### Modulo 6: Centinela de Desindexacion y Purga de Cache (*SERP De-indexing Sentinel*)
* **Que hace:** Consulta periódicamente (cada 12-24 horas) mediante SerpApi si el enlace sigue indexado en Google. En paralelo, verifica si el servidor de origen ya arrojó código `404 Not Found`. En cuanto detecta el `404`, somete automáticamente la petición a la herramienta de *Remove Outdated Content* de Google para acelerar la purga de caché y envia una **Push Notification** de confirmacion al celular.
* **Por que es propio:** Cierra el ciclo completo: no solo busca la eliminación en la red social, sino que garantiza que desaparezca de los resultados de búsqueda globales.

---

## 7. Resumen de la Pila Tecnologica Recomendada (Mobile-First Tech Stack)

| Capa | Tecnologia Propuesta | Justificacion |
| :--- | :--- | :--- |
| **Frontend / App Movil** | **React Native (Expo)** o **Flutter** | Soporte multiplataforma (iOS/Android), acceso fluido a Share Sheet y biometria. |
| **Share Sheet Extension** | iOS Action Extension / Android Send Intent | Permite capturar links de Instagram/TikTok sin abrir la app manualmente. |
| **Cómputo Local (Zero-Knowledge)** | Criptografia local / pHash en el cliente | La foto sensible se hashea en el dispositivo y nunca se sube a ningun servidor. |
| **Push Notifications** | Expo Push / Firebase Cloud Messaging (FCM) | Alertas inmediatas en pantalla de bloqueo sobre el avance de los SLAs legales. |
| **Backend & Workers** | Python (FastAPI + Celery / Redis) | Ecosistema ideal para OSINT, OpenTimestamps, automatizaciones Playwright. |
| **Automatizacion Web** | Playwright + Playwright-Stealth | Ejecuta el llenado de formularios de Google/Meta en servidores headless. |
| **Firma & KYC** | Stripe Identity Mobile SDK + Dropbox Sign API | Verificacion biometrica con camara nativa y firma legal LPOA. |
| **Base de Datos & Auth** | PostgreSQL + Supabase (Auth & Realtime) | Sincronizacion en tiempo real con la app movil mediante WebSockets. |
| **Monitoreo SERP** | SerpApi / ValueSERP | Auditoria limpia de resultados de Google. |

---

## 8. Proximos Puntos a Desarrollar e Iterar
1. **Flujo de Pantallas de la App Movil (UX Onboarding en Crisis):** Definir la navegacion desde que el usuario comparte el link hasta que recibe la confirmacion de envio del reclamo legal.
2. **Especificacion de la Extension de Compartir (Share Sheet):** Definir como parsear los enlaces de Instagram (posts, reels, stories), TikTok y X/Twitter.
3. **Estructura del Mandato Legal (LPOA Template para Firma Movil):** Redaccion del clausulado legal simplificado para firma tactil en pantalla.
