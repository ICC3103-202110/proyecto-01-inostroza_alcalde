from card import Card
class Captain(Card):
    def __init__(self,name):
           super().__init__(name)
           self.block_exto=True
               
           
    def extortion(self,Ambassador,player,player_2): #pleyer dos es al que le van a robar 
        if self.block_exto != False and Ambassador.block_exto != False:
            coins= player_2.change_coins(-2)
            player.change_coins(coins)
        else:
            self.block_exto=True
            Ambassador.block_exto =True
        

    def block_extotion(self):
        self.block_exto=False
        
        #metodos del capitan