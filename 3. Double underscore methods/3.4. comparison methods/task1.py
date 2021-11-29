# __eq__ - ==
# __ne__ - !=
# __lt__ - <
# __le__ - <=
# __gt__ - >
# __ge__ - >=

class Rectange:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    # вычисляем площадь прямоугольника    
    @property 
    def area(self):
        return self.a * self.b
    
    def __eq__(self, other):
        print('__eq__call')
        if isinstance(other, Rectange):
            return self.a == other.a and self.b == other.b
        
    def __lt__(self, other):
        print('__lt__call')
        if isinstance(other, Rectange):
            return self.area < other.area
        elif isinstance(other, (int, float)):
            return self.area < other
        
    def __le__(self, other):
        return self == other or self < other

q = Rectange(5, 5)
s = Rectange(10, 3)
print(q <= s)
print(q >= s)
print(s >= q)
