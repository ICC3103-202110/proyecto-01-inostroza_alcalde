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
        val=self.__coins
        if value==2:
            
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