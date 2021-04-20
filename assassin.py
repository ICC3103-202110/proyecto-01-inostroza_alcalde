from card import Card 
class Assassin(Card): #asesino listo 
    def __init__(self,name):
           super().__init__(name) 

    def killer(self,play,contessa,player,name_cards): #selecciona la carta para eliminar 
        play.change_coins(-3)
        if contessa.no_killer != False:
            player.raise_card(name_cards)
            
        else:
            contessa.no_killerv = True
        return 