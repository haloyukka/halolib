# halolib

## ライブラリを作る

基本ディレクトリ構成

```bash
halolib
├── setup.py
└── halolib
    ├── __init__.py
    └── halolib.py
```

---

## インストール方法

```bash
cd [setup.py]と同階層
pip install .
```

## アンインストール方法

- ライブラリを指定してアンインストール

```bash
pip uninstall halolib
```

- pipパッケージをアンインストール

```bash
# パッケージを出力"
pip freeze > requirements.txt

# すべてのパッケージを一括で削除する場合
pip uninstall -r requirements.txt -y

# パッケージを1つずつアンインストールする場合
pip uninstall -r requirements.txt
```

## 開発（editable）モードでのインストール

```bash
pip install -e .
```

`editable`モードでは、ライブラリ更新時に```pip install```し直さなくても、その内容が即座に反映される。

## 自作ライブラリをGitHubからインストール

```bash
pip install git+<リポジトリのURL>
```

---

## \_\_init\_\_.pyの書き方

- `__init__.py`とは2つの意味がある
  - 1つはPythonディレクトリを表す役割を担う
  - 1つはモジュールをimportするときの初期化処理を行う

### import ～とfrom ～ import ～の違い

### import

```python
import モジュール名 [as 別名]
```

- あるモジュールの機能を追加する
- 機能を利用するときは(モジュール名 もしくは 別名).(機能名)と入力する

```python
#randomというパッケージをimport
import random

#random内のrandintという関数を使う
A=random.randint(0,100)
print(A)
```

```python
A=[1,2,3,4,5]

#matplotlib内にあるpyplot.pyをimport
import matplotlib.pyplot as plt

#pyplot.pyのplotという関数を使う
plt.plot(A)
plt.show()
```

### from import

- `from モジュール名 import 機能名`
- あるモジュールのある機能を追加する。  
- ある機能のみを追加したいとき、モジュール名を書かずに使うことが出来る。

```python
A=[1,2,3,4,5]

#matplotlibパッケージ内のpyplot.py内にあるplot関数とshow関数の２つのみをimport
from matplotlib.pyplot import plot,show

plot(A)
show()
```

この2つには大差がないが`__init__.py`では意味が変わる。

### \_\_init\_\_.pyの書き方

パッケージの例

```bash
test_imt
├── __init__.py
├── main.py
└── sub.py
```

`main.pyの中身`

```python
import test_imt.sub as ts
def chkprint2():
 ts.chkprint()
 print("You use main.py!")
```

`sub.pyの中身`

```python
def chkprint():
 print("You use sub.py!")
```

```text
<注意>
パッケージにするときの同じディレクトリ内のモジュールのimportはパッケージ名から書いた方が良い
import (パッケージ名).(モジュール名)
```

# \_\_init\_\_.pyの中身が空のとき

- `__init__.py`は何も書かなくてもよい。
- ただし、importして関数を使いたい時、多少面倒になる。
  - 例えば、`main.py`の`chkprint2`関数を使い時、次のように入力する。

`test.py`

```python
import test_imt as ti
ti.main.chkprint2()

#結果
#You use sub.py!
#You use main.py!
```

"main"とモジュール名を間に入れる必要がでてくる。

モジュール名を書かないと次のようになる。

```python
import test_imt as ti
ti.chkprint2()

#結果
#test.py, line 2, in <module>
#    ti.chkprint2()
#AttributeError: module 'test_imt' has no attribute 'chkprint2'
```

`test_imt`には`chkprint2`という関数はない。

### \_\_init\_\_.pyでモジュール名をカット

`main.py`の`chkprint2`関数をモジュール名をカットして使いたいときには次のようにする。

`__init__.py`の中身

```python
from test_imt.main import *
```

import時

`test.py`

```python
import test_imt as ti
ti.chkprint2()

#結果
#You use sub.py!
#You use main.py!
```

- ここでは`from ~ imoprt *`を利用する。
- `import ~`を利用するとモジュール名をカットして関数を使うと先程のエラーが発生する。

- このような性質があるので
  - モジュール名をカットして使いたい時は`from ~ import *`を使って書く
  - 単に準備のために作ったモジュールで、公開するとき必要性が無いものは`import ~ `を使って書く
つ使い分けができる。

- 例えば、
  - `main.py`の中身を主に使用するなら`from test_imt.main import *`と書く。
  - `sub.py`をプログラム内に取り込むだけで主要な関数が無いなら`import test_imt.sub`と書く。
