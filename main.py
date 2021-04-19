
from contessa   import Contessa 
from cards      import Cards 
from captain    import Captain 
from ambassador import Ambassador
from duke       import Duke 
from assassin   import Assassin
from player     import Player 
import system 
import printer
import random

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
    printer.startup()
    name_cards=['duke ♕','contessa ♔','captain ⌘','ambassador ✎','assassin ⚔']
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
        print("Select number of players, 3 or 4?\n")
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
                print("Enter player name "+str(x+1))
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
        while stp != 1:
            player = players[turn]
            printer.print_all(turn,players,name_cards)
            elec = printer.election(names,turn,players)
            if elec == 0: # eleccion que no se puede desafiar o atacar
                player.change_coins(1)
            if elec == 1: # eleccion que no se puede desafiar o atacar
                    player.change_coins(-7)
                    print('which player do you want to hit?')
                    for x in range(len(names)):
                        print(f"{x}) {names[x]}")
                    valu=int(input())
                    play=players[valu]
                    play.raise_card(name_cards) ##crear las cartas, aun falta eso 
            if elec > 1:
                win , chall,participation =printer.priority_challeng(names,turn)  #aca se elige quien desafia 
            else:
                print("\n this action cannot be challenged or countered")
                break
            if elec == 3 and win == 10:
                print ("Tax action not countered, proceeds to be executed")
                player.change_coins(3)
                break
            ve=0
            if elec == 2 or elec == 5 or elec == 4:
                va=1
                if win == 10:
                    print("\n as no one challenged, we proceed to counter attacks")
                    val = printer.counter(names,turn,participation,players,name_cards)  
                else:
                    if chall<l_names:
                        print("we proceed to counter attacks")
                        val = printer.counter(names,turn,participation,players,name_cards)
                if val != 10:
                    win_2 = printer.priority_challeng(names,val)
                    
                if win_2 != 10:
                    print("as two challenges have been generated, it will be chosen when grilling 1")
                    cha = [[win,turn],[win_2[0],val]]
                    ve = random.randint(0,1) #first disorder
                    gg = cha[ve]
                    print(f"the winner to face {names[gg[1]]} is {names[gg[0]]}")
            else:
                va=0
            stop=1
        if elec>2:
            veri_chang=True
            veri_counter=True 
            if ve == 0 and elec >2: #aca vamos a ver los desafio de eleccion 1

                if elec == 3:
                    verification_card = 1
                elif elec == 4:
                    verification_card = 3
                elif elec == 5:
                    verification_card = 5
                elif elec == 6:
                    verification_card = 4
                play_cards=player.cards
                if play_cards[0][1] != verification_card and play_cards[1][1]:
                    print(f'Player {player.name} did not have the card \n')
                    player.raise_card(name_cards)
                    veri_chang=False
                    if val !=10 and va!=0:
                        print("against attack it will not be carried out player {player.name} did not have the letter")
                else:
                    print(f'Player {player.name} did have the card \n')
                    if val != 0:
                        print('the counter attacks will be carried out')
                    play=players[win]
                    print(f'player {play.name} lost the challenge \n')
                    play.raise_card(name_cards)
            if ve==1
            

            




            
                



            
          
        turn += 1
        if turn>len(names)-1:
            turn=0

        
            





    while stop!=1:
        if system.winner!=5:
            print('poner quien gana ')
            stop=1
    
if __name__ == '__main__':
    
    #aca llama funciones
    main()

        

