class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        return isinstance(other, Point) and\
    self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))

p3 = Point(3, 4)
p4 = Point(3, 4)
p5 = Point(7, 8)

print(p3 == p4)
print(p4 == p5)
print(hash(p3))
print(hash(p4))
print(hash(p5))