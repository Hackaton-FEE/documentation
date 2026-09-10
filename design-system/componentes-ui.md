# Especificación de Componentes de Interfaz (UI Components)

Este documento define la anatomía visual, estados, tokens aplicables y directrices de implementación para los componentes clave de la aplicación móvil Flutter.

---

## 1. Medidor de Exposición (`ExposureGauge`)

El `ExposureGauge` es el componente protagónico del Dashboard. Resume la salud de la huella digital en una escala de 0 a 100 mediante un arco semicircular con gradiente continuo y animación de carga.

```
          . - ~ ~ ~ - .
      . '               ' .
    /      42 / 100         \
   |    NIVEL MODERADO       |
    \                       /
      ` .               . '
          ' - - - - - '
     [ 🔍 usuario@dominio.com ]
```

### 1.1. Anatomía y Métricas
* **Diámetro del Arco:** `220dp` a `240dp`.
* **Grosor del Trazo (*Stroke Width*):** `14dp` con bordes redondeados (`StrokeCap.round`).
* **Fondo del Arco Inactivo:** `#E2E8F0` (Gris Slate 200).
* **Gradiente Activo:** Interpolación continua entre los 4 colores del semáforo:
  - 0% a 25%: `#10B981` (Menta)
  - 26% a 55%: `#F59E0B` (Ámbar)
  - 56% a 79%: `#F97316` (Coral)
  - 80% a 100%: `#EF4444` (Carmesí)
* **Texto Central del Score:**
  - Tamaño: `44sp` (`FontWeight.w800`), color `#1E293B`.
  - Sufijo `/ 100`: `18sp` (`FontWeight.w500`), color `#64748B`.
* **Etiqueta de Nivel:**
  - Badge redondeado con fondo contenedor suave y texto en mayúsculas (`LabelSmall`, `12sp`, `FontWeight.w600`).

### 1.2. Archivo Fuente en el Código
* [Ver implementación en Flutter](file:///home/peterpad/Hackaton-FEE/app/lib/features/footprint/presentation/widgets/exposure_gauge.dart)

---

## 2. Botones Flotantes Duales (`DualFloatingActionButtons`)

Para garantizar una ergonomía óptima con una sola mano, la aplicación ancla dos acciones prioritarias en la zona inferior de la pantalla sin solaparse con la barra de navegación del sistema operativo:

```
+-------------------------------------------------------------+
|   [ 🔍 Escanear Identidad ]    [ 🛡️ + Nuevo Reporte ]       |
+-------------------------------------------------------------+
```

### 2.1. Anatomía
1. **Botón Izquierdo ("Escanear Identidad"):**
   - Estilo: `OutlinedButton` elevado o `FilledButton.tonal` con color suave de acento (`#FFF1B4` / `#C0B587`).
   - Icono: `Icons.radar_rounded` o `Icons.manage_search`.
   - Altura mínima: `52dp`, esquinas redondeadas `BorderRadius.circular(18)`.
2. **Botón Derecho ("Nuevo Reporte"):**
   - Estilo: `FilledButton` con color primario institucional (`#403D2D`).
   - Icono: `Icons.add_moderator_rounded`.
   - Altura mínima: `52dp`, elevación `4dp`.
* **Separación (*Gap*):** `12dp` entre ambos botones con distribución simétrica proporcional (`Row` con `Expanded`).

### 2.2. Archivo Fuente en el Código
* [Ver implementación en Flutter](file:///home/peterpad/Hackaton-FEE/app/lib/features/footprint/presentation/widgets/dual_floating_action_buttons.dart)

---

## 3. Tarjeta de Hallazgo (`FindingCard`)

Muestra de forma compacta y pedagógica cada cuenta, registro público o fuga detectada por los motores OSINT:

```
+-------------------------------------------------------------+
| [🔵] Instagram                                   [ MODERADO ]|
|      Cuenta pública vinculada a 'luisa.castilleja'          |
|                                                             |
| 🏷️ Redes Sociales   📅 Detectado: Hace 3 meses              |
|                                                             |
| [ 🗑️ Eliminar Cuenta ]             [ Iniciar Caso Retiro > ]|
+-------------------------------------------------------------+
```

### 3.1. Anatomía
* **Contenedor:** `Card` blanco (`#FFFFFF`), `elevation: 0`, borde de 1px `#E2E8F0`, radio de curvatura `16dp`.
* **Avatar de Plataforma:** Círculo de `40dp` con color de categoría y favicon / icono representativo.
* **Badge de Severidad:** Situado en la esquina superior derecha, con texto en mayúsculas y fondo translúcido (ej. `#FEF3C7` para moderado).
* **Descripción Resumida:** Tipografía `BodyMedium` (`14sp`), máximo 2 líneas elipsadas.
* **Fila de Acciones:**
  - Botón de texto/outline: Acceso a guía de borrado en JustDelete.me.
  - Botón sutil: *"Crear Caso"* para pre-llenar la solicitud de desindexación.

### 3.2. Archivo Fuente en el Código
* [Ver implementación en Flutter](file:///home/peterpad/Hackaton-FEE/app/lib/features/footprint/presentation/widgets/finding_card.dart)

---

## 4. Hoja Inferior de Escaneo (`ScanBottomSheet`)

Modal interactivo deslizable que permite ingresar nuevos identificadores para ser auditados:

### 4.1. Anatomía
* **Superficie:** `RoundedRectangleBorder(borderRadius: BorderRadius.vertical(top: Radius.circular(24)))`.
* **Pill / Manija de Arrastre (*Drag Handle*):** Rectángulo central de `36dp x 4dp`, radio `2dp`, color `#CBD5E1`.
* **Chips de Selección Rápida:**
  - `Email` (e.g. `nombre@empresa.com`)
  - `Handle / Alias` (e.g. `@usuario`)
  - `Teléfono` (e.g. `+52 55 ...`)
* **Campo de Entrada (`TextField`):**
  - Relleno suave `#F8FAFC`, borde de enfoque `#403D2D` de `2px`.
  - Icono de prefijo dinámico según el tipo de dato seleccionado.

### 4.2. Archivo Fuente en el Código
* [Ver implementación en Flutter](file:///home/peterpad/Hackaton-FEE/app/lib/features/footprint/presentation/widgets/scan_bottom_sheet.dart)

---

## 5. Avisos de Estado Semánticos (`StatusNotice`)

Banner ligero para informar sobre eventos de la aplicación sin bloquear la pantalla:
* **Variantes Semánticas:** Éxito / Aceptar (`#10B981`), Información / Institucional (`#605B44` / `#403D2D`), Advertencia (`#F59E0B`), Error / Destructivo / Cerrar (`#EF4444`).
* **Accesibilidad:** Envuelto en `Semantics(liveRegion: true)` con mensajes sanitizados que no leen secretos ni URLs sensibles en altavoz.

* [Ver implementación en Flutter](file:///home/peterpad/Hackaton-FEE/app/lib/shared/presentation/status_notice.dart)
