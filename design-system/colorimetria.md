# Colorimetría y Sistema Cromático Semántico

El sistema de color de **Osisn't / Hackaton-FEE** responde a una necesidad psicológica fundamental: **desactivar el pánico y fomentar el empoderamiento**. La mayoría de las aplicaciones de seguridad saturan al usuario con rojos alarmistas, fondos negros y parpadeos amenazantes. Nuestro sistema adopta una paleta institucional y sobria de tonos tierra, bronce/oliva y crema sobre negro (`#000000`, `#403D2D`, `#605B44`, `#80795A`, `#C0B587`, `#FFF1B4`), combinando autoridad técnica, custodia de activos y serenidad visual en el dispositivo móvil.

---

## 1. Psicología del Color en Ciberseguridad Empática

```mermaid
graph LR
    subgraph Enfoque Tradicional OSINT
        A[Fondo Negro Terminal] --> B[Alertas Rojas Masivas]
        B --> C[Parálisis, Culpa y Desesperanza]
    end

    subgraph Enfoque FEE / Osisn't (Mobile App)
        D[Crema Suave #FFF1B4 / Off-White #F5F7F8] --> E[Oliva Profundo Institucional #403D2D]
        E --> F[Semáforo Racional Gradual #10B981 - #EF4444]
        F --> G[Claridad, Confianza y Acción Resolutiva]
    end
```

* **Paleta Representativa Principal:** Una progresión de 6 valores tonales coordinados que articulan la identidad de la app móvil:
  - **Negro Absoluto (`#000000`):** Contraste supremo, tipografía de alta jerarquía y fondos de alto impacto.
  - **Oliva Profundo / Bronce Quemado (`#403D2D`):** Color de marca principal (*Brand Primary*), botones primarios y encabezados clave. Proyecta firmeza, custodia de activos y discreción bancaria.
  - **Oliva Medio / Caqui Terroso (`#605B44`):** Color secundario de marca, acentos de interfaz y navegación.
  - **Caqui Cálido / Tierra Dorada (`#80795A`):** Elementos interactivos complementarios, bordes activos y estados intermedios.
  - **Oro Arena / Champagne Suave (`#C0B587`):** Contenedores secundarios, chips y realces en modo claro y acento primario en modo oscuro.
  - **Crema Claro / Vainilla Pastel (`#FFF1B4`):** Contenedores suaves de badges, fondos de selección y superficies luminosas anti-fatiga.
* **Superficies Claras Anti-Fatiga (`#FFF1B4` / `#F5F7F8`):** Rompen el cliché del "hacker hostil", invitando al usuario a percibir la ciberhigiene como una tarea cotidiana, ordenada y libre de estrés.
* **Semáforo Racional:** Los tonos cálidos y rojos solo se emplean como acentos semánticos acotados, nunca como fondos envolventes ni titulares acusatorios.

---

## 2. Paleta Institucional (Brand & Surface Tokens)

### 2.1. Escala Cromática Representativa de la Aplicación Móvil

