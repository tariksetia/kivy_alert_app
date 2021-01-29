import os
from os.path import join, dirname
from kivy import utils
from kivy.app import App
from kivy.lang import Builder
from kivy.resources import resource_add_path
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty, BooleanProperty, ListProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout



KV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'kvs'))
resource_add_path(KV_PATH)

Builder.load_file('label.kv')



class Grid(GridLayout):
    pass

class FieldName(Label):
    pass

class FieldValue(Label):
    pass

class FieldValueWrappable(Label):
    pass

class BorderLabel(Label):
    pass

class BackgroundLabel(Label):
    expired = BooleanProperty(False)
    background_color = StringProperty("#fc960c")
    
    def get_color(self):
        if self.expired:
            return get_color_from_hex("#777CA3")
        else:
            return get_color_from_hex("#fc960c")

class DashboardCard(Grid) :
    status = NumericProperty('0')
    title = StringProperty('TITLE')
    heading = StringProperty('Heading')
    primary_text = StringProperty('Primary Text')

    def get_color_for_status(self, status):
        if status == 0:
            return "#48D3CD"
        elif status ==1:
            return "#FA9200"
        else:
            return "#FA3A2F"
    
    def get_status_icon(self, status):
        if status == 0:
            return "check-circle"
        else:
            return "exclamation-triangle"
    
    def get_label_color(self, status):
        if status == 0:
            return "#777CA3"
        elif status == 1:
            return "#FA9200"
        else:
            return "#FA3A2F"


class AlertStatusLabel(BackgroundLabel):
    status = NumericProperty(0)

    def get_color(self):
        if self.status == 0:
            return get_color_from_hex("#fc960c")
        else:
            return get_color_from_hex("#777CA3")

class Spinner(Label):
    pass


class SpinnerLabel(FloatLayout):
    angle = NumericProperty(0)
    color = StringProperty("#FFFFFF")
    icon = StringProperty('spinner')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.anim = Animation(angle = 360, duration=1) 
        self.anim += Animation(angle = 360, duration=1)
        self.anim.repeat = True
        self.anim.start(self)

    def on_angle(self, item, angle):
        if angle == 360:
            item.angle = 0
    
    def stop_anim(self):
        self.anim.cancel(self)
        
    
    def start_anim(self):
        self.anim.start(self)