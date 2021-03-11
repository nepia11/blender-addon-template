import bpy
from util import setup_logger

logger = setup_logger(modname=__name__)


class Template_PT_MyPanel(bpy.types.Panel):

    bl_label = "My panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "MY"

    # 本クラスの処理が実行可能かを判定する
    @classmethod
    def poll(cls, context):
        try:
            # 何かしらの判定処理
            return True
        except AttributeError:
            return False

    def draw(self, context):
        layout = self.layout
        layout.label(text="hoge")
        # [開始] / [終了] ボタンを追加
        layout.operator("template.my_operator")
        layout.separator()
        # ストローク並べ替え
        layout.label(text="Sorting strokes")
        arrange_props = [("TOP", "Bring to Front"), ("UP", "Bring Forward"),
                         ("DOWN", "Send Backward"), ("BOTTOM", "Send to Back")]
        for prop in arrange_props:
            op = layout.operator("gpencil.stroke_arrange",
                                 text=prop[1])
            op.direction = prop[0]
        layout.separator()
