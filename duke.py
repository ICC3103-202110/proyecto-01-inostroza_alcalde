from card import Card
class Duke(Card): #duke esta listo 
    def __init__(self,name):
       super().__init__(name)

    def block_help(self):
         self.block=False  #se va a necesitar cambiarse fuera de la clase 
    def plus_tax(self):
         self.tax = True
    # metodos definidos para el duke 