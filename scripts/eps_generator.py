import sys
from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget

import numpy as np
from time import time

from PIL import Image
import os

Window.size = (200, 300)
class CustomSpinner(Spinner):
    pass

class DragAndDropFileImporter(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._scaling_target = 512.
        self._file = Window.bind(
            on_dropfile = self._on_file_drop
        )

    def _on_file_drop(self, window, file_path):
        file_name = ""
        export_path = ""
        img = Image.open(file_path)
        # img_pg = Image_Pg_(file_path)

        if os.name == "posix":
            image_magick = "convert"
            export_path = "/"
            file_name = str(file_path).split("/")[-1].split(".")[0]
            export_path_parts = str(file_path).split("/")[0:-1]
            del export_path_parts[0]
            for _, path_parts in enumerate(export_path_parts):
                export_path = export_path + path_parts + "/"
        elif os.name == "nt":
            image_magick = "magick"
            file_name = str(file_path).split("¥")[-1].split(".")[0]
            export_path_parts = str(file_path).split("¥")[0:-1]
            del export_path_parts[0]
            for _, path_parts in enumerate(export_path_parts):
                export_path = export_path + path_parts + "¥"
    
        longer_idx = np.argmax([img.width, img.height])
        if longer_idx == 0:
            scaling_ref = img.width
        else:
            scaling_ref = img.height
        channel_size = len(img.split())
        if scaling_ref > self._scaling_target:
            if channel_size == 4:
                scaling_facter = self._scaling_target / scaling_ref

                resized_img = img.resize((int(img.width * scaling_facter), int(img.height * scaling_facter)))
                alpha_masked_img = Image.new("RGB", resized_img.size, (255, 255, 255))
                alpha_masked_img.paste(resized_img, mask=resized_img.split()[3])
                alpha_masked_img = alpha_masked_img.convert('RGB')
                alpha_masked_img.save(export_path + file_name + ".eps",  loss_less=True)
            else:
                scaling_facter = self._scaling_target / scaling_ref

                resized_img = img.resize((int(img.width * scaling_facter), int(img.height * scaling_facter)))
                resized_img = resized_img.convert('RGB')
                resized_img.save(export_path + file_name + ".eps",  loss_less=True)

        else:
            if channel_size == 4:
                alpha_masked_img = Image.new("RGB", img.size, (255, 255, 255))
                alpha_masked_img.paste(img, mask=img.split()[3])
                alpha_masked_img = alpha_masked_img.convert('RGB')
                alpha_masked_img.save(export_path + file_name + ".eps",  loss_less=True)
            else:
                img = img.convert('RGB')
                img.save(export_path + file_name + ".eps",  loss_less=True)
        return
        

class WindowLayout(FloatLayout): 
    '''The code of the application itself.''' 
    def __init__(self, **kwargs): 
          
        '''The button at the opening of the window is created here, 
        not in kv 
        ''' 
        super().__init__(**kwargs) 
        
        self._file_importer = DragAndDropFileImporter()
        self.add_widget(self._file_importer)

    def _change_export_format(self, x): 
        '''x is self.mainbutton.text refreshed''' 
        self._file_importer._scaling_target= float(x)

class EpsGenerator(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def build(self):
        if os.name != "posix" and os.name != "nt":
            sys.exit()
        return

if __name__ == '__main__':
    EpsGenerator().run()