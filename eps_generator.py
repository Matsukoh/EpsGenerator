import sys
from kivy.app import App
from kivy.core.window import Window
from PIL import Image as Image_PIL
from pgmagick import Image as Image_Pg_
import os


class EpsGenerator(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.img_format = "EPS"

    def build(self):
        if os.name != "posix" and os.name != "nt":
            print("This Operating System is not Supported")
            sys.exit()

        Window.bind(on_dropfile=self._on_file_drop)
        return

    def _on_file_drop(self, window, file_path):
        file_name = ""
        export_path = ""
        img_pil = Image_PIL.open(file_path)
        img_pg = Image_Pg_(file_path)

        if os.name == "posix":
            export_path = "/"
            file_name = str(img_pil.filename).split("/")[-1].split(".")[0]
            export_path_parts = str(img_pil.filename).split("/")[0:-1]
            del export_path_parts[0]
            for _, path_parts in enumerate(export_path_parts):
                export_path = export_path + path_parts + "/"
        elif os.name == "nt":
            file_name = str(img_pil.filename).split("¥")[-1].split(".")[0]
            export_path_parts = str(img_pil.filename).split("¥")[0:-1]
            del export_path_parts[0]
            for _, path_parts in enumerate(export_path_parts):
                export_path = export_path + path_parts + "¥"
        # img = img.resize((int(img.height/2), int(img.width/2)), Image.LANCZOS)
        # img.thumbnail(size, Image.LANCZOS)
        # print(img.size)
        if self.img_format == "EPS":
            img_pg.write("EPS:" + export_path + file_name + ".eps")
        elif self.img_format == "EPS2":
            img_pg.write("EPS2:" + export_path + file_name + ".eps")
        elif self.img_format == "EPS3":
            img_pg.write("EPS3:" + export_path + file_name + ".eps")
        # img.save(export_path + file_name + ".eps2", "EPS")
        return


if __name__ == '__main__':
    EpsGenerator().run()