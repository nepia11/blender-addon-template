import importlib
from logging import getLogger, StreamHandler, Formatter, handlers, DEBUG
import inspect
import sys
import bpy
import os
import datetime


# アドオン情報
bl_info = {
    "name": "Blender Addon Template",
    "author": "nepia",
    "version": (0, 1, 0),
    "blender": (2, 83, 0),
    "location": "addon (operator,panel,ui) location",
    "description": "addon description",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "",
}


def setup_logger(log_folder: str, modname=__name__):
    """ loggerの設定をする """
    logger = getLogger(modname)
    logger.setLevel(DEBUG)
    # log重複回避　https://nigimitama.hatenablog.jp/entry/2021/01/27/084458
    if not logger.hasHandlers():
        sh = StreamHandler()
        sh.setLevel(DEBUG)
        formatter = Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        sh.setFormatter(formatter)
        logger.addHandler(sh)
        fh = handlers.RotatingFileHandler(
            log_folder, maxBytes=500000, backupCount=2)
        fh.setLevel(DEBUG)
        fh_formatter = Formatter(
            "%(asctime)s - %(filename)s - %(name)s"
            " - %(lineno)d - %(levelname)s - %(message)s")
        fh.setFormatter(fh_formatter)
        logger.addHandler(fh)
    return logger


# log周りの設定
scripts_dir = os.path.dirname(os.path.abspath(__file__))
log_folder = os.path.join(scripts_dir, f"{datetime.date.today()}.log")
logger = setup_logger(log_folder, modname=__name__)
logger.debug('hello')


# サブモジュールのインポート
module_names = [
    "ops_template",
    "ops_capture_color",
    "ui_template",
    "translations",
]
namespace = {}
for name in module_names:
    fullname = '{}.{}.{}'.format(__package__, "lib", name)
    # if "bpy" in locals():
    if fullname in sys.modules:
        namespace[name] = importlib.reload(sys.modules[fullname])
    else:
        namespace[name] = importlib.import_module(fullname)
logger.debug(namespace)

# モジュールからクラスの取得
classes = []
for module in module_names:
    for module_class in [obj for name, obj in inspect.getmembers(
            namespace[module]) if inspect.isclass(obj)]:
        classes.append(module_class)


# 翻訳用の辞書
translation_dict = namespace["translations"].get_dict()
translation = bpy.app.translations.pgettext


def register():
    for c in classes:
        bpy.utils.register_class(c)

    # 翻訳辞書の登録
    bpy.app.translations.register(__name__, translation_dict)
    logger.debug("succeeded register template addon")


def unregister():
    # 翻訳辞書の登録解除
    bpy.app.translations.unregister(__name__)

    for c in classes:
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()
