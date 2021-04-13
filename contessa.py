from card import Card
class Contessa(Card) : #condesa listo 
    def __init__(self,name):
           super().__init__(name)
           self.__no_killer
    def block_killer(self):
        value=False
        self.__no_killer = value  # creo que es lo unico que hace la condesa 
# metodos para la contessa