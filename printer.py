import random
#This py is in charge of printing and basic verifications, but it never modifies any class
def startup():
    print(
    '''
▀▀ ▄▄ ▀▀ ▄▄ ▀▀ ▄▄ ▀▀ ▄▄   █▀▀ █▀█ █ █ █▀█   ▄▄ ▀▀ ▄▄ ▀▀ ▄▄ ▀▀ ▄▄ ▀▀
▀▀ ░░ ▀▀ ░░ ▀▀ ░░ ▀▀ ░░   █▄▄ █▄█ █▄█ █▀▀   ░░ ▀▀ ░░ ▀▀ ░░ ▀▀ ░░ ▀▀
    ''')
    print("\nPress any button to start . . .\n")
    input()


# Checks if value is viable until a valid input is entered
def inputverifier(value):
    token = 0
    while token == 0:
        if value == "0" or value == "1" or value == "2" or value == "3" or value == "4" or value == "5" or value == "6" or value == "7" or value == "8" or value == "9" or value == "10":
            value = int(value)
            return value

        else:
            value = input("Invalid input value, please try again\n")
            token = 0

def election(names,turn,players):
    player=players[turn]
    stop=0
    while stop!=1:
        actions=['CLAIM INCOME ★','HIT ANOTHER PLAYER ✖','FOREIGN AID ☻','GENERATE TAX $',
                'START EXTORTION ⍗','ASSASSINATE ⚔','START TRADE CHANGE ⇆']
        print("      player " +names[turn])
        print(" Selections played:")
        for x in range(7):
            print(str(x)+") "+ actions[x])
        print(("---")*30)
        value = inputverifier(input())
        if value == 1:
            if player.coins>=7:
                stop=1
            else:
                print("INSUFFICIENT COINS TO FULFILL THIS ACTION, PLEASE CHOOSE ANOTHER ACTION \n\n")
        elif value != 1 and value != 5:

            stop = 1
        if value == 5:
            if player.coins>2:
                    stop=1
            else:
                print("INSUFFICIENT COINS TO FULFILL THIS ACTION, PLEASE CHOOSE ANOTHER ACTION \n\n")
        elif value != 5 and value!= 1:
        
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
    res=inputverifier(input())
    return res
'''
def challenge_message (name):
    print(f"The player {name} has challenged your choice")

def counter_messenge (name,card):
    print(f"The player {name} has made a counter attack at your choice, he claims to have {card}")
'''
def result_counter (value):
    if value == True:
        print("You win the counter attack")
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

def priority_challeng(names,turn): #Ready
    participation=[]
    print("challenge priority is set, who of you dares to challenge player " + names[turn] +" ?")
    for x in range(len(names)):
        if x != turn:
            print(f"{x}) {names[x]}")

    print("10) We are all chickens")
    print(("---")*30)
    value_1= inputverifier(input())
    if value_1 == 10:
        print("from here I can see their feathers falling")
        return 10 , 0, [10]
    else:
        stop=0
        cha=[]
        participation.append(value_1)
    while stop!=1:
        if len(names)>3:
            stop=1
            print(("---")*30)
            for y in range(len(names)):
                print()
                if y !=turn and y != value_1: #Pending . . .
                    print('player' + names[y])
                    
            print("are they chickens? won't they challenge it?")
            for y in range(len(names)):
                if y !=turn and y != value_1:
                    print(str(y)+') '+names[y])

            print("10) We are all chickens")
            print(("---")*30)
            value_2= inputverifier(input())
            if value_2 == 10:
                
                return value_1 , len(cha),participation
            else:
                cha.append(value_1)
                cha.append(value_2)
                participation.append(value_2)
            print(("---")*30)
            for y in range(len(names)):
                    if y !=turn and y != value_1 and y != value_2:
                        print('player '+names[y]+ ' going to challenge? \n'
                        '0) NO \n'
                        '1) YES \n')
                        print(("---")*30)
                        v= inputverifier(input())
                        if v== 1:
                            cha.append(y)
        else:
            stop=1
            print(("---")*30)
            for y in range(len(names)):
                    if y !=turn and y != value_1:
                        print('player '+names[y]+ ' going to challenge? \n'
                        '0) NO \n'
                        '1) YES \n')
                        print(("---")*30)
                        v= inputverifier(input())
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
        print("\n who wishes to counter attack") #Counter attacks
        for x in range(len(names)):
            if x != turn:
                ve = x in participation
                if  ve != True:
                    print(f'{x}) {names[x]}')
        print("10) We are all chickens")
        value_1= inputverifier(input())
        if value_1 == 10:
            print("from here I can see their feathers falling")
            stop=1
            print(("---")*30)
            return 10
        
        else: 
            print(f'{names[value_1]} these are your cards:')
            play=players[value_1]
            cards_1=play.cards
            for x in cards_1:
                if x[0]==0:
                    val=name_cards[x[1]-1]
                    print('\t- '+strike(val))
                else:
                    print('\t- '+name_cards[x[1]-1])
            print("Are you sure you want to fight back?")
            print("0) NO\n1) YES")
            print(("---")*30)
            confi= inputverifier(input())
            if confi == 1:
                stop = 1
    return value_1

def strike(text):   #https://www.javaer101.com/es/article/14726975.html
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

def print_all(turn,players,name_cards):  #Prints everyone's cards and coins
    print(("---")*30)
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
            cart_1=c[0]
            car_1=cart_1[:]
            cart_2=c[1]
            car_2=cart_2[:]
            if car_1[0] == 1:
                car_1[1] = 5
            else:
                car_1[1]-=1
            if car_2[0] == 1:
                car_2[1]=5
            else:
                car_2[1]-=1
            
            print(f"%9s               {player.coins}                            {name_cards[car_1[1]]} , {name_cards[car_2[1]]} " %player.name)
    print(f"It's {play.name}'s turn")
    print(f'\nyour coins: {coin_1}')
    
    print("Your cards in play: ")
    for x in cards_1:
        if x[0]==0:
            val=name_cards[x[1]-1]
            print('\t- **'+strike(val)+' **')
        else:
            print('\t- '+ str(name_cards[x[1]-1]))
    print('\n')
    





