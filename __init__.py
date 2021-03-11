# blenderのreload scripts対応
if not("bpy" in locals()):
    import src
else:
    import imp
    imp.reload(src)

import bpy
import datetime

# log周りの設定

log_folder = '{0}.log'.format(datetime.date.today())
logger = src.util.setup_logger(log_folder, modname=__name__)
logger.debug('hello')

# 翻訳用の辞書
translation_dict = src.translations.translation_dict
translation = bpy.app.translations.pgettext


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


classes = []


def register():
    for c in classes:
        bpy.utils.register_class(c)

    # 翻訳辞書の登録
    bpy.app.translations.register(__name__, translation_dict)


def unregister():
    # 翻訳辞書の登録解除
    bpy.app.translations.unregister(__name__)

    for c in classes:
        bpy.utils.unregister_class(c)


if __name__ == "__main__":
    register()
