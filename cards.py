import random
class Cards(): #cartas listo 
      def __init__(self,card=0):
             self.card=card

      def create_cards(self): #create a cards
         list_1 = list(range(1,6))
         list_2 = list_1[:]
         list_3 = list_1[:]
         table = list_1+list_2+list_3
         random.shuffle(table) #first disorder
         random.shuffle(table) #second disorder 
         self.cards = table

      def delete_card(self): #para sacar cartas del  mazo
            self.s_card = self.cards[0]
            self.cards.pop(0)
            self.cards
           

      def add_card(self,imp_card):
             self.cards.append(imp_card)
             random.shuffle(self.cards)
             self.cards
            
     
    

