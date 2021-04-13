class Player():
    def __init__(self,name,coins,cards,life): #las cartas van a cambiar mucho, creo que no vale la pena que sean privadas 
        self.name=name
        self.__coins=coins
        self.__cards=cards
        self.__life=life

    @property
    def name(self):
        return self.__name

    @property
    def coins(slef):
        return self.__coins

    @property
    def life(slef):
        return self.__life

    @coins.setter
    def coins(self,value):
        if (self.coins + value) < 0:
            self.__coins = 0 #ver por que esto da error
        else:
            self.__coins += value

    @life.setter
    def life(self,value):
        if self.__life == 1:
             self.__life = 0
'''

    @property
    def cards(slef):
        return self.__cards

    @cards.setter
    def cards(self,value):
        if (len(self.cards)<=2):
            if (value[0] == 0):
'''

    def raise_card(self):
        value = int(input("enter the position of the card you want to turn"))
        self.cards[value][0] = 0
        return self.cards 

    def end_game(self):
        return self.life = 0

    def change_coins(self,value):
        val=self.coins
        self.coins = value
        if val-value < 0:
            return 1
        else:
            return 2 
        return 



        
    # de atributods va a tener sus dos cartas y las monedas 