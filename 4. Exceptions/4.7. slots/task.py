from timeit import timeit

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class PointSlors:
    
    __slots__ = ('x', 'y')
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def make_cls1():
    sec = Point(3, 4)
    sec.x = 100
    sec.x
    del sec.x
    
def make_cls2():
    sec = PointSlors(3, 4)
    sec.x = 100
    sec.x
    del sec.x

print(timeit(make_cls1))
print(timeit(make_cls2))