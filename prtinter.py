def election():
    print(
        " Selections played:       \n "
        '0) CLAIM INCOME           \n'
        '1) FOREIGN AID            \n'
        '2) HIT ONOTHER PLAYER     \n'
        '3) START EXTORTION        \n'
        '4) COMMIT MURDER          \n'
        '5) START CHANGE           \n'
        )
    value = int(input())
    return value

def answer(name,value):
    actions=['CLAIM INCOME','FOREIGN AID','HIT ONOTHER PLAYER',
             'START EXTORTION','COMMIT MURDER','START CHANGE', 
             'BLOCKING EXTORTION','BLOCKING KILLER','BLOCKING FOREIGN AID']

    print(f"the player {name} has chosen {actions[value]} \n")
    print(
        "What would you like to do ? \n"
        "0) TO CHALLENGE             \n")
    if value <5:
        print(f"1) COUNTER                  \n")
    res=int(input())
    return res

def challenge_message (name):
    print(f"The player {name} has challenged your choice")

def counter_messenge (name,card):
    print(f"The player {name} has made a counter attack at your choice, he claims to have {card}")

