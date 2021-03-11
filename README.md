便利なマルチファイルアドオン用のテンプレートです

## 概要
vscodeでの仕様を前提としていますが、適当にいじれば他の環境でも大丈夫かも



## setup
pipenvで必要なパッケージを管理したい場合はこんな感じで
```
pip install --user pipenv
echo export PIPENV_VENV_IN_PROJECT=true >> ~/.bashrc
source ~/.bashrc
cd "addon dev dir"
pipenv install
```
requirements.txtから環境のpipに直接インストールするなら
```
pip install --user -r requirements.txt
```


