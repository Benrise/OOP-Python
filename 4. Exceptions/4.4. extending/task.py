class Person:
    def breathe(self):
        print('Person can breathe')


    def sleep(self):
        print('Person sleep')       
        
    def combo(self):
        self.breathe()
        if hasattr(self, 'walk'):
            self.walk()
        self.sleep()

    
class Doctor(Person): # subclass
    def breathe(self):
        print('Doctor can breathe')
        
    def sleep(self):
        print('Doctor sleep')  

    def walk(self):
        print('Doctor can walk')

d = Doctor()
p = Person()
d.combo()
p.combo()