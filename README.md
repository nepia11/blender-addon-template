便利なマルチファイルアドオン用のテンプレートです

## 概要

vscode での仕様を前提としていますが、適当にいじれば他の環境でも大丈夫かも

トップレベルの`__init__.py`はできるだけ小さく、変更が少ないようにしたい

基本 1 ファイルでオペレータを書くようにすると依存関係とかの面倒くささが少ないと思う

そのままダウンロードすればアドオンとしてインストールできるけど、build.py を使えば余計なファイルのない zip を生成できて素敵

## setup

pipenv で必要なパッケージを管理したい場合はこんな感じで

```
pip install --user pipenv
echo export PIPENV_VENV_IN_PROJECT=true >> ~/.bashrc
source ~/.bashrc
cd "addon dev dir"
pipenv install
```

requirements.txt から環境の pip に直接インストールするなら

```
pip install --user -r requirements.txt
```

## build

```
python build.py your_addon_name
```
