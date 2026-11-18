# Copyright (C) 2000-2017 Andy Loening
# Copyright (C) 2026 temeedeeki
# SPDX-License-Identifier: GPL-2.0-or-later

"""Generate an NIH color map LUT for ImageJ."""

import math
from pathlib import Path

LUT_SIZE = 256


def convert_hsv_to_rgb(h: float, s: float, v: float) -> tuple[int, int, int]:
    """Convert HSV to 8-bit RGB."""
    h %= 360.0

    sector = math.floor(h / 60.0)
    fraction = h / 60.0 - sector

    p = v * (1.0 - s)
    q = v * (1.0 - s * fraction)
    t = v * (1.0 - s * (1.0 - fraction))

    colors = (
        (v, t, p),
        (q, v, p),
        (p, v, t),
        (p, q, v),
        (t, p, v),
        (v, p, q),
    )
    red, green, blue = colors[sector]

    return int(255 * red), int(255 * green), int(255 * blue)


def convert_intensity_to_nih_rgb(value: float) -> tuple[int, int, int]:
    """Convert normalized intensity [0, 1] to NIH RGB."""
    hue = 300.0 * (1.0 - value)
    saturation = 1.0
    brightness = min(1.0, 5.0 * value)

    return convert_hsv_to_rgb(hue, saturation, brightness)


def generate_nih_lut() -> bytes:
    """Generate an ImageJ-compatible NIH color map LUT."""
    colors = [convert_intensity_to_nih_rgb(i / (LUT_SIZE - 1)) for i in range(LUT_SIZE)]
    red, green, blue = zip(*colors, strict=True)

    # ImageJ raw LUT: 256 bytes per channel (R, G, B).
    return bytes(red) + bytes(green) + bytes(blue)


def main() -> None:
    lut_file_path = Path("NIH.lut")

    lut = generate_nih_lut()
    lut_file_path.write_bytes(lut)

    print(f"Successfully generated {lut_file_path.resolve()}")


if __name__ == "__main__":
    main()
