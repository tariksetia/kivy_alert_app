import os, kivysome
from os.path import join, dirname
from kivy.app import App
from kivy.lang import Builder
from kivy.resources import resource_add_path, resource_find
from kivy.uix.button import Button, ButtonBehavior
from kivy.uix.togglebutton import ToggleButton, ToggleButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty
from kivysome import icon
from kivy import utils
from widgets.label import SpinnerLabel


kivysome.enable(source='5.14.0', group=kivysome.FontGroup.REGULAR, font_folder= "./assets/fonts/fontsawesome")
kivysome.enable(source='5.14.0', group=kivysome.FontGroup.SOLID, font_folder="./assets/fonts/fontsawesome")



KV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'kvs'))
resource_add_path(KV_PATH)

Builder.load_file('button.kv')

class Grid(GridLayout):
    pass

class FlatButton(Button):

    def get_back_color(self, state, disabled):
        if disabled:
            return utils.get_color_from_hex("#cccddb")
        
        if state=='normal':
            return utils.get_color_from_hex("#FFFFFF") 
        
        return utils.get_color_from_hex('#787BA3')

class FlatSelectionButton(Button):
    pass

class FlatSelectionToggleButton(ToggleButton):
    pass

class FlatBorderButton(Button):
    
    def get_icon_color(self):
        if self.state == 'normal':
            return "#0B145A"
        else:
            return "#FFFFFF"

class FlatToggleButton(ToggleButton):
    pass

class SidebarButton(ToggleButtonBehavior, Grid):
    icon = StringProperty()
    label_text = StringProperty()
 

class DashboardButton(ButtonBehavior, Grid) :
    status = NumericProperty('0')
    title = StringProperty('TITLE')
    heading = StringProperty('Heading')
    primary = StringProperty('Primary Text')

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


class DashboardButtonLarge(ButtonBehavior, Grid) :
    status = NumericProperty(-1)
    title = StringProperty('TITLE')
    heading = StringProperty(' ')
    primary = StringProperty(' ')
    secondary = StringProperty(' ')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_color_for_status(self, status):
        if status == -1:
            return "#777CA3"
        elif status == 0:
            return "#48D3CD"
        elif status == 1:
            return "#FA9200"
        else:
            return "#FA3A2F"
    
    def get_status_icon(self, status):
        if status == -1:
            return "spinner"
        elif status == 0:
            return "check-circle"
        else:
            return "exclamation-triangle"
    
    def set(self, status=-1, heading=' ', primary=' ', secondary=' '):
        self.status = status
        self.heading = heading
        self.primary = primary
        self.secondary = secondary


class IconButton(Button, Grid):
    pass

class FullWidthButton(Button):
    pass

class SettingsToggleButton(ToggleButton):
    pass