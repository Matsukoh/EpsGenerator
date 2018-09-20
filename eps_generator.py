import sys
from kivy.app import App
from kivy.core.window import Window
from PIL import Image
import os


class EpsGenerator(App):
    def build(self):
        if os.name != "posix" and os.name != "nt":
            print("This Operating System is not Supported")
            sys.exit()

        Window.bind(on_dropfile=self._on_file_drop)
        return

    def _on_file_drop(self, window, file_path):
        file_name = ""
        export_path = ""
        img = Image.open(file_path)
        size = 480, 480

        if os.name == "posix":
            export_path = "/"
            file_name = str(img.filename).split("/")[-1].split(".")[0]
            export_path_parts = str(img.filename).split("/")[0:-1]
            del export_path_parts[0]
            for _, path_parts in enumerate(export_path_parts):
                export_path = export_path + path_parts + "/"
        elif os.name == "nt":
            file_name = str(img.filename).split("¥")[-1].split(".")[0]
            export_path_parts = str(img.filename).split("¥")[0:-1]
            del export_path_parts[0]
            for _, path_parts in enumerate(export_path_parts):
                export_path = export_path + path_parts + "¥"
        img.thumbnail(size)
        print(img.size)
        img.save(export_path + file_name + ".eps", "EPS")
        return


if __name__ == '__main__':
    EpsGenerator().run()