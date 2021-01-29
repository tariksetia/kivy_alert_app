
import os
import time
import glob
import hashlib
import logging
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.resources import resource_add_path
from .alert_details_screen import AlertDetailScreen
from .dashboard_screen import Dashboard
from widgets.label import SpinnerLabel



KV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'kvs'))
resource_add_path(KV_PATH)

Builder.load_file('main_screen_manager.kv')



class MainScreenManager(ScreenManager):

    def show_dashboard(self, transition='left'):
        self.transition.direction = transition
        self.current = 'screen_dashboard'

    def show_alert_details(self, alert, backref):
        self.transition.direction = 'left'
        name = str(time.time())
        ads = AlertDetailScreen(name=name)
        ads.backref = backref
        ads.main_screen_manager = self
        self.add_widget(ads)
        self.current=name

    