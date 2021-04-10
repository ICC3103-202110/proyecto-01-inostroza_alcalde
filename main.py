
from contessa   import Contessa 
from cards      import Cards 
from captain    import Captain 
from sistem     import Sistem 
from ambassador import Ambassador 
from duke       import Duke 
import printer
'''
name in carts
duke = 1
contessa = 2
captain = 3
ambassador = 4
assassin = 5

'''
def cards():
    duke = Duke(1)
    contessa = Contessa(2)
    captain = captian(3)
    ambassador = ambassador(4)
    assassin = assassin(5)
    diferent_card=[duke,contessa,captain,ambassador,assassin]
    return diferent_card

def winner(player_1,player_2,player_3,player_4=0):
    try:
        if player_4 == 0:
            lifes=[]
            lifes.append(player_1.life)
            lifes.append(player_2.life)
            lifes.append(player_3.life)
    except:
        else:
            lifes=[]
            lifes.append(player_1.life)
            lifes.append(player_2.life)
            lifes.append(player_3.life)
            lifes.append(player_4.life)
    if sum(lifes)>1:
         return False
    else :
         stop=0
         while stop<len(lifes):
            if lifes[stop] == 1:
                return stop
            stop+=1

def         
if __name__ == 'main':
    #aca llama funciones
    pass 

        

