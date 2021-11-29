class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __len__(self):
        print('call__len__')
        return abs(self.x - self.y)
    
    def __bool__(self):
        print('call__bool__')
        return self.x != 0 or self.y != 0

print(bool(Point(3,4)))
print(len(Point(5, 5)))