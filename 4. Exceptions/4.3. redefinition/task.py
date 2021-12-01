class Person:
    
    def __init__(self, name):
        self.name = name
    
    def breathe(self):
        print('Person can breathe')

    def walk(self):
        print('Person can walk')

    def sleep(self):
        print('Person sleep')       
        
    def combo(self):
        self.breathe()
        self.walk()
        self.sleep()

    def __str__(self):
        return f'Person {self.name}'

    
class Doctor(Person): # subclass
    
    def breathe(self):
        print('Doctor can breathe')
        
    def sleep(self):
        print('Doctor sleep')  
        
    def __str__(self):
        return f'Doctor {self.name}'

d = Doctor('John')
p = Person('Adam')
d.combo()
p.combo()