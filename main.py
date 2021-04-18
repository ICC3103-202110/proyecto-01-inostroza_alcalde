
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
    name_cards=['duke','contessa','captain','ambassador','assassin']
    cards=Cards()#creacion de mazo
    stop_2=0
    duke = Duke(1)
    contessa = Contessa(2)
    captain = Captain(3)
    ambassador = Ambassador(4)
    assassin = Assassin(5)
    list_card=[duke,contessa,captain,ambassador,assassin]
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
                card_play=[[1,cards.s_card]]
                cards.delete_card()
                card_play.append([1,cards.s_card])
                all_cards.append(card_play)
                print("enter name to player "+str(x+1))
                name=input()
                names.append(name)
            player_1=Player(names[0],2,all_cards[0])
            player_2=Player(names[1],2,all_cards[1])
            player_3=Player(names[2],2,all_cards[2])
            player_4=0
            players=[player_1,player_2,player_3]
            stop_2=1
        else:
            stop_2=1
            names=[]
            all_cards=[]
            for x in range(4):
                cards.delete_card()
                card_play=[[1,cards.s_card]]
                cards.delete_card()
                card_play.append([1,cards.s_card])
                all_cards.append(card_play)
                print("enter player name "+str(x+1))
                name=input()
                names.append(name)
            player_1=Player(names[0],2,all_cards[0])
            player_2=Player(names[1],2,all_cards[1])
            player_3=Player(names[2],2,all_cards[2])
            player_4=Player(names[3],2,all_cards[3])
            players=[player_1,player_2,player_3,player_4]
        
    stop=0
    stop_1=0
    print("\n")
    print("\n")
    l_names=len(names)
    turn=0
    while stop_1 != 1:
        
        stp=0 
        print("hola inicio")
        while stp!=1:
            player=players[turn]
            elec= printer.election(names,turn,players)
            if elec==0:
                player.change_coins(1)
                print(player.coins)
                break
            if elec == 1:
                    player.change_coins(-7)
                    Assassin.killer(contessa,player,name_cards)  ##crear las cartas, aun falta eso 

                     
            if elec > 1:
                win , chall =printer.priority_challeng(names,turn)  #aca se elige quien desafia 
            else:
                print("\n this action cannot be challenged or countered")
                break
            if win == 10:
                print("\n as no one challenged, we proceed to counter attacks")
                val=printer.counter(names,turn)
               
            else:
                if chall<l_names:
                    print("we proceed to counter attacks")
        print(player.cards)            
        turn += 1
        print(turn)
        if turn>len(names)-1:
            print("hola dos")
            turn=0

        
            





    while stop!=1:
        if system.winner!=5:
            print('poner quien gana ')
            stop=1
    
if __name__ == '__main__':
    
    #aca llama funciones
    main()

        

