# Задача: необходимо вычислить площать квадрата
# Условия: 
# 1. При изменении стороны экземпляра меняется площадь квадрата.
# 2. При уже вычисленном значении площади повторно не вычисляем, возвращаем уже вычисленное

class Square:
    def __init__(self, s):
        self.__side = s
        self.__area = None
        
    @property
    def side(self):
        return self.__side
    
    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None
        
    @property
    def area(self):
        if self.__area is None:
            print('calculate area')
            self.__area = self.__side**2
        return self.__area

a = Square(10)
print(a.area)
a.side = 12
print(a.area)