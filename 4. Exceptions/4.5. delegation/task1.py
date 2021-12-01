class Person:
    
    def __init__(self, name, surname, age = 50):
        self.name = name
        self.surname = surname
        self.age = age
    
    def __str__(self):
        return f'Person {self.name} {self.surname}'
        
    def info(self):
        print('Parent class')
        print(self)
        
    
class Doctor(Person): # subclass

    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age
    
    def __str__(self):
        return f'Doctor {self.name} {self.surname}'

p = Person('Ivan', 'Ivanov')
d = Doctor('Petr', 'Petrov', 25)
print(p.name, p.surname, p.age)
print(d.name, d.surname, d.age)