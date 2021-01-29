import os
import time
import random
from datetime import datetime
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.resources import resource_add_path
from kivy.properties import ObjectProperty, NumericProperty
from dateutil.relativedelta import relativedelta


# Widget imports for Dashboard.kv
from widgets.button import DashboardButtonLarge
from widgets.label import DashboardCard


KV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'kvs'))
resource_add_path(KV_PATH)
Builder.load_file('dashboard_screen.kv')


class Dashboard(Screen):
    main_screen_manager = ObjectProperty()
    run_time = NumericProperty(0)

    def __init__(self, *args, **kwargs):
        self.app = App.get_running_app()
        self.latest_alert = None
        self.last_hbeat = None
        super().__init__(*args, **kwargs)

    def on_last_alert_click(self, btn):
        self.update_last_alert()
        self.main_screen_manager.show_alert_details( None, backref='dashboard')


    def on_enter(self):
        Clock.schedule_interval(self.update_dashboard, 1)

    def on_leave(self):
        pass


    def update_last_alert(self):
        last_alert = self.ids.last_alert
        btn_data = {
            'status': 0,
            'heading': "Alert Title",
            'primary': "Alert Primary Text",
            'secondary': "Alert Secondary Text"

        }
        last_alert.set(**btn_data)

    def update_dashboard(self, dt):
        self.update_last_alert()
