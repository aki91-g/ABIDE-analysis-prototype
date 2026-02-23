# オープンソースベースのリポジトリ

### 構成案
```text
.
├── .devcontainer/
│   ├── .gitattributes
│   ├── devcontainer.json
│   └── Dockerfile        # ライブラリ(NetworkX, bctpy, Snakemake)
├── .dvc/
│   └── .dvcignore
├── .github/
│   ├── workflows/        # CI (Lint, Directory Tree Auto-update)
│   └── CODEOWNERS
├── data/                 # .dvc ファイルで追跡
│   ├── raw/              # ABIDE, ADHD-200, OpenNeuro
│   └── processed/
├── docs/                 # 理論背景、数理モデルの解説
├── notebooks/            # 実験用 (ASD解析など)
├── results/              # .gitignore で除外(.gitkeep利用)
│   ├── figures/          # グラフ、可視化画像 (PNG, PDF)
│   ├── tables/           # 統計結果、精度評価表 (CSV, LaTeX)
│   ├── models/           # 学習済みモデル (PyTorchの重み, Joblibなど)
│   └── logs/             # 実験時のログ出力
├── src/                  # 共通ロジック (コアフレームワーク) --nilearn, MNE-Python, Nibabel
├── tests/                # CIで走らせるテスト
├── workflow/             # Snakemake
└── README.md             # ディレクトリ構成を自動注入
```
