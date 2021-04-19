from card import Card 
class Assassin(Card): #asesino listo 
    def __init__(self,name):
           super().__init__(name) 

    def killer(self,player,name_cards): #selecciona la carta para eliminar 
        
        print(player.name +" choose the card you want to discard:")
        c=player.cards
        for x in range(6):
            if x==c[0][1]:
                print(name_cards[c[0][1]])
            if x==c[1][1]:
                    print(name_cards[c[1][1]])
        print("1) first card \n 2)second card ")
        value=int(input())
        return value-1