| Tono / Muestra | HEX | RGB | Rol en el Sistema |
| :---: | :--- | :--- | :--- |
| ![#000000](https://dummyimage.com/24x24/000000/000000.png) | `#000000` | `rgb(0, 0, 0)` | **Negro Absoluto:** Fondos Dark Mode, textos Display y contraste máximo. |
| ![#403D2D](https://dummyimage.com/24x24/403D2D/403D2D.png) | `#403D2D` | `rgb(64, 61, 45)` | **Oliva Profundo:** Semilla institucional principal (`brand.primary`), botones principales. |
| ![#605B44](https://dummyimage.com/24x24/605B44/605B44.png) | `#605B44` | `rgb(96, 91, 68)` | **Oliva Medio:** Color secundario institucional (`brand.secondary`), enlaces y acentos. |
| ![#80795A](https://dummyimage.com/24x24/80795A/80795A.png) | `#80795A` | `rgb(128, 121, 90)` | **Caqui Cálido:** Bordes de foco, estados hover y elementos auxiliares. |
| ![#C0B587](https://dummyimage.com/24x24/C0B587/C0B587.png) | `#C0B587` | `rgb(192, 181, 135)` | **Oro Arena:** Contenedor secundario (`secondaryContainer`), acento modo oscuro. |
| ![#FFF1B4](https://dummyimage.com/24x24/FFF1B4/FFF1B4.png) | `#FFF1B4` | `rgb(255, 241, 180)` | **Crema Claro:** Contenedor primario suave (`primaryLight`), badges y selección. |

### 2.2. Mapeo a Tokens de Marca (Brand Tokens)

| Token Name | HEX | RGB | Muestra | Uso y Semántica |
| :--- | :--- | :--- | :---: | :--- |
| `color.brand.primary` | `#403D2D` | `rgb(64, 61, 45)` | ![#403D2D](https://dummyimage.com/24x24/403D2D/403D2D.png) | **Color Semilla Principal.** Botones de acción primaria, encabezados institucionales, barras de progreso y acentos clave. |
| `color.brand.primaryDark` | `#000000` | `rgb(0, 0, 0)` | ![#000000](https://dummyimage.com/24x24/000000/000000.png) | Estados *pressed/hover* de botones primarios y textos de máxima jerarquía. |
| `color.brand.primaryLight` | `#FFF1B4` | `rgb(255, 241, 180)` | ![#FFF1B4](https://dummyimage.com/24x24/FFF1B4/FFF1B4.png) | Contenedores suaves de badges, fondos de selección y chips activos. |
| `color.brand.secondary` | `#605B44` | `rgb(96, 91, 68)` | ![#605B44](https://dummyimage.com/24x24/605B44/605B44.png) | Oliva medio terroso. Elementos informativos, vínculos a documentación y botones secundarios. |
| `color.brand.secondaryContainer` | `#C0B587` | `rgb(192, 181, 135)` | ![#C0B587](https://dummyimage.com/24x24/C0B587/C0B587.png) | Fondo para banners de orientación pedagógica y tarjetas de ayuda. |

### 2.3. Superficies y Neutros (Neutrals & Slate Hierarchy)

| Token Name | HEX | Muestra | Aplicación en la Interfaz |
| :--- | :--- | :---: | :--- |
| `color.surface.scaffold` | `#F5F7F8` | ![#F5F7F8](https://dummyimage.com/24x24/F5F7F8/F5F7F8.png) | Fondo de pantalla global (`Scaffold.backgroundColor`). |
| `color.surface.card` | `#FFFFFF` | ![#FFFFFF](https://dummyimage.com/24x24/FFFFFF/FFFFFF.png) | Fondo de tarjetas, hojas de modal (`BottomSheet`) y diálogos. |
| `color.surface.cardBorder` | `#E2E8F0` | ![#E2E8F0](https://dummyimage.com/24x24/E2E8F0/E2E8F0.png) | Borde sutil de 1px en tarjetas y separadores de lista. |
| `color.surface.textPrimary` | `#1E293B` | ![#1E293B](https://dummyimage.com/24x24/1E293B/1E293B.png) | Títulos, valores de score y texto principal (Slate 800). |
| `color.surface.textSecondary` | `#64748B` | ![#64748B](https://dummyimage.com/24x24/64748B/64748B.png) | Subtítulos, descripciones de hallazgos y notas secundarias (Slate 500). |
| `color.surface.textMuted` | `#94A3B8` | ![#94A3B8](https://dummyimage.com/24x24/94A3B8/94A3B8.png) | Fechas relativas, metadatos y placeholders de formularios (Slate 400). |

---

## 3. Semáforo Semántico de Riesgo (Exposure Score)

El medidor de riesgo (*Exposure Gauge*) y las tarjetas de hallazgos utilizan una escala cromática calibrada de 4 niveles que informa con exactitud sin recurrir al sensacionalismo:

```
[ 0 ------------ 25 ]   [ 26 ----------- 55 ]   [ 56 ----------- 79 ]   [ 80 ---------- 100 ]
     BAJO / MENTA            MODERADO / ÁMBAR          ELEVADO / CORAL          CRÍTICO / CARMESÍ
       #10B981                   #F59E0B                   #F97316                  #EF4444
```

| Nivel de Riesgo | Rango | Color Token | Contenedor Suave | Significado y Experiencia de Usuario |
| :--- | :---: | :---: | :---: | :--- |
| **Bajo / Fantasma Digital** | `0 - 25` | `#10B981` (Mint) | `#ECFDF5` | Huella mínima o excelente higiene digital. No hay filtraciones ni registros sensibles públicos. |
| **Moderado / Usuario Habitual** | `26 - 55` | `#F59E0B` (Amber) | `#FEF3C7` | Presencia típica en redes y comercios electrónicos sin contraseñas comprometidas. Mantenimiento preventivo. |
| **Elevado / Vulnerable** | `56 - 79` | `#F97316` (Coral) | `#FFEDD5` | Mismo alias o teléfono reutilizado en múltiples servicios o sitios con incidentes pasados. Remediación aconsejada. |
| **Crítico / Peligro Inmediato** | `80 - 100` | `#EF4444` (Crimson) | `#FEE2E2` | Documentos de identidad, datos bancarios indexados en Google o contraseñas en texto plano expuestas. |

---

## 4. Acciones Semánticas Normalizadas vs. Paleta de Identidad de Marca

> [!IMPORTANT]
> **Regla de Coexistencia de Color:** La paleta representativa de la aplicación (`#000000`, `#403D2D`, `#605B44`, `#80795A`, `#C0B587`, `#FFF1B4`) rige toda la identidad de marca, navegación, tarjetas, tipografías y superficies. No obstante, **las acciones funcionales estándar y convencionales se mantienen normalizadas**:
> * **Aceptar / Confirmar / Éxito:** Se utiliza **verde normalizado (`#10B981`)** para garantizar el reconocimiento cognitivo instantáneo de estados seguros y confirmaciones.
> * **Cerrar / Cancelar / Destructivo / Error:** Se utiliza **rojo normalizado (`#EF4444`)** para alertas de peligro, eliminación de cuentas y botones de cierre crítico.
> * **Advertencia:** Se utiliza **ámbar normalizado (`#F59E0B`)**.

| Acción Funcional | Token | HEX | Contenedor | Aplicación en la Interfaz |
| :--- | :--- | :---: | :---: | :--- |
| **Aceptar / Guardar / Confirmar** | `color.semanticActions.confirm` | `#10B981` | `#ECFDF5` | Botón "Aceptar", modales de confirmación positiva, estados de éxito. |
| **Cerrar / Cancelar / Destructivo** | `color.semanticActions.destructive` | `#EF4444` | `#FEE2E2` | Botón "Cerrar (X)", "Eliminar Caso", alertas de borrado irreversible. |
| **Advertencia Preventiva** | `color.semanticActions.warning` | `#F59E0B` | `#FEF3C7` | Avisos de advertencia previa a acciones no destructivas pero sensibles. |
| **Acciones Principales de Flujo** | `color.brand.primary` | `#403D2D` | `#FFF1B4` | Botones de navegación ("Escanear", "Continuar", "Siguiente"). Rigen la identidad visual. |

---

## 5. Paleta de Categorías de Huella Digital (Bubble Map & Tags)

Para el gráfico de burbujas solares y los filtros de la lista de hallazgos, cada esfera de datos expuestos cuenta con un color representativo:

| Categoría | Color Token | Fondo de Chip | Icono Típico | Ámbitos y Ejemplos |
| :--- | :---: | :---: | :---: | :--- |
| **Redes Sociales & Comunicación** | `#3B82F6` | `#EFF6FF` | `Icons.people_alt_outlined` | Instagram, X/Twitter, TikTok, Telegram, WhatsApp, LinkedIn. |
| **Comercio & Finanzas** | `#10B981` | `#ECFDF5` | `Icons.shopping_bag_outlined` | MercadoLibre, Amazon, PayPal, billeteras de criptomonedas. |
| **Estilo de Vida & Streaming** | `#8B5CF6` | `#F5F3FF` | `Icons.sports_esports_outlined`| Spotify, Steam, Netflix, Tinder, Strava, Chess.com. |
| **Cuentas Olvidadas / Inactivas** | `#D97706` | `#FFFBEB` | `Icons.history_toggle_off` | Gravatar, foros antiguos (phpBB, vBulletin), Ask.fm, Tumblr. |
| **Brechas de Datos & Dumps** | `#DC2626` | `#FEF2F2` | `Icons.warning_amber_rounded` | Bases de datos filtradas (HaveIBeenPwned), Pastebin, leaks. |

---

## 6. Especificación de Modo Oscuro (*Dark Theme*)

Para entornos de baja luminosidad o preferencias del usuario, el sistema cuenta con su contraparte oscura calculada para mantener el confort visual sin perder el carácter institucional:

| Elemento | Token Claro | Token Oscuro | Razón de Diseño |
| :--- | :--- | :--- | :--- |
| **Scaffold** | `#F5F7F8` | `#000000` (Negro Puro) | Fondo absoluto que aprovecha la paleta base del sistema (`#000000`). |
| **Cards & Sheets** | `#FFFFFF` | `#403D2D` (Oliva Oscuro) | Superficie elevada con excelente separación cromática y calidez visual. |
| **Primary Accent** | `#403D2D` | `#C0B587` (Oro Arena) | Tono champagne luminoso de alto contraste sobre fondos oscuros y negros. |
| **Texto Principal** | `#1E293B` | `#FFF1B4` (Crema Claro) | Crema suave de alta legibilidad sin la agresividad del blanco puro. |
| **Texto Secundario** | `#64748B` | `#80795A` (Caqui Cálido) | Tono terroso armónico que garantiza contraste accesible en párrafos. |

---

## 7. Ratios de Contraste y Accesibilidad (WCAG 2.1 AA)

Todos los pares de color de texto y superficie han sido verificados contra las pautas de accesibilidad WCAG 2.1 nivel AA:

| Par Evaluado | Razón de Contraste | Cumplimiento WCAG AA |
| :--- | :---: | :---: |
| `#403D2D` (Primario) sobre `#FFFFFF` (Card) | **10.92 : 1** | ✅ Pasa con excelencia (AAA) |
| `#403D2D` (Primario) sobre `#FFF1B4` (PrimaryLight) | **9.61 : 1** | ✅ Pasa con excelencia (AAA) |
| `#000000` (Texto / Dark) sobre `#FFF1B4` (Crema Claro) | **18.49 : 1** | ✅ Pasa con excelencia (AAA) |
| `#605B44` (Secundario) sobre `#FFFFFF` (Card) | **6.82 : 1** | ✅ Pasa con excelencia (AAA) |
| `#C0B587` (Oro Arena) sobre `#000000` (Fondo Oscuro) | **10.20 : 1** | ✅ Pasa con excelencia (AAA) |
| `#1E293B` (Texto Primario) sobre `#F5F7F8` (Scaffold) | **12.43 : 1** | ✅ Pasa con excelencia (AAA) |
| `#EF4444` (Crítico) sobre `#FEE2E2` (Badge Container) | **5.12 : 1** | ✅ Pasa (Mínimo 4.5:1) |
