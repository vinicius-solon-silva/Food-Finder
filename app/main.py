from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
import finder 

# Funções da tela
class Interface(MDFloatLayout):
    # Chama função finder e muda as labels conforme preciso
    def busca(self):
        # Pega o conteúdo dos textfields e coloca em variáveis
        comida = self.ids.mealType.text
        local = self.ids.location.text

        # Chama a função finder e armazena o dicionário em uma variável
        resposta = finder.findARestaurant(comida, local)

        # Muda o texto das labels conforme o resultado
        self.ids.name.text += resposta['name']
        self.ids.adress.text += resposta['address']
        self.ids.photo.text += resposta['photo']

# Não sei pra que serve
class Interface(MDApp):
    pass
    
# Inicia o aplicativo
Interface().run()