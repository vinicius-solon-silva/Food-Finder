from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.card import MDCard
from kivy.clock import Clock
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
import finder 
import db_conn

Window.size = (470,750)

class ResultadosCard(MDCard):
   def __init__(self,name='',address='',photo='',**kwargs):
       super().__init__(**kwargs)
       self.ids.name.text = name
       self.ids.address.text = address
       self.ids.photo.source = photo
       
class SenhaCard(MDCard):
    def fechar(self):
        self.parent.remove_widget(self)

class ExcluirCard(MDCard):
    def fechar(self):
        self.parent.remove_widget(self)

class DemoProject(ScreenManager):
    
    def login(self):
        MDApp.get_running_app().root.current = "tela_login"

    Clock.schedule_once(login, 5)

    def busca(self):
        comida = self.ids.mealType.text
        local = self.ids.location.text
        resposta = finder.find(comida, local)
        return resposta 

    def abrir_card(self,name,address,photo):
        self.ids.results_box.add_widget(ResultadosCard(name=name, address=address, photo=photo))

    def remove_cards(self):
        while True:
            try:
                self.ids.results_box.remove_widget(self.ids.results_box.children[0])
            except:
                break

    def navigation(self, tela):
        MDApp.get_running_app().root.current = tela

    def cadastrar(self):
        nome = self.ids.cdt_nome.text
        cpf = self.ids.cdt_cpf.text
        data_nasc = self.ids.cdt_data_nascimento.text
        email = self.ids.cdt_email.text
        senha = self.ids.cdt_senha.text

        try:
            retorno = db_conn.cadastrar(nome, cpf, data_nasc, email, senha)
            if retorno == "Cadastro concluido com sucesso!":
                self.dialog = MDDialog(title = 'Cadastro Concluído!', buttons=[MDFlatButton(text='Concluir')])
                self.dialog.open()
        except:
            self.dialog = MDDialog(title = 'Erro',text = 'Tente novamente' )
            self.dialog.open()

  
        

class TelaHome(Screen):
    ...

class TelaConta(Screen):
    def alter_senha(self): #método para abrir o card
        self.add_widget(SenhaCard())

    def excluir_conta(self): #método para abrir o card
        self.add_widget(ExcluirCard())
    ...

class ListaResultados(Screen):
    ...

class Myapp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'DeepOrange'
        #self.theme_cls.primary_light = ""
        Builder.load_file('interface.kv')
        return DemoProject()
    
# Inicia o aplicativo
Myapp().run()