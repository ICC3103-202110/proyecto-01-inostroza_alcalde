from card import Card 
class Ambassador(Card):
    def __init__(self,name):
           super().__init__(name)
           self.block_exto= True

    @property
    def cards_1(self):
        return self.__cards_1
    
    @cards_1.setter
    def cards_1(self,value,cards_1):
        if len(value)<=2:
            if cards_1[0] == 6 and cards_1[1] == 6:
                 self.__cards_1 = value
            else:
                 self.__cards_1 = [6,6]
        else:
             self.__cards_1
        return

           
    def excahnge_card(self,duke,cards,player,name_cards):
        if duke.block == True:
            all = []
            val = []
            va=2
            cards.delete_card()
            value_1 = cards.s_card
            all.append(value_1)
            cards.delete_card()
            value_2 = cards.s_card
            all.append(value_2)
            p_card = player.cards
            if p_card[0][0] == 1:
                all.append(p_card[0][1])
            else:
                all.append('dead card')
                val.append(2)
                va=1
            if p_card[1][0] == 1:
                all.append(p_card[1][1])
            else:
                all.append('dead card')
                val.append(3) 
                va=1
            if len(val)>0:
                print('Cards already revealed cannot be exchanged\n')
            stop=0
            
            while stop != 1:
                if len(val)>1:
                    stop=1
                    break
                for x in range(len(all)):
                    if x == "dead card":
                        print(str(x)+') '+all[x])
                    else:
                        print(f"{x}) {name_cards[all[x]-1]}")
                valu=int(input())
                if valu in val == True:
                    print('This card is already selected for your deck')
                else:
                    val.append(valu)
                    
           
            
            for x in val:
                if x == 3:
                    if va == 1:
                        c_2=[0,p_card[1][1]]
                    else:
                        c_2=[1,p_card[1][1]]
                elif x == 2:
                    if va == 1:
                        c_1=[0,p_card[0][1]]
                    else:
                        c_1=[1,p_card[0][1]]
                
                if x == 0:
                    c_1=[1,all[val[x]]]
                if x == 1:
                    c_2=[1,all[val[x]]]
                    
            player.cards=[c_1,c_2]
            for x in range(len(all)):
                if x in val == False:
                    cards.add_card(all[x])
        else:
            duke.block= True
        return

    def block_extotion(self):
        self.block_exto= False
        

    def restore(self):
        self.__cards_1 = [6,6]
        return
