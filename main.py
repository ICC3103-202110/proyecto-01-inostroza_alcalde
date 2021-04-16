
from contessa   import Contessa 
from cards      import Cards 
from captain    import Captain 

from ambassador import Ambassador
from duke       import Duke 
from assassin   import Assassin
from player     import Player 
import system 
import printer

'''
name in carts
duke = 1
contessa = 2
captain = 3
ambassador = 4
assassin = 5
list=1,2,3,4,5
'''
def main():
    name_cards=[('duke',1),('contessa',2),('captain',3),('ambassador',4),('assassin',5)]
    cards=Cards()#creacion de mazo
    stop_2=0
    list_cards=Cards()
    cards.create_cards() 
    while stop_2 !=1: #creacion de los jugadores 
        if stop_2 == 2:
            print ("You have entered an invalid number, please try again")
        print("with how many players are you going to play, 3 or 4?")
        value=int(input())
        if value<3 or value > 4:
             stop_2=2
        elif value ==3:
            names=[]
            all_cards=[]
            for x in range(3):
                cards.delete_card()
                card_play=[cards.s_card]
                cards.delete_card()
                card_play.append(cards.s_card)
                all_cards.append(card_play)
                print("enter player name "+str(x+1))
                name=input()
                names.append(name)
            player_1=Player(names[0],2,all_cards[0])
            player_2=Player(names[1],2,all_cards[1])
            player_3=Player(names[2],2,all_cards[2])
            player_4=0
            stop_2=1
        else:
            stop_2=1
            names=[]
            all_cards=[]
            for x in range(4):
                cards.delete_card()
                card_play=[cards.s_card]
                cards.delete_card()
                card_play.append(cards.s_card)
                all_cards.append(card_play)
                print("enter player name "+str(x+1))
                name=input()
                names.append(name)
            player_1=Player(names[0],2,all_cards[0])
            player_2=Player(names[1],2,all_cards[1])
            player_3=Player(names[2],2,all_cards[2])
            player_4=Player(names[3],2,all_cards[3])
        
    stop=0
    stop_1=0
    while stop_1 != 1:
        turn=0
        stp=0 
        while stp!=1:
            elec=printer.election(names,turn)
            win , chall=printer.priority_challeng(names,turn)  #aca se elige quien desafia 
            if win == 10:
                print("as no one challenged, we proceed to counter attacks")
                val=printer.counter(names,turn)
               
            else:
                pass

        
            





    while stop!=1:
        if system.winner!=5:
            print('poner quien gana ')
            stop=1

print("hola")     
if __name__ == '__main__':
    
    #aca llama funciones
    main()

        

