class Rectange:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __str__(self):
        return f'Rectange with the parties {self.a}x{self.b}:'
        
    def get_area(self):
        return self.a * self.b
    
class Square:
    
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f'Square with the parties {self.a}x{self.a}:'
        
    def get_area(self):
        return self.a ** 2
    
class Circle:
    
    def __init__(self, r):
        self.r = r

    def __str__(self):
        return f'Circle with raduis {self.r}:'
        
    def get_area(self):
        return 3.14 * self.r ** 2

rect1 = Rectange(5, 6)
rect2 = Rectange(4, 8)
sqr1 = Square(5)
sqr2 = Square(7)
cir1 = Circle(3)
cir2 = Circle(2)

figures = [rect1, rect2, sqr1, sqr2, cir1, cir2]
for figure in figures:
    print(figure, figure.get_area())