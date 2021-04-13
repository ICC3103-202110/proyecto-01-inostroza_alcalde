from card import Card 
class Assassin(Card): #asesino listo 
    def __init__(self,name):
           super().__init__(name) 

    def killer(self,name_player):
        self.kill=(name_player)