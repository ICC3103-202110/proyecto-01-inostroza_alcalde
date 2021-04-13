from contessa   import Contessa 
from cards      import Cards 
from captain    import Captain 

from ambassador import Ambassador
from duke       import Duke 
from assassin import Assassin
import printer
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
        if player_4 != 0:
            lifes=[]
            lifes.append(player_1.life)
            lifes.append(player_2.life)
            lifes.append(player_3.life)
            lifes.append(player_4.life)
    except:
        lifes=[]
        lifes.append(player_1.life)
        lifes.append(player_2.life)
        lifes.append(player_3.life)
                
    if sum(lifes)>1:
        return 5
    else :
        stop=0
        while stop<len(lifes):
            if lifes[stop] == 1:
                return stop  #retorna lugar del ganador 
            stop+=1






            

