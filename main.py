
from contessa   import Contessa 
from cards      import Cards 
from captain    import Captain 
from sistem     import System 
from ambassador import Ambassador
from duke       import Duke 
from assassin import Assassin
import prtinter

'''
name in carts
duke = 1
contessa = 2
captain = 3
ambassador = 4
assassin = 5
list=1,2,3,4,5
'''
def cards():
    duke = Duke(1)
    contessa = Contessa(2)
    captain = Captain(3)
    ambassador = Ambassador(4)
    assassin = Assassin(5)
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

      
if __name__ == 'main':
    #aca llama funciones
    pass 

        

