from card import Card
class Contessa(Card) : #Contessa ready
    def __init__(self,name):
           super().__init__(name)
        
    def block_killer(self):
        value=False
        self.no_killer = value
# Contessa Methods