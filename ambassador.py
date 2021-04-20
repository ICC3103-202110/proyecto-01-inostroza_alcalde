from card import Card 
class Ambassador(Card):
    def __init__(self,name):
           super().__init__(name)

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

           
    def excahnge_card(self,value_1,value_2):
        cards=[value_1,value_2]
        self.__cards_1 = cards #ver por que se cae esto  !!
        return

    def block_extotion(self):
        self.block_exto= False
        

    def restore(self):
        self.__cards_1 = [6,6]
        return
