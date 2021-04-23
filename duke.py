from card import Card
class Duke(Card): #Duke ready
    def __init__(self,name):
       super().__init__(name)
       self.block = True

    def block_help(self):
         self.block = False  #Needs to be changed outside the class
         
    def plus_tax(self,player):
         player.change_coins(3)
    # Duke Methods