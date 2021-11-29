class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
    def __len__(self):
        return len(self.name + self.surname)
    
class Segment:
    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2
        
    def __len__(self):
        return abs(self) # self.__abs__()
    
    def __abs__(self):
        return abs(self.x2 - self.x1)

person = Person('Ivan', 'Ivanov')
print(len(person))
print(person.__len__())

segment = Segment(10, 6)
print(len(segment))
print(abs(segment))