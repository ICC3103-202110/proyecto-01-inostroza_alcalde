from card import Card 
class Assassin(Card): # Assassin ready
    def __init__(self,name):
           super().__init__(name) 

    def killer(self,play,contessa,player,name_cards): #Selects card to eliminate
        cards=player.cards
        if cards[0][0] == 0 and cards[1][0] == 0:
            print("Sorry this player just lost all his cards")
        else:
            play.change_coins(-3)
            if contessa.no_killer != False:
                player.raise_card(name_cards)
                
            else:
                contessa.no_killerv = True
        return 