import random
class Cards(): #Cards Ready
      def __init__(self,card=0):
             self.card=card

      def create_cards(self): #Creates cards
         list_1 = list(range(1,6))
         list_2 = list_1[:]
         list_3 = list_1[:]
         table = list_1+list_2+list_3
         random.shuffle(table) #first disorder
         random.shuffle(table) #second disorder 
         self.cards = table

      def delete_card(self): #To pick cards out of the deck
            cards=self.cards
            self.s_card = cards[0]
            cards.pop(0)
            self.cards=cards
           

      def add_card(self,imp_card):
             self.cards.append(imp_card)
             random.shuffle(self.cards)
             self.cards
            
     
    

