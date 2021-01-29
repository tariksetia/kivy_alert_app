import os, time
import shutil
import pathlib
import logging
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.resources import resource_add_path

# Imports used in main_screen.kv
from widgets.button import Grid
from screens.main_screen_manager import MainScreenManager

KV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'kvs'))
resource_add_path(KV_PATH)
Builder.load_file('main_screen.kv')


class Ipas(GridLayout):

    def show_dashboard(self, btn):
        sm = self.ids.screen_manager
        sm.current = 'screen_dashboard'
    
    def show_alert_list(self, btn):
        sm = self.ids.screen_manager
        sm.show_alert_list()


class IPASApp(App): 
    def __init__(self,db, warn_processor, **kwargs):
        super().__init__(**kwargs)
        
    def build(self):
        self.title = 'Eyes on IPAWS'
        return Ipas()
    

if __name__ == "__main__":
    from kivy.core.window import Window
    Window.clearcolor = (1, 1, 1, 1)
    IPASApp().run()