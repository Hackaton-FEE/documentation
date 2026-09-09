# Sistema de Diseño y Métodos de Experiencia (Design System)

> **"De la Ansiedad Técnica a la Acción Resolutiva."**  
> Guía oficial de identidad visual, colorimetría semántica, tipografía modular, métodos de diseño UX y especificación de componentes para la plataforma **Osisn't / Hackaton-FEE**.

---

## 🏛️ Propósito y Filosofía de Diseño

Las herramientas tradicionales de OSINT (*Open Source Intelligence*) fueron diseñadas por y para analistas de ciberinteligencia: interfaces de consola negra, fuentes monospace verdes o fosforescentes, y volcados masivos de datos crudos. Este paradigma produce **parálisis por ansiedad** en el usuario civil, quien descubre que sus datos están expuestos pero carece del conocimiento para saber qué tan grave es o cómo remediarlo.

El **Sistema de Diseño de Hackaton-FEE** subvierte este esquema apoyándose en los valores fundacionales de **FEE** (soberanía individual, propiedad del dato y transparencia) y de la **Universidad de la Libertad** (acción ejecutiva, resolución de problemas y autogestión):

1. **Diseño Empático y Calmo (*Calm Security UX*):** Sustituimos la estética de "hacker hostil" por un entorno luminoso, sobrio y accesible que inspira confianza similar a una aplicación bancaria de alta gama.
2. **Pedagogía Visual Instantánea:** Ningún dato técnico se muestra sin su traducción a lenguaje natural y su indicador de riesgo contextualizado.
3. **Orientación a la Acción en 1 Clic:** Todo diagnóstico de vulnerabilidad se acompaña de un camino de remediación directa (baja asistida, desindexación o creación de caso local cifrado).

---

## 📂 Estructura del Sistema de Diseño

Este módulo está organizado en especificaciones independientes pero altamente cohesivas:

| Documento | Descripción y Contenido Clave |
| :--- | :--- |
| 🎨 **[`colorimetria.md`](./colorimetria.md)** | Paleta institucional (`#167569` Cyber Teal / Deep Pine), superficies off-white anti-fatiga, semáforo de riesgo (0-100), categorías cromáticas de huella digital y especificación completa de Modo Oscuro. |
| 🔤 **[`tipografia.md`](./tipografia.md)** | Familias Sans-Serif legibles (*Inter* / *Outfit*), tipografía técnica monoespaciada (*JetBrains Mono*), escala modular de tamaños, jerarquía semántica y reglas de accesibilidad WCAG. |
| 🧠 **[`metodos-diseno-ux.md`](./metodos-diseno-ux.md)** | Metodologías de diseño de interacción: Modelo de 3 Capas, psicología para combatir la parálisis de seguridad, heurísticas de usabilidad para privacidad y lineamientos de empatía con la víctima. |
| 🧩 **[`componentes-ui.md`](./componentes-ui.md)** | Especificaciones anatómicas de widgets clave: `ExposureGauge` (medidor de riesgo), `DualFloatingActionButtons`, `FindingCard`, `ScanBottomSheet`, `StatusNotice` y formularios de casos. |
| 💾 **[`tokens.json`](./tokens.json)** | Diccionario estandarizado de Design Tokens (W3C Design Token Community Group / Figma Tokens / Style Dictionary) para integración automatizada. |

---

## 🚀 Implementación en el Código de la Aplicación

Los tokens definidos en este sistema son la fuente de verdad que alimenta directamente el tema de Flutter en:
- [Tema Global Flutter](file:///home/peterpad/Hackaton-FEE/app/lib/app/theme.dart)
- [Dashboard de Huella Digital](file:///home/peterpad/Hackaton-FEE/app/lib/features/footprint/presentation/dashboard_page.dart)
- [Medidor de Exposición](file:///home/peterpad/Hackaton-FEE/app/lib/features/footprint/presentation/widgets/exposure_gauge.dart)
- [Tarjetas de Hallazgos](file:///home/peterpad/Hackaton-FEE/app/lib/features/footprint/presentation/widgets/finding_card.dart)

### Mapeo Rápido de Tokens a Flutter (`ThemeData`)

```dart
// app/lib/app/theme.dart
final colors = ColorScheme.fromSeed(
  seedColor: const Color(0xFF167569), // Brand Primary Deep Pine
  brightness: Brightness.light,
);

return ThemeData(
  useMaterial3: true,
  colorScheme: colors,
  scaffoldBackgroundColor: const Color(0xFFF5F7F8), // Surface Scaffold
  // Botones y tarjetas con esquinas orgánicas definidas en tokens.json
  cardTheme: CardThemeData(
    elevation: 0,
    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
  ),
  floatingActionButtonTheme: const FloatingActionButtonThemeData(
    elevation: 4,
    shape: RoundedRectangleBorder(borderRadius: BorderRadius.all(Radius.circular(18))),
  ),
);
```

---

## 🛠️ ¿Cómo usar este módulo como Repositorio Independiente?

Este módulo se aloja de forma nativa en `documentation/design-system/` para garantizar la máxima agilidad durante el Hackathon. Si en fases futuras la organización requiere convertirlo en un repositorio propio (por ejemplo, `github.com/Hackaton-FEE/design-system` para publicar paquetes NPM o Dart):

```bash
# Opción A: Extraer con git subtree a un nuevo repositorio
git subtree split -P documentation/design-system -b design-system-standalone

# Opción B: Inicializar un repositorio gemelo en la raíz
cd /home/peterpad/Hackaton-FEE
mkdir -p design-system && cp -r documentation/design-system/* design-system/
cd design-system && git init
```
