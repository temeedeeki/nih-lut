# NIH LUT

[![Python](https://img.shields.io/badge/-Python-3776ab?logo=python&logoColor=ffdd54&style=for-the-badge)](https://www.python.org/)

[![License: GPL-2.0-or-later](https://img.shields.io/badge/License-GPL--2.0--or--later-blue.svg)](../LICENSE)

[English](../README.md) | [日本語](README.ja.md)

AMIDEを基にした、ImageJ用のNIHカラーマップ・ルックアップテーブル（LUT）です。

![NIHカラーマップのプレビュー](../assets/nih-colorbar.svg)

## 概要

このリポジトリでは、[AMIDE](https://amide.sourceforge.net/)の実装を基に作成した、ImageJ用のNIHカラーマップLUTを公開しています。

`NIH.lut`をダウンロードしてImageJに導入することで、AMIDEで使用されているNIHカラーマップを再現できます。

## インストール方法

1. [最新のリリース](https://github.com/temeedeeki/nih-lut/releases/latest)から`NIH.lut`をダウンロードします。
2. ImageJのインストールディレクトリを確認します。
3. ダウンロードした`NIH.lut`をImageJのインストールディレクトリ内にある`luts/`ディレクトリにコピーします。
4. ImageJが起動している場合は再起動します。
5. `Image` > `Lookup Tables` > `NIH`を選択して、カラーマップを適用します。

> [!NOTE]
> ImageJのインストールディレクトリは、OSやインストール方法（APT、Fiji、スタンドアロン版など）によって異なります。必要に応じて、該当する`luts/`ディレクトリを手動で確認してください。

## 使用方法

Pythonのソースコードから`NIH.lut`を生成するには、次のコマンドを実行します。

```bash
uv run generate_nih_lut.py
```

生成された`NIH.lut`はカレントディレクトリに保存されます。

## ライセンス

このプロジェクトは、GNU General Public License v2.0以降（`GPL-2.0-or-later`）の下で公開されています。詳細は[LICENSE](../LICENSE)を参照してください。

NIHカラーマップの実装は、Andy Loening氏が開発した[AMIDE](https://amide.sourceforge.net/)の実装を基にしています。
