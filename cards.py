import random
class Cards():
      def __init__(self,card=0):
             self.card=card

      def create_cards(self): #create a cards
         list_1 = list(range(1,5+1))
         list_2 = list_1[:]
         list_3 = list_1[:]
         table = list_1+list_2+list_3
         random.shuffle(table) #first disorder
         random.shuffle(table) #second disorder 
         self.cards = table
      def delete_card(self,cards):
            self.card = cards[0]
            cards.pop(0)
            self.cards
           

      def add_card(self,cards,imp_card):
             cards.append(imp_card)
             random.shuffle(cards)
             self.cards
            
     
    

