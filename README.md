# NIH LUT

[![Python](https://img.shields.io/badge/-Python-3776ab?logo=python&logoColor=ffdd54&style=for-the-badge)](https://www.python.org/)

[![License: GPL-2.0-or-later](https://img.shields.io/badge/License-GPL--2.0--or--later-blue.svg)](LICENSE)

[English](README.md) | [日本語](docs/README.ja.md)

NIH color map lookup table (LUT) for ImageJ, based on AMIDE.

![NIH color map preview](assets/nih-colorbar.svg)

## Overview

This repository provides an NIH color map LUT for ImageJ, based on the implementation in [AMIDE](https://amide.sourceforge.net/).

The `NIH.lut` file can be downloaded and installed in ImageJ to reproduce the NIH color map used in AMIDE.

## Installation

1. Download [`NIH.lut`](https://github.com/temeedeeki/nih-lut/releases/latest/download/NIH.lut).
2. Locate your ImageJ installation directory.
3. Copy `NIH.lut` into the `luts/` directory inside your ImageJ installation.
4. Restart ImageJ if it is already running.

> [!NOTE]
> The ImageJ installation directory varies depending on your operating system and installation method (e.g., APT, Fiji, or a standalone installation). Locate the appropriate `luts/` directory manually if necessary.

## Usage

In ImageJ, select `Image` > `Lookup Tables` > `NIH` to apply the color map.

## Generating the LUT

To generate the `NIH.lut` file from the Python source code, run:

```bash
uv run generate_nih_lut.py
```

The generated `NIH.lut` file will be saved in the current working directory.

## License

This project is licensed under the GNU General Public License v2.0 or later (`GPL-2.0-or-later`). See [LICENSE](LICENSE) for details.

The NIH color map implementation is based on [AMIDE](https://amide.sourceforge.net/), originally developed by Andy Loening.
