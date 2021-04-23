from card import Card
class Contessa(Card) : #Contessa Ready
    def __init__(self,name):
           super().__init__(name)
           self.no_killer = True
        
    def block_killer(self):
        value=False
        self.no_killer = value  # creo que es lo unico que hace la condesa 
# Contessa Methods