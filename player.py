class Player():
    def __init__(self,name,coins,cards): #Cards will change a lot, so it's not necessary to make them private
        self.__name=name
        self.__coins=coins
        self.cards=cards #Change this if you want to make it private
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
    def life(self,Value):
        if Value == False:
            self.__life = Value
        life=self.__life
        if life == True:
             self.__life = False
        else:
            self.__life

    def raise_card(self,name_cards): 
        print(f'Player {self.name}, select a letter to delete:')
        cards=self.cards[:]
        stop=0
        while stop !=1 :
            values=[]
            if cards[0][0]==1:
                c_1=cards[0][1] -1
                print(f"0) {name_cards[c_1]}")
                values.append(0)
            if cards[1][0] == 1:
                c_2=cards[1][1] -1
                print(f"1) {name_cards[c_2]} \n")
                values.append(1)
            val = input("Enter the position of the card you want to turn: \n")
            if val == '1' or val=='0':
                value=int(val)
                if cards[value][0]==1:
                    stop=1
                    break
                else:
                    print('Selected card is no longer in your deck, try again')
            else:
                print('Wrong embedded value')
        cards[value][0] = 0
        self.cards = cards
        return

    def End_game(self,value):
        print(value)
        cards=self.cards
        if cards[0][0] == 0 and cards[1][0] == 0:
            self.life = value
        else:
            self.life
        return
       

    def change_coins(self,value): #This should be changed, to use the setter
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
   For now cards are not private.
    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self,value):
        if (len(self.cards)<=2):
            if (value[0] != 0):

'''