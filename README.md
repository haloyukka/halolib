# halolib
# ライブラリを作る
基本ディレクトリ構成
```
halolib
├── setup.py
└── halolib
    ├── __init__.py
    └── halolib.py
```

# インストール方法
```
cd [setup.py]と同階層
pip install .
```

# アンインストール方法
```
pip uninstall halolib
```

# 開発（editable）モードでのインストール
```
pip install -e .
```
`editable`モードでは、ライブラリ更新時に```pip install```し直さなくても、その内容が即座に反映される。

# 自作ライブラリをGitHubからインストール
```
pip install git+<リポジトリのURL>
```