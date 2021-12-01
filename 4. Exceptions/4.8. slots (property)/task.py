class Rectangle:
    __slots__ = '__width', 'height'
    
    def __init__(self, a, b):
        self.width = a
        self.height = b
        
    @property # getter
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        print('setter called')
        self.__width = value
        
class Square(Rectangle):
        __slots__ = 'color'
        def __init__(self, a, b, color):
            super().__init__(a, b)
            self.color = color

c = Square(4, 5, 'red')
c.width, c.height, c.color