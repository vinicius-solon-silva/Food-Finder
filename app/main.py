from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.card import MDCard
import finder 

class ResultadosCard(MDCard):
   def __init__(self,name='',address='',photo='',**kwargs):
       super().__init__(**kwargs)
       self.ids.name.text = name
       self.ids.address.text = address
       self.ids.photo.source = photo

class DemoProject(ScreenManager):
    def busca(self):
        comida = self.ids.mealType.text
        local = self.ids.location.text
        resposta = finder.find(comida, local)
        return resposta 

    def abrir_card(self,name,address,photo):
        self.ids.results_box.add_widget(ResultadosCard(name=name, address=address, photo=photo))  

    def navigation(self, tela):
        MDApp.get_running_app().root.current = tela

class TelaHome(Screen):
    ...

class ListaResultados(Screen):
    ...

class Myapp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'DeepOrange'
        self.theme_cls.accent_palette = 'Red'
        Builder.load_file('interface.kv')
        return DemoProject()
    
# Inicia o aplicativo
Myapp().run()