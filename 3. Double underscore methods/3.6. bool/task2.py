class City:
    
    def __init__(self, name):
        self.name = " ".join([x.capitalize() for x in name.split()])
        
    def __str__(self):
        return self.name
    
    def __bool__(self):
        return False if self.name[len(self.name) - 1] in 'a, e, i, o, u' else True

p1 = City('new york')
print(p1)  # печатает "New York"
print(bool(p1))  # печатает "True"
p2 = City('SaN frANCISco')
print(p2)  # печатает "San Francisco"
print(p2 == True)  # печатает "False"