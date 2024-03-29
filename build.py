import os
import random
import shutil
import string
import sys
import zipfile

# リリース用のzipを作るスクリプト

file_list = (
    "LICENSE",
    "README.md",
    "__init__.py",
    "lib",
)

ignores = shutil.ignore_patterns("__pycache__", "*.pyc")

# 引数
args = sys.argv


def random_name(n: int) -> str:
    return "".join(random.choices(string.ascii_letters + string.digits, k=n))


def make_zip(org_name: str, file_list: tuple, suffix: str):
    zip_name: str = org_name + "_" + suffix
    zip_dir = "./" + zip_name
    zip_path = "./" + zip_name + ".zip"
    print(zip_path)

    os.mkdir(zip_name)
    for s in file_list:
        _path = "./" + s
        if os.path.isdir(_path):
            shutil.copytree(_path, zip_dir + "/" + _path, ignore=ignores)
        else:
            shutil.copy(_path, zip_dir)

    zp = zipfile.ZipFile(zip_path, mode="w", compression=zipfile.ZIP_DEFLATED)

    for dirname, subdirs, filenames in os.walk(zip_dir):
        for filename in filenames:
            zp.write(os.path.join(dirname, filename))

    zp.close
    shutil.rmtree(zip_dir)


def main(args):
    arg_len = len(args)
    org_name: str = "dst"
    suffix: str = ""
    if arg_len == 1:
        suffix = random_name(4)
    elif arg_len == 2:
        suffix = args[1]
    else:
        org_name = args[1]
        suffix = args[2]

    make_zip(org_name, file_list, suffix)


main(args)
