
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
▀▀ ▄▄ ▀▀ ▄▄ ▀▀ ▄▄ ▀▀ ▄▄   █▀▀ █▀█ █░█ █▀█   ▄▄ ▀▀ ▄▄ ▀▀ ▄▄ ▀▀ ▄▄ ▀▀
▀▀ ░░ ▀▀ ░░ ▀▀ ░░ ▀▀ ░░   █▄▄ █▄█ █▄█ █▀▀   ░░ ▀▀ ░░ ▀▀ ░░ ▀▀ ░░ ▀▀
'''
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
    cards=Cards() #Deck generation
    stop_2=0
    duke = Duke(1)
    contessa = Contessa(2)
    captain = Captain(3)
    ambassador = Ambassador(4)
    assassin = Assassin(5)
    cards.create_cards() 
    while stop_2 !=1: #Player generation
        if stop_2 == 2:
            print ("You have entered an invalid number, please try again")
        print("Select number of players, 3 or 4?\n")
        value= printer.inputverifier(input())
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
                print("Enter player name "+str(x+1))
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
            win=10
            win_2=10
        
            if elec == 0: # Selection cannot be challanged or countered
                player.change_coins(1)
            if elec == 1: # Selection cannot be challanged or countered
                    player.change_coins(-7)
                    print('Which player do you want to hit?')
                    for x in range(len(names)):
                        if turn != x:
                            print(f"{x}) {names[x]}")
                    valu= printer.inputverifier(input())
                    play=players[valu]
                    play.raise_card(name_cards) ##crear las cartas, aun falta eso 
            if elec > 2:
                win , chall,participation =printer.priority_challeng(names,turn)  # Picks challenger priority
            else:
                print("\n this action cannot be challenged or countered")
                break
            '''
            if elec == 3 and win == 10:
                print ("Tax action not countered, proceeds to be executed")
                player.change_coins(3)
                break
            '''
            ve=0
            if elec == 2 or elec == 5 or elec == 4:
                va=1
                if win == 10:
                    print("\n as no one challenged, we proceed to counter attacks")
                    val = printer.counter(names,turn,participation,players,name_cards)  
                    veri_val=val
                else:
                    if chall<l_names:
                        print("we proceed to counter attacks")
                        val = printer.counter(names,turn,participation,players,name_cards)
                        veri_val=val
                if val != 10:
                    win_2 = printer.priority_challeng(names,val)
                    
                if win_2 != 10:
                    print("as two challenges have been generated, it will be chosen when grilling 1")
                    cha = [[win,turn],[win_2[0],val]]
                    ve = random.randint(0,1) #first disorder
                    gg = cha[ve]
                    print(f"the winner to face {names[gg[1]]} is {names[gg[0]]}")
                    stp=1
                    break
            else:
                va=0
            stp=1
        if elec >= 2:
            veri_chang = True
            veri_counter = True
            if val == 10:
                veri_counter == False 
            
            if ve == 0 and elec >2: #Checks challanges for selection 1
                if win != 10:
                    if elec == 3:
                        verification_card = 1
                    elif elec == 4:
                        verification_card = 3
                    elif elec == 5:
                        verification_card = 5
                    elif elec == 6:
                        verification_card = 4
                    play_cards=player.cards
                    
                    if play_cards[0][1] != verification_card and play_cards[1][1] != verification_card: #Doesn't have the card
                        print(f'Player {player.name} did not have the card \n')
                        player.raise_card(name_cards)
                        veri_chang=False
                        if val != 10 and va != 0:
                            print(f"against attack it will not be carried out player {player.name} did not have the card")
                    else:
                        
                        top=0
                        if play_cards[0][1] == verification_card and play_cards[0][0] == 1:
                            top=1
                        if play_cards[1][1] == verification_card and play_cards[1][0] == 1:
                            top=1
                        if top == 1: #aca hay que cambiarle la carta al jugador 
                            print(f'Player {player.name} did have the card {name_cards[verification_card]}\n')
                            player.chang_card(cards,value)
                            cards.add_card(player.del_card)
                            if val != 0:
                                print('the counter attacks will be carried out') # ver este print esta raro
                            play = players[win]
                            print(f'player {play.name} lost the challenge \n')
                            play.raise_card(name_cards)

                        else:
                            print(f'Player {player.name} did not have the card \n')
                            player.raise_card(name_cards)
                            veri_chang = False
                            if val != 10 and va != 0:
                                print(f"against attack it will not be carried out player {player.name} did not have the card")
            if ve == 1: #Challenges counterattacks
                 
                if elec == 2:
                    veri_card_1 = 1
                    veri_card_2 = 0
                elif elec == 5:
                    veri_card_1 = 2
                    veri_card_2 = 0
                elif elec == 4:
                    veri_card_1 = 4
                    veri_card_2 = 3
                play=players[va]
                
                play_cards=play.cards
                top_2 = 0
                if play_cards[0][1] == veri_card_1 or play_cards[0][0] == veri_card_2:
                    if play_cards[0][0] == 1:
                        top_2 = 1
                if play_cards[1][1] == veri_card_1 or play_cards[1][1] == veri_card_2:
                    if play_cards[1][0] == 1:
                        top_2 = 1
                if top_2 == 1:
                    print(f'Player {player.name} did have the card \n') #aca hay que cambiale la carta al jugador 
                    player.chang_card(cards,value)
                    cards.add_card(player.del_card)
                    play_2 = players[win_2]
                    c_1=veri_card_1
                    c_2=veri_card_2
                    print(f'player {play_2.name} lost the challenge \n')
                    play_2.raise_card(name_cards)
                if top_2 == 0:
                    print(f'Player {player.name} did not have the card \n')
                    play.raise_card(name_cards)
                    veri_counter = False
                    print('contra ataque no se llevara acabo')
            if veri_counter == True:
                if c_1 == 1:
                    duke.block_help
                if c_1 == 5:
                    contessa.block_killer
                if c_1 == 4:
                    Ambassador.block_extotion
                if c_2 == 3:
                    captain.block_extotion

            if veri_chang == True:
                if elec == 3:
                    duke.plus_tax

                if elec == 4:
                    print('which player do you want to extort?')
                    for x in range(len(names)):
                        if turn != x:
                            print(f"{x}) {names[x]}")
                    valu= printer.inputverifier(input())
                    play=players[valu]
                    captain.extortion(ambassador,player,play)

                if elec == 2:
                    if duke.block == True:
                        player.change_coins(2)
                    else:
                        duke.block = True

                if elec == 5:
                    print('which player do you want to murder?')
                    for x in range(len(names)):
                        if turn != x:
                            print(f"{x}) {names[x]}")
                    valu= printer.inputverifier(input())
                    play=players[valu]
                    assassin.killer(player,contessa,play,name)

                if elec == 6:
                    ambassador.exchange_card(duke,cards,player,name_cards)


                




                
                

            
                

            

            




            
                



            
          
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

        

