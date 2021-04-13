class Player():
    def __init__(self,name,coins,cards): #las cartas van a cambiar mucho, creo que no vale la pena que sean privadas 
        self.__name=name
        self.__coins=coins
        self.__cards=cards
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
            self.__coins = 0 #ver por que esto da error
        else:
            self.__coins += value

    @life.setter
    def life(self,value,__life):
        if self.__life == True:
             self.__life = False

    def raise_card(self):
        value = int(input("enter the position of the card you want to turn"))
        self.cards[value][0] = 0
        self.cards 

    def end_game(self):
        self.life = False
        self.life = False

    def change_coins(self,value):
        val=self.coins
        self.coins = value
        if val-value < 0:
            return 1
        else:
            return 2 
        return 
    


    @property
    def cards(self):
        return self.__cards
'''
    @cards.setter
    def cards(self,value):
        if (len(self.cards)<=2):
            if (value[0] == 0):

'''


        
    # de atributods va a tener sus dos cartas y las monedas 