import os
import json, threading, time
from datetime import datetime
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty
from kivy.resources import resource_add_path
from kivy.clock import Clock
from kivy_garden.mapview import MapMarker, MapView
from kivy_garden.mapview.geojson import GeoJsonMapLayer
from kivy_garden.mapview.utils import get_zoom_for_radius, haversine

KV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'kvs'))
resource_add_path(KV_PATH)

Builder.load_file('alert_details_screen.kv')

class AlertDetails(GridLayout):
    status = StringProperty("Status")
    category = StringProperty("Category")
    event = StringProperty("Event")
    sent = StringProperty("Sent")
    sender = StringProperty("Sender")
    expires = StringProperty("Expires")
    long_text = StringProperty("Long Text")
    language = StringProperty("Language")
    short_text = StringProperty("Short Text")
    area_desc = StringProperty("Area Desc")
    alert_id = StringProperty("Alert ID")
    headline = StringProperty("Headline")
    desc = StringProperty("Description")
    instruction = StringProperty("Instruction")
    contact = StringProperty("Contact")
    web = StringProperty("www.PleaseHelp.me")
    expired = BooleanProperty()


class AlertDetailScreen(Screen):
    main_screen_manager = ObjectProperty()
    backref = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def goto_backref(self, btn):
        if self.main_screen_manager:
            if self.backref == 'dashboard':
                self.main_screen_manager.show_dashboard(transition='right')
            else:
                self.main_screen_manager.show_alert_list(transition='right')


    def on_enter(self):
        self.mapbox = self.ids.map_box
        self.mapview = MapView()
        self.mapview.zoom = 5
        self.mapview.center_on(40.5960129, -99.5961643)        

        import random
        import glob
        counties = glob.glob('*.polygon')
        county = random.choice(counties)
        with open(county, 'r') as f:
            polygons = eval(f.read())
        
        #self.draw_polygons(polygons)
        polygon_draw_thread = threading.Thread(target = self.draw_polygons, args = (polygons,))
        polygon_draw_thread.start()


    def draw_polygons(self, polygons):
        if not polygons:
            return

        polygons = [ ("severe", polygon) for polygon in polygons]
        geo_json = self.get_geojson(polygons)
        self.gj_layer = GeoJsonMapLayer(geojson=geo_json)
        if self.gj_layer:
            lon, lat = self.gj_layer.center
            self.lon = lon
            self.lat = lat
            self.mapview.lon = self.lon
            self.mapview.lat = self.lat
            min_lon, max_lon, min_lat, max_lat = self.gj_layer.bounds
            radius = haversine(min_lon, min_lat, max_lon, max_lat)
            zoom = get_zoom_for_radius(radius, lat)
            self.mapview.zoom = zoom
            self.mapview.center_on(lat, lon)
        self.mapview.add_widget(self.gj_layer)
        self.mapbox.add_widget(self.mapview)
        #Clock.schedule_once(self.create_marker, 1)

    def create_marker(self,dt):
        self.marker = MapMarker(lat=self.lat, lon=self.lon)
        self.mapview.add_widget(self.marker)


    def on_leave(self):
        self.clear_widgets()
    
    def get_geojson(self, polygons):
        features = []
        
        for sev, p in polygons:
            feat = self.get_feature_dict()
            poly = self.fix_polygon(p)
            feat["geometry"]["coordinates"].append(poly)
            feat["properties"]["color"] = self.get_color_for_severity(sev)
            features.append(feat)
        
        result = {
            "type": "FeatureCollection",
            "features": features
            }
        
        return result
        
    def get_feature_dict(self):
        return {
            "type": "Feature",
            "properties":{
                "color":"blue"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": []
                }
            }
        
    def get_color_for_severity(self, severity):
        sev_dict = {
            "extreme": "red",
            "severe": "orange",
            "moderate": "blue",
            "minor": "green",
            "unknown": "grey"
        }
        return sev_dict.get(severity.lower(),'grey')
    
    def fix_polygon(self, polygon):
        p = list(polygon)
        for i in range(len(p)):
            p[i] = p[i][::-1]   
        
        return p
            
    
    def get_category_display_text(self, category):
        db_val_to_category_val = {
            "geo": "Earthquakes",
            "met": "Weather",
            "safety": "Public Safety",
            "rescue": "Rescue",
            "fire": "Fire",
            "health": "Health",
            "env": "Environment",
            "transport": "Transportation",
            "infra": "Infrastructure",
            "cbrne": "CBRNE",
            "other": "Other"
        }
        return db_val_to_category_val.get(category, category.title())


class AlertDetailApp(App):
    def __init__(self, alert, **kwargs):
        self.alert = alert
        super().__init__(**kwargs)

    def build(self):
        return AlertDetailScreen(alert=self.alert)
    
