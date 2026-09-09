# Documento de Arquitectura de Software (SAD)
## Modelo C4, Patrones de Diseño y Architecture Decision Records (ADRs)
**Estándar de referencia:** ISO/IEC/IEEE 42010 / C4 Model (Simon Brown)  
**Versión:** 1.0.0  

---

## 1. Visión y Objetivos Arquitectónicos

La arquitectura de la suite está diseñada bajo cuatro pilares fundamentales:
1. **Zero-Knowledge por Diseño:** Procesamiento criptográfico en el dispositivo del usuario para imágenes íntimas y credenciales sensibles; la nube nunca recibe contenido no cifrado.
2. **Desacoplamiento Orientado a Eventos:** Las operaciones de rastreo OSINT y preservación forense son inherentemente lentas y propensas a latencias externas; por ello, la arquitectura es 100% asíncrona mediante colas de mensajes distribuidas.
3. **Resiliencia ante Anti-Scraping:** Manejo tolerante a fallos, reintentos con *exponential backoff* y rotación de proxies residenciales en la capa de agregación OSINT.
4. **Mobile-First Nativo:** Integración profunda con los mecanismos nativos del sistema operativo móvil (Share Extensions, biometría del enclave seguro y notificaciones push).

---

## 2. Modelo C4 - Niveles de Arquitectura

### 2.1 Nivel 1: Diagrama de Contexto del Sistema (System Context)
Muestra cómo interactúan los usuarios finales y los agentes legales con la suite y con el ecosistema externo de Big Tech, motores de búsqueda y data brokers.

```mermaid
C4Context
    title Diagrama de Contexto (Nivel 1) - Suite de Soberanía Digital y Osisn't

    Person(user, "Usuario Final / Luisa", "Persona que busca auditar su huella digital o defender su reputación ante agresiones en línea.")
    Person(dpo, "Oficial de Datos / DPO", "Representante legal de plataformas o Data Brokers que recibe solicitudes de supresión.")

    System(suite, "Suite Soberanía Digital", "Plataforma integral: app móvil reactiva + diagnóstico preventivo Osisn't.")

    System_Ext(social, "Plataformas Sociales", "Instagram, TikTok, X, Facebook (Orígenes de exposición / difamación).")
    System_Ext(google, "Ecosistema Google", "Google Search SERP, Legal Removal y Outdated Content Tool.")
    System_Ext(brokers, "Data Brokers (750+)", "Directorios de búsqueda de personas y registros públicos.")
    System_Ext(blockchain, "Cadena de Bloques Bitcoin", "Anclaje de sellos de tiempo inmutables vía OpenTimestamps.")

    Rel(user, suite, "Ejecuta diagnóstico Osisn't o comparte URLs difamatorias", "HTTPS / Push")
    Rel(user, social, "Navega y consume contenido", "App Nativa")
    Rel(social, suite, "Envía URL infractora vía Share Sheet", "Send Intent / Extension")
    Rel(suite, google, "Monitorea SERP y solicita desindexación legal", "APIs / Playwright")
    Rel(suite, dpo, "Despacha cartas formales de opt-out amparadas en GDPR/CCPA", "Email Certificado / API")
    Rel(suite, blockchain, "Registra hash forense SHA-256 de la evidencia", "OTS Protocol")
    Rel(suite, brokers, "Transmite peticiones de borrado masivo", "Batch API / Mail")
```

---

### 2.2 Nivel 2: Diagrama de Contenedores (Container Diagram)
Describe los límites del software ejecutable, tecnologías seleccionadas y cómo viajan los datos entre el cliente y el backend.

