
def election(names,turn):
    print(names[turn-1])
    print(
        " Selections played:       \n "
        '0) CLAIM INCOME           \n'
        '1) HIT ONOTHER PLAYER     \n'
        '2) FOREIGN AID            \n'
        '3) START EXTORTION        \n'
        '4) COMMIT MURDER          \n'
        '5) START TRADE CARDS           \n'
        )
    value = int(input())
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

def challenge_message (name):
    print(f"The player {name} has challenged your choice")

def counter_messenge (name,card):
    print(f"The player {name} has made a counter attack at your choice, he claims to have {card}")

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

def verification_counter(name,value):
    if value == True:
        print("No one has attack you")
    else:
        print(f"The player {name} has attacked your decision")


def priority_challeng(names,turn):
    print("challenge priority is set, who of you dares to challenge player " + names[turn-1])
    if turn<=len(names):
        print("0) "+names[turn])





