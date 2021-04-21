class Player():
    def __init__(self,name,coins,cards): #las cartas van a cambiar mucho, creo que no vale la pena que sean privadas 
        self.__name=name
        self.__coins=coins
        self.cards=cards #cambiar esto si lo quiero hacer privado 
        self.__life=True

    @property
    def name(self):
        return self.__name

    @property
    def coins(self):
        return self.__coins

    @property
    def life(self):
        return self.__life

    @coins.setter
    def coins(self,value,__coins):
        if (self.coins + value) < 0:
            self.__coins = 0 
        else:
            self.__coins += value

    @life.setter
    def life(self):
        life=self.__life
        if life == True:
             self.__life = False
        else:
            self.__life

    def raise_card(self,names_cards): 
        cards=self.cards
        stop=0
        while stop !=1 :
            values=[]
            if cards[0][0]==1:
                print(f"0) {names_cards[cards[0][1]-1]}")
                values.append(0)
            if cards[1][0] == 1:
                print(f"1) {names_cards[cards[1][1]-1]} \n")
                values.append(1)
            val = input("enter the position of the card you want to turn: \n")
            if val == '1' or val=='0':
                value=int(val)
                if cards[value][0]==1:
                    stop=1
                    break
                else:
                    print('selected card is no longer in your deck, try again')
            else:
                print('wrong embedded value')
        cards[value][0] = 0
        self.cards =cards

    def end_game(self):
        cards=self.cards
        if cards[0][0] == 0 and cards[1][0] == 0:
            self.life = False
        self.life

    def change_coins(self,value): #esto de aca se deberia cambiar creo, pasa usar el setter 
        val=self.__coins
        if value==-2:
            
            if val+value < 0:
                self.__coins=0
                return 1
            else:
                self.__coins=val+value
                return 2 
            return 
        else:
            if val+value < 0:
                    self.__coins=0
            else:
                self.__coins=val+value

    def chang_card(self,cards_1,value):
        cards=self.cards
        if cards[0][1] == value and cards[0][0] == 1:
            self.del_card=cards[0][1]
            cards_1.delete_card
            cards[0][1] = cards_1.s_card
            
        if cards[1][1] == value and cards[1][0] == 1:
            self.del_card=cards[1][1]
            cards_1.delete_card
            cards[1][1] = cards_1.s_card
        self.cards=cards


            

'''   
   por ahora las cartas son no privadas, despues cver como las hago privadas 
    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self,value):
        if (len(self.cards)<=2):
            if (value[0] != 0):

'''



        
    # de atributods va a tener sus dos cartas y las monedas 