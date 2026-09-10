# Especificación de Contrato de API (REST / OpenAPI 3.1)
## Backend Gateway: Osisn't Engine & Reputation Defense Shield
**Versión de API:** `v1`  
**Formato:** JSON / REST sobre TLS 1.3  
**Autenticación:** `Authorization: Bearer <JWT>` — emitido por el Módulo de Autenticación (passkeys FIDO2, sección 4). Sin nombre de usuario ni contraseña.

---

## 1. Convenciones Generales y Estándares

* **Códigos de Estado:**
  * `200 OK`: Petición procesada exitosamente con payload síncrono.
  * `201 Created`: Recurso creado exitosamente.
  * `202 Accepted`: Tarea encolada en workers asíncronos (patrón habitual en OSINT y Vault).
  * `400 Bad Request`: Parámetros inválidos o formato no soportado.
  * `401 Unauthorized`: Token JWT ausente o expirado.
  * `429 Too Many Requests`: Violación de cuota de peticiones (Rate Limit).
  * `500 Internal Server Error`: Falla no controlada del servidor.
* **Formato de Errores:** Se implementa el estándar **RFC 7807 (Problem Details for HTTP APIs)**:
  ```json
  {
    "type": "https://api.reputation-shield.io/errors/invalid-identifier",
    "title": "Invalid Target Identifier",
    "status": 400,
    "detail": "The provided username contains invalid characters for OSINT scanning.",
    "instance": "/api/v1/osint/scans"
  }
  ```

---

## 2. Endpoints del Módulo Preventivo: Osisn't

### 2.1 Iniciar Escaneo de Huella Digital
* **Ruta:** `POST /api/v1/osint/scans`
* **Descripción:** Encola una tarea asíncrona de descubrimiento multivariable (Sherlock, Holehe, Maigret, HIBP).
* **Cabeceras:** `Authorization: Bearer <JWT>`, `Content-Type: application/json`
* **Request Payload:**
```json
{
  "target_type": "email",
  "identifier": "luisa.castilleja@gmail.com",
  "associated_usernames": ["luisita_cp", "luisa_cp23"],
  "include_breaches": true
}
```
* **Response `202 Accepted`:**
```json
{
  "scan_id": "scn_89f02b1c-7f54-4a88-823a-e99bf8841029",
  "status": "QUEUED",
  "estimated_duration_seconds": 45,
  "created_at": "2026-09-09T15:45:00Z",
  "polling_url": "/api/v1/osint/scans/scn_89f02b1c-7f54-4a88-823a-e99bf8841029"
}
```

---

### 2.2 Consultar Estado y Progreso del Escaneo
* **Ruta:** `GET /api/v1/osint/scans/{scan_id}`
* **Descripción:** Permite al cliente móvil consultar el avance porcentual del rastreo para alimentar barras de progreso en la app.
* **Response `200 OK` (En progreso):**
```json
{
  "scan_id": "scn_89f02b1c-7f54-4a88-823a-e99bf8841029",
  "status": "PROCESSING",
  "progress_percentage": 68,
  "completed_modules": ["Holehe", "HaveIBeenPwned"],
  "running_modules": ["Sherlock"],
  "partial_findings_count": 14
}
```

---

### 2.3 Obtener Resultados Normalizados para el Dashboard Digestible
* **Ruta:** `GET /api/v1/osint/scans/{scan_id}/results`
* **Descripción:** Retorna la estructura JSON adaptada para renderizar el grafo de esferas y el Exposure Score en la app móvil.
* **Response `200 OK` (Completado):**
```json
{
  "scan_id": "scn_89f02b1c-7f54-4a88-823a-e99bf8841029",
  "exposure_score": 68,
  "risk_level": "ELEVATED",
  "summary": {
    "total_platforms_found": 18,
    "compromised_in_breaches": 2,
    "high_risk_accounts": 3,
    "inactive_accounts": 5
  },
  "categories": [
    {
      "category_name": "Social & Media",
      "color_hex": "#3B82F6",
      "items_count": 8,
      "items": [
        {
          "platform_name": "Instagram",
          "username": "luisita_cp",
          "url": "https://instagram.com/luisita_cp",
          "risk": "LOW",
          "human_explanation": "Cuenta activa y visible. Expone foto de perfil y biografía.",
          "remediation": {
            "type": "PRIVACY_CONFIG",
            "action_url": null,
            "instructions": "Cambia tu cuenta a privada en Configuración > Privacidad."
          }
        },
        {
          "platform_name": "Tumblr",
          "username": "luisita_cp",
          "url": "https://luisita-cp.tumblr.com",
          "risk": "MEDIUM",
          "human_explanation": "Blog inactivo desde 2016 con fotos personales y correo visible.",
          "remediation": {
            "type": "DIRECT_DELETION",
            "justdelete_slug": "tumblr",
            "direct_deletion_url": "https://www.tumblr.com/account/delete",
            "difficulty": "EASY"
          }
        }
      ]
    },
    {
      "category_name": "Breaches & Leaks",
      "color_hex": "#EF4444",
      "items_count": 2,
      "items": [
        {
          "platform_name": "Canva Leak (2019)",
          "exposed_data": ["Emails", "Passwords (Bcrypt)", "Names"],
          "risk": "CRITICAL",
          "human_explanation": "Tus datos estuvieron en una filtración pública masiva.",
          "remediation": {
            "type": "PASSWORD_RESET",
            "instructions": "Cambia la contraseña en cualquier otro servicio donde hayas usado esta clave."
          }
        }
      ]
    }
  ]
}
```

---

