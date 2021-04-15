from card import Card
class Captain(Card):
    def __init__(self,name):
           super().__init__(name)
           
    def extortion (self,player,player_2): #pleyer dos es al que le van a robar 
        if self.block_exto!=False:
            coins= player_2.change_coins(-2)
            player.player.change_coins(coins)
        else:
            self.block_exto=False
        

    def block_extotion(self):
        self.block_exto=False
        
        #metodos del capitan