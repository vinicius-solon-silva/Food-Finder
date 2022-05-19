from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
import finder 

# Funções da tela
class Interface(MDFloatLayout):
    dialog = None

    # Chama função finder e muda as labels conforme preciso
    def busca(self):
        # Pega o conteúdo dos textfields e coloca em variáveis
        comida = self.ids.mealType.text
        local = self.ids.location.text

        # Chama a função finder e armazena o dicionário em uma variável
        resposta = finder.findARestaurant(comida, local)
       
        # Muda o texto das labels conforme o resultado
        if type(resposta) == dict:
            self.ids.resultados.text = "Resultados encontrados:"
            self.ids.name.text += resposta['name']
            self.ids.adress.text += resposta['address']
            self.ids.photo.text += resposta['photo']
        else:
            self.ids.resultados.text = "0 Resultados encontrados, tente novamente"
            self.ids.name.text = ""
            self.ids.adress.text = ""
            self.ids.photo.text = ""

# Não sei pra que serve
class Interface(MDApp):
    pass
    
# Inicia o aplicativo
Interface().run()
