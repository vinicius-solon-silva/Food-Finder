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

# Classes com as telas
class Resultados(Screen):
    ...
   
class Inicial(Screen):
    ...

class TelaLogin(Screen):
    ...

class TelaHome(Screen):
    def busca(self):
        comida = self.ids.mealType.text
        local = self.ids.location.text

        resposta = finder.find(comida, local)
        print(resposta)
        return resposta 

    def abrir_card(self,name,address,photo):
        self.ids.box.add_widget(ResultadosCard(name=name, address=address, photo=photo))

class TelaConta(Screen): 
    ...

class TelaFavoritos(Screen):
    ...

# Screen manager
sm = ScreenManager()
sm.add_widget(TelaLogin(name='tela_login'))
sm.add_widget(TelaLogin(name='tela_home'))
sm.add_widget(TelaLogin(name='tela_conta'))
sm.add_widget(TelaLogin(name='tela_favoritos'))
sm.add_widget(Inicial(name='inicial'))
sm.add_widget(Resultados(name='resultados'))
sm.add_widget(TelaHome(name='home'))


# Construção principal do app
class Myapp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'DeepOrange'
        self.theme_cls.accent_palette = 'Red'
        return Builder.load_file('interface.kv')
    
# Inicia o aplicativo
Myapp().run()

