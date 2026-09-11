# Identidad Visual y Animación de Carga: Viento y Huella Digital (Blanco y Negro)

> **"El viento que recorre las redes, se desprende de su rastro y se condensa en la soberanía de una huella digital limpia."**  
> Identidad visual, manual de assets vectoriales y especificación de la animación de carga de 120 fotogramas en **Blanco y Negro** para **Hackaton-FEE / Osisn't**.

---

## 🌪️ Concepto Cinético: De la Ráfaga a la Huella Digital

El isotipo oficial representa una transformación visual precisa:

1. **Entrada de la Ráfaga de Viento (Transparencia e Impulso):**
   - El viento ingresa desde la derecha como una corriente de aire dinámica con estelas de velocidad.
2. **Eliminación Progresiva de la Cola Trasera (Sin Efecto Fruta / Tallo):**
   - A medida que el viento avanza hacia la izquierda y se arremolina en el núcleo, **la cola por donde inició se va eliminando y disipando detrás de la onda**.
   - Esto evita que el logo parezca una fruta con tallo (*evil fruit*) y enfoca la atención en el objetivo final: **crear una huella digital pura**.
3. **Huella Digital Centrada y Consolidada:**
   - Al disolverse la cola, el logotipo queda compuesto exclusivamente por las crestas y vórtices que forman la silueta ovalada de una huella dactilar biométrica, centrada perfectamente en el lienzo.

---

## 🎨 Colorimetría: Blanco y Negro

Siguiendo las pautas de [`colorimetria.md`](../colorimetria.md):
- **Negro Puro (`#000000` / `#111827`):** Máximo contraste institucional sobre fondos claros y superficies anti-fatiga (`#F5F7F8` / `#FFFFFF`).
- **Blanco Puro (`#FFFFFF`):** Luminosidad limpia sobre fondos oscuros y pantallas Dark Mode (`#000000` / `#091312`).

---

## 📂 Estructura de Assets Creados

```text
documentation/design-system/logo/
├── README.md                           # Esta documentación
├── preview.html                        # Visor interactivo HTML5 (conmutador Negro/Blanco, 30/60 FPS, scrubber)
├── generate_frames.py                  # Generador determinista de los 120 frames SVG
├── logo_loading_animation.gif          # GIF animado (30 FPS)
├── logo_loading_animation.mp4          # Video MP4 optimizado (60 FPS)
├── standalone/
│   ├── logo_loading_black.svg          # SVG animado autónomo en Negro (#000000)
│   ├── logo_loading_white.svg          # SVG animado autónomo en Blanco (#FFFFFF)
│   ├── logo_loading_animated.svg       # Alias por defecto (Negro)
│   └── logo_loading_dark.svg          # Alias para Dark Mode (Blanco)
├── vector/
│   ├── logo_clean.svg                 # Versión original limpia (sin metadatos C2PA)
│   ├── logo_monochrome.svg            # Versión negra (#000000)
│   ├── logo_dark_white.svg            # Versión blanca (#FFFFFF)
│   └── logo_wh_bg.svg                 # Versión con fondo blanco sólido
├── frames_120/                         # 120 fotogramas SVG en NEGRO (#000000)
│   ├── frame_001.svg a frame_120.svg
└── frames_120_white/                   # 120 fotogramas SVG en BLANCO (#FFFFFF)
    ├── frame_001.svg a frame_120.svg
```

> [!NOTE]
> Esta misma estructura se encuentra replicada en [`app/assets/logo/`](https://github.com/Hackaton-FEE/app/tree/main/assets/logo) y declarada en [`app/pubspec.yaml`](https://github.com/Hackaton-FEE/app/blob/main/pubspec.yaml).

---

## 🎬 Fases de los 120 Fotogramas

| Fase | Frames | Duración (60 FPS) | Descripción Cinética |
| :--- | :---: | :---: | :--- |
| **1. Entrada del Viento** | 001 - 024 | 0.00s - 0.40s | La ráfaga entra por la derecha con estelas de velocidad, avanzando hacia el centro. |
| **2. Retracción de la Cola** | 025 - 060 | 0.41s - 1.00s | El viento se enrolla en espiral y **la cola trasera se elimina por completo detrás de la onda**. El logo se traslada al centro horizontal. |
| **3. Huella Digital Limpia** | 061 - 095 | 1.01s - 1.58s | La cola ha desaparecido al 100%. Solo queda la huella digital centrada, nítida y respirando orgánicamente. |
| **4. Disipación y Bucle** | 096 - 120 | 1.59s - 2.00s | Las crestas se transforman en corrientes de aire que fluyen hacia adelante, enlazando sin saltos con el Frame 001. |

---

## 💻 Uso en Flutter (`LogoLoadingIndicator`)

```dart
import 'package:fee_app/core/widgets/logo_loading_indicator.dart';

// Modo Claro (Negro sobre transparente/blanco)
const LogoLoadingIndicator(size: 96.0)

// Modo Oscuro (Blanco sobre fondos oscuros)
const LogoLoadingIndicator(
  size: 96.0,
  isDarkMode: true,
  message: 'Analizando huella digital...',
)
```
