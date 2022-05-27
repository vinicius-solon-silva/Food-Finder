from kivymd.app import MDApp, App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivymd.uix.floatlayout import FloatLayout, MDFloatLayout
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDRectangleFlatButton

Window.size = (400,750)

class SplashScreenApp(MDApp):
    def build(self):
        global sm
        sm = ScreenManager()
        sm.add_widget(Builder.load_file("splash.kv"))
        sm.add_widget(Builder.load_file("login.kv"))
        sm.add_widget(Builder.load_file("logado.kv"))
        return sm
    def on_start(self):
        Clock.schedule_once(self.login, 3)

    def login(*args):
        sm.current = "login"
    
    def logado(*args):
        sm.current = "logado"

if __name__=="__main__":
    SplashScreenApp().run()