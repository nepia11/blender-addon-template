import bpy
import bgl
from logging import getLogger
logger = getLogger(__name__)

translation = bpy.app.translations.pgettext


def capture_under_cursor(buffer, mouse_x=0, mouse_y=0, type_flg="i") -> list:
    """
    フラットなrgba(float)のlistを返す
    """
    # GL_FLOATでバッファ作って読むと馬鹿みたいに重いのでGL_BYTE,GL_UNSIGNED_BYTEになってる
    bgl.glReadBuffer(bgl.GL_FRONT)
    bgl.glReadPixels(
        mouse_x,
        mouse_y,
        1,
        1,
        bgl.GL_RGBA,
        bgl.GL_UNSIGNED_BYTE,
        buffer,
    )
    if type_flg == "i":
        return [value for value in buffer]
    elif type_flg == "f":
        return [value / 255 for value in buffer]


def bytes_to_color_code(color: list) -> str:
    """ RGBAのイテラブルを投げるとカラーコードを返してくれる"""
    c = color
    return f"#{c[0]:x}{c[1]:x}{c[2]:x}{c[3]:x}"


def create_buffer(src_width: int = 1, src_height: int = 1):
    buffer = bgl.Buffer(bgl.GL_BYTE, src_width * src_height * 4)
    return buffer


class TEMPLATE_OT_CaptureColor(bpy.types.Operator):
    """ カーソル下の色を取得するやつ """
    bl_idname = "template.capture_color"
    bl_label = translation("my operator")
    bl_description = "operator description"
    bl_options = {"REGISTER", "UNDO"}

    buffer = create_buffer()
    # イベントを受け取りたいときはexecuteの代わりにinvokeが使える

    def invoke(self, context, event):
        color = capture_under_cursor(
            self.buffer, event.mouse_x, event.mouse_y, "f")
        context.tool_settings.gpencil_paint.brush.color = (color[:3])
        # brushes = [b for b in bpy.data.brushes]
        # for b in brushes:
        #     b.color = (color[:3])
        # logging
        logger.debug(color)
        # infoにメッセージを通知
        self.report({"INFO"}, f"{color}")
        # 正常終了ステータスを返す
        return {"FINISHED"}


class TEMPLATE_PT_CursorColor(bpy.types.Panel):
    bl_label = "CursorColor"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        layout.operator(TEMPLATE_OT_CaptureColor.bl_idname)
