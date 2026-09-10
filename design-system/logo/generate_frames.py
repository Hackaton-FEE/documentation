import xml.etree.ElementTree as ET
import re
import math
import os
import shutil

def main():
    # --- 1. Load Base Vector Geometry ---
    base_svg_path = 'documentation/design-system/logo/vector/logo_clean.svg'
    tree = ET.parse(base_svg_path)
    root = tree.getroot()
    for elem in root.iter():
        elem.tag = elem.tag.split('}')[-1]

    paths = root.findall('.//path')
    p0_d = paths[0].attrib['d']
    p0_parts = re.findall(r'[Mm][^Mm]+', p0_d)
    main_ribbon = p0_parts[0]

    discrete_elements = []
    # p0 subpaths 1..14
    for part in p0_parts[1:]:
        coords = [float(x) for x in re.findall(r'[-+]?\d*\.?\d+', part)]
        if not coords:
            continue
        xs, ys = coords[0::2], coords[1::2]
        discrete_elements.append({
            'd': part,
            'cx': sum(xs) / len(xs),
            'cy': sum(ys) / len(ys),
        })

    # Other paths (1..70)
    for p in paths[1:]:
        d = p.attrib.get('d', '')
        coords = [float(x) for x in re.findall(r'[-+]?\d*\.?\d+', d)]
        if not coords:
            continue
        xs, ys = coords[0::2], coords[1::2]
        discrete_elements.append({
            'd': d,
            'cx': sum(xs) / len(xs),
            'cy': sum(ys) / len(ys),
        })

    TOTAL_FRAMES = 120

    # Output directories for both Black (#000000) and White (#FFFFFF)
    DIRS_BLACK = [
        'documentation/design-system/logo/frames_120',
        'app/assets/logo/frames_120'
    ]
    DIRS_WHITE = [
        'documentation/design-system/logo/frames_120_white',
        'app/assets/logo/frames_120_white'
    ]

    for d in DIRS_BLACK + DIRS_WHITE:
        os.makedirs(d, exist_ok=True)

    print(f"Loaded geometry: 1 main ribbon + {len(discrete_elements)} discrete elements.")

    def render_frame_svg(frame_num, total_frames=120, color="#000000"):
        # frame_num: 1 to 120
        # t in [0.0, 1.0)
        t = (frame_num - 1) / float(total_frames)

        # -------------------------------------------------------------
        # 1. Wind Front and Tail Retraction Waves
        # - Front sweeps from 1150 down to 0 (reveals fingerprint)
        # - Back sweeps from 1250 down to 600 (erases the tail behind it!)
        # -------------------------------------------------------------
        if t < 0.50:
            front_p = t / 0.50
            front_e = 0.5 * (1.0 - math.cos(front_p * math.pi))
        elif t < 0.80:
            front_e = 1.0
        else:
            diss_t = (t - 0.80) / 0.20
            front_e = 1.0 - (0.5 * (1.0 - math.cos(diss_t * math.pi)))

        x_lead = 1150.0 - front_e * 1250.0

        # Back of the wind wave: starts advancing at t = 0.16, reaches 600 at t = 0.50
        # Once at 600, the tail is COMPLETELY ELIMINATED!
        if t < 0.16:
            x_trail = 1250.0  # tail still intact as it enters
        elif t < 0.50:
            trail_p = (t - 0.16) / (0.50 - 0.16)
            trail_e = 0.5 * (1.0 - math.cos(trail_p * math.pi))
            x_trail = 1250.0 - trail_e * (1250.0 - 600.0)
        else:
            x_trail = 600.0  # tail is 100% erased

        # -------------------------------------------------------------
        # 2. Smooth Centering Translation
        # When tail dissolves, the fingerprint glides from left (350)
        # to the exact horizontal center (576) of the 1152 canvas!
        # -------------------------------------------------------------
        if t < 0.20:
            shift_x = 0.0
        elif t < 0.52:
            s_p = (t - 0.20) / (0.52 - 0.20)
            s_e = 0.5 * (1.0 - math.cos(s_p * math.pi))
            shift_x = s_e * 226.0
        elif t < 0.80:
            shift_x = 226.0
        else:
            s_d = (t - 0.80) / 0.20
            s_e = 0.5 * (1.0 - math.cos(s_d * math.pi))
            shift_x = 226.0 * (1.0 - s_e)

        # -------------------------------------------------------------
        # 3. Dynamic Mask Path (Band between Lead Front and Trail Back)
        # -------------------------------------------------------------
        steps = 42
        front_pts = []
        for i in range(steps + 1):
            y = 960.0 - (1020.0 * i / steps)
            dy = (y - 440.0) / 440.0
            aero = max(0.0, 1.0 - dy * dy) * 140.0
            w = math.sin(y * 0.02 + t * 4.0 * math.pi) * 22.0
            x_pt = x_lead - aero + w
            front_pts.append((x_pt, y))

        trail_pts = []
        for i in range(steps + 1):
            y = -60.0 + (1020.0 * i / steps)
            dy = (y - 440.0) / 440.0
            # Natural curved boundary for the fingerprint oval at the right
            oval_curve = math.sqrt(max(0.0, 1.0 - dy * dy)) * 75.0
            w_trail = math.sin(y * 0.025 - t * 4.0 * math.pi) * 14.0
            x_t = x_trail + oval_curve + w_trail
            trail_pts.append((x_t, y))

        mask_pts = [f"M {front_pts[0][0]:.1f} {front_pts[0][1]:.1f}"]
        for pt in front_pts[1:]:
            mask_pts.append(f"L {pt[0]:.1f} {pt[1]:.1f}")
        for pt in trail_pts:
            mask_pts.append(f"L {pt[0]:.1f} {pt[1]:.1f}")
        mask_pts.append("Z")
        mask_d = " ".join(mask_pts)

        # -------------------------------------------------------------
        # 4. Discrete Elements Animation
        # -------------------------------------------------------------
        elem_svg = []
        for elem in discrete_elements:
            cx, cy = elem['cx'], elem['cy']
            d_val = elem['d']

            if cx > 620:
                # Tail element: only visible while the gust is passing over it
                if x_lead < cx < x_trail + 50:
                    op = 1.0
                else:
                    op = 0.0
            else:
                # Fingerprint element: forms and stays
                norm_x = (620.0 - cx) / 570.0
                arr_t = 0.18 + norm_x * 0.32
                if t < arr_t:
                    op = 0.0
                elif t < arr_t + 0.08:
                    op = (t - arr_t) / 0.08
                elif t < 0.80:
                    op = 1.0
                else:
                    diss = (t - 0.80) / 0.20
                    op = max(0.0, 1.0 - diss * 1.5)

            if op > 0.01:
                elem_svg.append(f'<path d="{d_val}" opacity="{op:.2f}" fill="{color}" />')

        # -------------------------------------------------------------
        # 5. Dynamic Wind Streamlines (Gust entrance)
        # -------------------------------------------------------------
        streamlines = []
        if t < 0.45:
            str_fade = max(0.0, 1.0 - t / 0.40)
            for s_i in range(5):
                y_c = 320.0 + s_i * 55.0
                phase = (t * 2.5 + s_i * 0.15) % 1.0
                xh = 1200.0 - phase * 1200.0
                xt = xh + 150.0
                if xh < 1150 and xt > 100:
                    str_d = f"M {xt:.1f} {y_c:.1f} Q {(xh + xt) * 0.5:.1f} {y_c + math.sin(phase * 6) * 18:.1f} {xh:.1f} {y_c - 10:.1f}"
                    str_op = 0.35 * str_fade
                    streamlines.append(f'<path d="{str_d}" stroke="{color}" stroke-width="2.5" stroke-linecap="round" fill="none" opacity="{str_op:.2f}" />')

        # -------------------------------------------------------------
        # 6. Biometric Pulse & Organic Breath (Phase 3: 52..80)
        # -------------------------------------------------------------
        breath_scale = 1.0
        if 0.52 <= t <= 0.80:
            pulse_p = (t - 0.52) / 0.28
            breath_scale = 1.0 + 0.02 * math.sin(pulse_p * math.pi)

        root_tf = f'transform="translate({shift_x:.1f}, 0) translate(350, 460) scale({breath_scale:.4f}) translate(-350, -460)"'

        stream_str = "\n    ".join(streamlines)
        elem_str = "\n    ".join(elem_svg)

        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1152" height="928" viewBox="0 0 1152 928">
  <defs>
    <clipPath id="waveClip_{frame_num}">
      <path d="{mask_d}" />
    </clipPath>
  </defs>
  
  <g id="logo_container" {root_tf}>
    <!-- Dynamic Wind Gust Streamlines -->
    <g id="wind_currents">
    {stream_str}
    </g>
    
    <!-- Main Ribbon (Tail eliminates behind the wind wave) -->
    <g id="main_ribbon" clip-path="url(#waveClip_{frame_num})" fill="{color}">
      <path d="{main_ribbon}" />
    </g>
    
    <!-- Fingerprint Ridges (Standalone Huella Digital) -->
    <g id="fingerprint_ridges">
    {elem_str}
    </g>
  </g>
</svg>'''
        return svg

    print("Generating 120 frames in Black (#000000) and White (#FFFFFF)...")
    for f_num in range(1, TOTAL_FRAMES + 1):
        fname = f"frame_{f_num:03d}.svg"

        # Render Black
        svg_black = render_frame_svg(f_num, TOTAL_FRAMES, color="#000000")
        for out_d in DIRS_BLACK:
            with open(os.path.join(out_d, fname), 'w', encoding='utf-8') as f:
                f.write(svg_black)

        # Render White
        svg_white = render_frame_svg(f_num, TOTAL_FRAMES, color="#FFFFFF")
        for out_d in DIRS_WHITE:
            with open(os.path.join(out_d, fname), 'w', encoding='utf-8') as f:
                f.write(svg_white)

    print(f"Generated 120 Black frames in {DIRS_BLACK[0]}")
    print(f"Generated 120 White frames in {DIRS_WHITE[0]}")

if __name__ == '__main__':
    main()
