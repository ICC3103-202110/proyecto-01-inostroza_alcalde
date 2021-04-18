#este archivo tiene cosas que se imprimen basicas, hace verificaciones basicas, pero nunca altera a clases
import random
def election(names,turn,players):
    player=players[turn]
    stop=0
    while stop!=1:
        actions=['CLAIM INCOME','HIT ANOTHER PLAYER','FOREIGN AID','GENERATE TAX',
                'START EXTORTION','COMMIT MURDER','START TRADE CHANGE']
        print("      player " +names[turn])
        print(" Selections played:")
        for x in range(7):
            print(str(x)+") "+ actions[x])
        value = int(input())
        if value == 1:
            if player.coins>=7:
                stop=1
            else:
                print("INSUFFICIENT COINS TO FULFILL THIS ACTION, PLEASE CHOOSE ANOTHER ACTION \n\n")
        else:
            stop=1

    print(names[turn]+" has chosen "+actions[value])
    return value

def answer(name,value):
    actions=['CLAIM INCOME','FOREIGN AID',
             'START EXTORTION','COMMIT MURDER','START CHANGE', 
             'BLOCKING EXTORTION','BLOCKING KILLER','BLOCKING FOREIGN AID']

    print(f"the player {name} has chosen {actions[value]} \n")
    print(
        "What would you like to do ? ")
    if value>2:
        print("0) TO CHALLENGE             \n")
    if value <5:
        print(f"1) COUNTER                  \n")
    res=int(input())
    return res
'''
def challenge_message (name):
    print(f"The player {name} has challenged your choice")

def counter_messenge (name,card):
    print(f"The player {name} has made a counter attack at your choice, he claims to have {card}")
'''
def result_counter (value):
    if value == True:
        print("Youe win the counter attack")
    else:
        print("You lose the counter attack")

def result_challenge(name,value):
    if value == True:
        print(f"You lose the challenge, the player {name} had the character")
    else:
        print(f"You win the challenge, the player {name} no had the character")
'''
def verification_counter(name,value):
    if value == True:
        print("No one has attack you")
    else:
        print(f"The player {name} has attacked your decision")
'''

def priority_challeng(names,turn): #esto ya esta listo
    participation=[]
    print("challenge priority is set, who of you dares to challenge player " + names[turn] +" ?")
    for x in range(len(names)):
        if x != turn:
            print(f"{x}) {names[x]}")

    print("10) We are all chickens")
    value_1=int(input())  #este int deberia ser aprueba de error aun no lo es 
    if value_1 == 10:
        print("from here I can see their feathers falling")
        return 10 , 0, 0
    else:
        stop=0
        cha=[]
        participation.append(value_1)
    while stop!=1:
        if len(names)>3:
            stop=1
            for y in range(len(names)):
                print()
                if y !=turn and y != value_1: #no recuerdo para que servia esto, revisar 
                    print(names[y])
            print("are they chickens? won't they challenge it?")
            for y in range(len(names)):
                if y !=turn and y != value_1:
                    print(str(y)+') '+names[y])
            print("10) We are all chickens")
            value_2=int(input())  #este int deberia ser aprueba de error aun no lo es 
            if value_2 == 10:
                
                return value_1 , len(cha),participation
            else:
                cha.append(value_1)
                cha.append(value_2)
                participation.append(value_2)
            for y in range(len(names)):
                    if y !=turn and y != value_1 and y != value_2:
                        print('player '+names[y]+ ' going to challenge? \n'
                        '0) NO \n'
                        '1) YES \n')
                        v=int(input())  #este int deberia ser aprueba de error aun no lo es 
                        if v== 1:
                            cha.append(y)
        else:
            stop=1
            for y in range(len(names)):
                    if y !=turn and y != value_1:
                        print('player '+names[y]+ ' going to challenge? \n'
                        '0) NO \n'
                        '1) YES \n')
                        v=int(input())  #este int deberia ser aprueba de error aun no lo es 
                        if v== 1:
                            cha.append(value_1)
                            cha.append(y)
                            participation.append(y)
                        else:
                            return value_1 , len(cha),participation
        print("It seems that we have more than one brave, the challenge refers")
        random.shuffle(cha) #first disorder
        win=cha[0]
        print("the winner to face "+names[turn]+" is "+names[win])
        return win,len(cha),participation

def counter(names,turn,participation,players,name_cards):
    print()
    stop=0
    while stop!=1:
        print("\n who wishes to counter attack") #aca igual se podria decir que es cada cosa de contra ataque 
        print(turn)
        for x in range(len(names)):
            if x != turn:
                ve=x in participation
                if  ve != True:
                    print(f'{x}) {names[x]}')
        print("10) We are all chickens")
        value_1=int(input())  #este int deberia ser aprueba de error aun no lo es 
        if value_1 == 10:
            print("from here I can see their feathers falling")
            stop=1
            return 10
        
        else: 
            print(f'{names[value_1]} these are your cards:')
            play=players[value_1]
            cards_1=play.cards
            for x in cards_1:
                if x[0]==0:
                    val=name_cards(x[1]-1)
                    print('\t- '+strike(val))
                else:
                    print('\t- '+name_cards[x[1]-1])
            print("are you sure you want to fight back")
            print("0) NO\n1) YES")
            confi=int(input())
            if confi == 1:
                stop = 1
    return value_1

def strike(text):   #https://www.javaer101.com/es/article/14726975.html
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

def print_all(turn,players,name_cards):  #imprime cartas de todos y monedas 
    name_cards.append("******")
    play=players[turn]
    cards_1=play.cards
    coin_1=play.coins
    print()
    print("NAME PLAYER             COINS                            CARDS")
    for x in range(len(players)):
        player=players[x]
        if x != turn:
            c=player.cards
            car_1=c[0]
            car_2=c[1]
            if car_1[0] == 1:
                car_1[1] = 5
            else:
                car_1[1]-=1

            if car_2[0] == 1:
                car_2[1]=5
            else:
                car_2[1]-=1
            print(f"%9s               {player.coins}                            {name_cards[car_1[1]]} , {name_cards[car_2[1]]} " %player.name)
    print(f'\nyour coins: {coin_1}')
    print("your cards in play: ")
    for x in cards_1:
        if x[0]==0:
            val=name_cards(x[1]-1)
            print('\t- '+strike(val))
        else:
            print('\t- '+name_cards[x[1]-1])
    print('\n')

            


                


                        
            





        

   