```mermaid
C4Container
    title Diagrama de Contenedores (Nivel 2) - Componentes de la Suite

    Container(app, "App Móvil (Cliente)", "React Native / Expo", "Interfaz de Osisn't (grafo, score), Share Extension nativa y firma táctil LPOA.")
    Container(api, "API Gateway & BFF", "FastAPI (Python 3.11)", "Control de acceso, orquestación de llamadas y agregador de respuestas en tiempo real.")
    ContainerDb(redis, "Broker de Mensajes & Caché", "Redis 7", "Colas Celery para tareas OSINT y caché volátil de resultados por 48h.")
    Container(worker_osint, "OSINT Aggregator Workers", "Python / Celery", "Ejecución paralela de Sherlock, Holehe, Maigret y consultas a HIBP.")
    Container(worker_vault, "Evidence Vault Workers", "Playwright + OTS", "Navegación headless, renderizado DOM, captura de pantalla y hash OpenTimestamps.")
    Container(worker_sla, "SLA & SERP Watchdog", "Python Cron / Celery Beat", "Sondeo periódico de desindexación en Google y escalamiento por días hábiles.")
    ContainerDb(db, "Base de Datos Central", "PostgreSQL (Supabase)", "Persistencia de casos, metadatos forenses, plantillas legales y estado de SLAs.")

    Rel(app, api, "Envía solicitudes de diagnóstico o casos de desindexación", "HTTPS / JSON / JWT")
    Rel(api, redis, "Encola tareas de escaneo o preservación forense", "Redis Protocol")
    Rel(redis, worker_osint, "Consume tareas de descubrimiento", "AMQP / Celery")
    Rel(redis, worker_vault, "Consume tareas de captura forense", "AMQP / Celery")
    Rel(worker_sla, db, "Verifica plazos de expedientes y estados", "SQL")
    Rel(worker_osint, api, "Publica eventos de avance de escaneo", "Redis PubSub")
    Rel(api, app, "Notificaciones de estado y grafo procesado", "WebSockets / Push FCM")
    Rel(api, db, "Lectura y escritura de perfiles y casos", "SQL / SQLAlchemy")
```

---

### 2.3 Nivel 3: Diagrama de Componentes (Component Diagram - Backend API)
Detalla la estructura interna del contenedor de API Gateway & BFF.

```mermaid
graph TD
    subgraph FastAPI Core Application
        Router[API Routers: /osint, /cases, /remediation, /auth]
        AuthGuard[Auth Guard & KYC Token Validator]
        
        subgraph Motores de Negocio
            ScoreEngine[Exposure Score Calculator Engine]
            LegalEngine[Legal Synthesizer & Rules Engine]
            DirectoryMgr[JustDelete.me & Broker Directory Manager]
            TaskDispatcher[Async Job Dispatcher]
        end

        subgraph Adaptadores Externos
            SerpAdapter[Google SERP & Outdated Content Adapter]
            MailAdapter[Certified Email / Lob Dispatcher]
            OTSAdapter[OpenTimestamps Client Library]
        end
    end

    Router --> AuthGuard
    AuthGuard --> TaskDispatcher
    TaskDispatcher --> ScoreEngine
    TaskDispatcher --> LegalEngine
    ScoreEngine --> DirectoryMgr
    LegalEngine --> MailAdapter
    TaskDispatcher --> SerpAdapter
    TaskDispatcher --> OTSAdapter
```

---

## 3. Registros de Decisiones de Arquitectura (ADRs)

### ADR-01: Cómputo Local de Hashing Perceptual (Zero-Knowledge) para Imágenes Íntimas
* **Estado:** Aprobado.
* **Contexto:** Las víctimas de extorsión o fotos íntimas no consentidas (NCII) desconfían profundamente de subir sus fotografías a la nube de una startup o hackathon.
* **Decisión:** Implementar algoritmos de *perceptual hashing* (pHash / PhotoDNA) en el cliente móvil utilizando WebAssembly o librerías nativas C++/Swift/Kotlin. El backend nunca recibe ni almacena las imágenes originales; únicamente almacena y transmite el hash criptográfico para cotejo en bases de datos de bloqueo (StopNCII / Meta / Google).
* **Consecuencias:**
  * *Positivas:* Privacidad absoluta del usuario, cumplimiento legal estricto contra almacenamiento de material explícito sensible, reducción drástica de costos de almacenamiento S3.
  * *Negativas:* Ligero incremento en el uso de batería y CPU del smartphone durante los segundos de cálculo.

