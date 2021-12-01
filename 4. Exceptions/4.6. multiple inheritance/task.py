class Doctor():
    
    def __init__(self, degree):
        self.degree = degree
        
class Builder:
    
    def __init__(self, rank):
        self.rank = rank    

class Person(Doctor, Builder):
    
    def __init__(self, degree, rank):
        super().__init__(degree) # делегирование Doctor
        Builder.__init__(self, rank) # делегирование Builde
        
    def __str__(self):
        return f'Person {self.degree}, {self.rank}'

per = Person(5, 'spec')
print(per)