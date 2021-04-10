

def winner(player_1,player_2,player_3,player_4=0):
    if (player_4 == 0):
        lifes=[]
        lifes.append(player_1.life)
        lifes.append(player_2.life)
        lifes.append(player_3.life)
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
            if(lifes[stop] == 1):
                return stop
            stop+=1
        


        

