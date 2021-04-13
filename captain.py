from card import Card
class Captain(Card):
    def __init__(self,name):
           super().__init__(name)
           
    def extortion (self):
        self.coins=2

    def block_extotion(self):
        self.block_exto=False
        
        #metodos del capitan