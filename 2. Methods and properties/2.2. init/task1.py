class Zebra:
    
    def __init__(self):
        self.color = 0
        
    def which_stripe(self):
        if self.color == 0:
            print("Полоска белая")
            self.color = 1
            return
        if self.color == 1:
            print("Полоска черная")
            self.color = 0
            return
z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe() # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe() # печатает "Полоска белая"