---

### ADR-02: Adopción de Celery + Redis como Motor Asíncrono de OSINT
* **Estado:** Aprobado.
* **Contexto:** Ejecutar búsquedas simultáneas en más de 400 sitios web mediante Sherlock y 120 plataformas mediante Holehe genera latencias de red impredecibles (de 10 a 60 segundos). Bloquear la petición HTTP del usuario agotaría los timeouts de los clientes móviles.
* **Decisión:** Utilizar un patrón *Asynchronous Request-Reply* soportado por Celery y Redis. El endpoint `POST /api/v1/osint/scan` retorna de inmediato un `job_id` con código HTTP `202 Accepted`. El cliente móvil escucha los avances progresivos mediante WebSockets o sondeos ligeros.
* **Consecuencias:**
  * *Positivas:* API reactiva de alta velocidad, tolerancia a desconexiones de red en el móvil y escalabilidad horizontal de workers independientes.
  * *Negativas:* Requiere mantener y monitorear la infraestructura del broker de Redis y los procesos Celery.

---

### ADR-03: Share Sheet Nativo como Canal Primario de Ingesta en Casos de Crisis
* **Estado:** Aprobado.
* **Contexto:** En situaciones de estrés emocional por doxxing o difamación, el usuario no abre una página web, no copia URLs complejas ni rellena formularios de 15 campos.
* **Decisión:** Diseñar la experiencia móvil alrededor de la extensión del menú "Compartir" de iOS y Android (*Share Sheet Extension*). Al compartir un enlace de Instagram/TikTok directamente con la app, se dispara en segundo plano la preservación forense y se precarga la plantilla legal en 3 toques.
* **Consecuencias:**
  * *Positivas:* Tiempos de respuesta reducidos de 30 minutos a 45 segundos; ventaja competitiva radical frente a servicios web de escritorio.
  * *Negativas:* Requiere desarrollo nativo multiplataforma específico para las extensiones del sistema operativo.

---

### ADR-04: Almacenamiento Caché Estático del Directorio JustDelete.me
* **Estado:** Aprobado.
* **Contexto:** La experiencia digestible de Osisn't requiere redirigir de inmediato al usuario a la URL de baja sin depender de peticiones HTTP externas que puedan fallar.
* **Decisión:** Empaquetar y sincronizar periódicamente la base de datos JSON abierta de JustDelete.me dentro del servidor de API y en la caché local SQLite de la app móvil.
* **Consecuencias:**
  * *Positivas:* Tiempos de respuesta de 0 milisegundos al tocar "Eliminar Cuenta"; disponibilidad completa incluso en condiciones de baja conectividad.
  * *Negativas:* Requiere un worker programado semanal para detectar cambios o nuevos enlaces en el repositorio de JustDelete.me.

---

## 4. Estrategia de Seguridad y Cadena de Custodia Forense

```mermaid
sequenceDiagram
    autonumber
    actor Target as Usuario
    participant Vault as Evidence Vault Worker (Playwright)
    participant OTS as Servidor OpenTimestamps
    participant BTC as Blockchain Bitcoin
    participant DB as PostgreSQL Encrypted

    Target->>Vault: Envía URL infractora
    Vault->>Vault: Renderiza página con Chromium Headless
    Vault->>Vault: Captura Screenshot PNG + HTML Source + Response Headers
    Vault->>Vault: Calcula SHA-256(screenshot || html || headers)
    Vault->>OTS: Envía SHA-256 para estampar tiempo
    OTS->>BTC: Ancla raíz de Merkle en bloque de Bitcoin
    OTS-->>Vault: Retorna archivo de prueba `.ots`
    Vault->>DB: Guarda dictamen forense con hash + `.ots`
    DB-->>Target: Emite certificado de evidencia con validez probatoria
```

Esta arquitectura garantiza que la evidencia digital recolectada mantenga plena validez pericial ante tribunales de justicia y juzgados civiles, demostrando de forma inalterable que la publicación existía en una fecha y hora exactas antes de que el agresor intente borrarla.