### 2.4 Catálogo de Remediación JustDelete.me
* **Ruta:** `GET /api/v1/remediation/directory/{service_slug}`
* **Descripción:** Devuelve la información de desuscripción de una plataforma específica desde el catálogo local en caché.
* **Response `200 OK`:**
```json
{
  "service": "Tumblr",
  "slug": "tumblr",
  "url": "https://www.tumblr.com/account/delete",
  "difficulty": "easy",
  "notes": "Una vez confirmada la contraseña, la cuenta y todos los blogs secundarios se eliminan permanentemente."
}
```

---

## 3. Endpoints del Módulo Reactivo: Escudo de Reputación (Panic Button)

### 3.1 Apertura de Caso desde Share Sheet
* **Ruta:** `POST /api/v1/cases`
* **Descripción:** Inicia un expediente de defensa reputacional al recibir un enlace compartido desde Instagram, TikTok o navegadores.
* **Request Payload:**
```json
{
  "source_url": "https://www.instagram.com/p/DF93ka8x1Z/",
  "platform_detected": "instagram",
  "infringement_type": "DEFAMATION",
  "victim_statement": "Publicación con acusaciones falsas y uso no consentido de mi nombre."
}
```
* **Response `201 Created`:**
```json
{
  "case_id": "cas_9a87d23e-11bc-4e09-bca1-f098234a4501",
  "status": "PRESERVING_EVIDENCE",
  "created_at": "2026-09-09T15:47:00Z"
}
```

---

### 3.2 Registro de Firma del Mandato Digital (LPOA)
* **Ruta:** `POST /api/v1/cases/{case_id}/lpoa`
* **Descripción:** Adjunta el poder de representación legal firmado táctilmente por el usuario con respaldo biométrico.
* **Request Payload:**
```json
{
  "full_legal_name": "Luisa Alfonsa Castilleja Peugnet",
  "document_id": "INE-MEX-98127391823",
  "biometric_auth_type": "FACE_ID",
  "signature_svg_base64": "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Ik0xMCA4MCBDIDQwIDEw...",
  "terms_accepted": true,
  "timestamp": "2026-09-09T15:47:15Z"
}
```
* **Response `200 OK`:**
```json
{
  "case_id": "cas_9a87d23e-11bc-4e09-bca1-f098234a4501",
  "lpoa_status": "EXECUTED",
  "lpoa_document_sha256": "8f4c2e71b293c0490b83e390c9b1b9e38d742611f58a38c8234857b2849102ef",
  "actions_unlocked": ["BIG_TECH_DISPATCH", "GOOGLE_DEINDEXATION"]
}
```

---

### 3.3 Consulta del Timeline de SLAs y Estado de Desindexación
* **Ruta:** `GET /api/v1/cases/{case_id}/timeline`
* **Descripción:** Muestra la cronología pericial, envíos legales efectuados y estado de desindexación en Google Search.
* **Response `200 OK`:**
```json
{
  "case_id": "cas_9a87d23e-11bc-4e09-bca1-f098234a4501",
  "current_stage": "DISPATCHED_TO_LEGAL",
  "evidence_sealed": {
    "sha256": "4b928374e29a8f4c12...",
    "bitcoin_block_height": 914230,
    "ots_file_available": true
  },
  "sla_watchdog": {
    "days_elapsed": 2,
    "days_remaining_for_legal_sla": 13,
    "next_scheduled_escalation": "2026-09-16T15:47:00Z"
  },
  "serp_sentinel": {
    "last_checked_at": "2026-09-09T15:00:00Z",
    "http_status_code": 200,
    "indexed_in_google": true,
    "outdated_purge_submitted": false
  }
}
```

---

## 4. Módulo de Autenticación (Passkeys FIDO2 / WebAuthn)

Registro e inicio de sesión sin nombre de usuario, correo ni contraseña. La
biometría desbloquea una llave privada que vive en el Secure Enclave / Android
Keystore; el servidor solo almacena un identificador aleatorio y llaves públicas.

Cada flujo tiene dos pasos: `.../options` (el servidor entrega un
`challenge_token` firmado y sin estado, válido 120 s) y `.../verify` (el cliente
devuelve ese token junto con la respuesta del autenticador). El login es
*usernameless*: `authentication/options` no envía `allowCredentials`.

| Ruta | Descripción | Respuesta |
| :--- | :--- | :--- |
| `POST /api/v1/auth/passkey/registration/options` | Reto para crear una passkey | `200` `{ challenge_token, public_key }` |
| `POST /api/v1/auth/passkey/registration/verify` | Verifica la passkey y **crea la cuenta** | `201` sesión |
| `POST /api/v1/auth/passkey/authentication/options` | Reto para iniciar sesión | `200` `{ challenge_token, public_key }` |
| `POST /api/v1/auth/passkey/authentication/verify` | Verifica y abre sesión | `200` sesión |
| `POST /api/v1/auth/token/refresh` | Rota el refresh token | `200` sesión |
| `POST /api/v1/auth/logout` | Revoca el refresh token | `204` |
| `GET /api/v1/auth/me` | Resumen de la cuenta (requiere `Bearer`) | `200` |

**Cuerpo de sesión** (`201`/`200`):

```json
{
  "access_token": "<JWT, 1 h>",
  "refresh_token": "<opaco, se rota en cada uso>",
  "token_type": "bearer",
  "expires_in": 3600,
  "user": { "id": "9a8f02b1", "label": "Mi bóveda FEE" }
}
```

**Errores** (RFC 7807): `invalid-challenge` (400), `invalid-credential` (400),
`unknown-credential` (401), `invalid-session` (401), `rate-limited` (429).

El contrato detallado, ejemplos para Flutter y los archivos de asociación de
dominio (`/.well-known/assetlinks.json`, `/.well-known/apple-app-site-association`)
están en `Hackaton-FEE/server` → `docs/auth-contract.md`.
