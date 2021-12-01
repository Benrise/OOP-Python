class Person:
    
    def can_breathe(self):
        print('I can breathe')
        
    def can_walk(self):
        print('I can walk')

class Doctor(Person):
    
    def can_cure(self):
        print('I can heal')
        
class Ortoped(Doctor):
    
    def can_scoliosis(self):
        print('I can heal diseases of the musculoskeletal system')
        print('Ortoped subclass Doctor and Person')
        
class Architect(Person):
    
    def can_build(self):
        print('I can build a house')

ort = Ortoped()
ort.can_breathe()
d = Doctor()
d.can_cure()
d.can_breathe()
d.can_walk()
a = Architect()
a.can_build()
a.can_breathe()
a.can_walk()