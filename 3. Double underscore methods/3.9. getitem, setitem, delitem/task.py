class Vector:   
    
    def __init__(self, *args):
        self.values = list(args)
        
    def __repr__(self):
        return str(self.values)
    
    def __getitem__(self, item):
        if 0 <= item < len(self.values):
            return self.values[item]
        else:
            IndexError('Индекс за границами нашей коллекции')
            
    def __setitem__(self, key, value):
        if 0 <= key < len(self.values):
            self.values[key] = value
        elif key > len(self.values):
            diff = key - len(self.values)
            self.values.extend([0] * diff) # разряженный массив
            self.values[key-1] = value
        else:
            IndexError('Индекс за границами нашей коллекции')  
            
    def __delitem__(self, key):
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            IndexError('Индекс за границами нашей коллекции') 

v5 = Vector(6, 7)
v5[5] = 10
print(v5)