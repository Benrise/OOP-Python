class Mark:
    def __init__(self, values):
        self.value = values
        self.index = 0

    def __iter__(self):
        return self        
        
    def __next__(self):
        print('call next_ Mark')
        if self.index >= len(self.value):
            self.index = 0
            raise StopIteration
        letter = self.value[self.index]
        self.index += 1
        return letter
        
class Student:
    
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks
    
    def __iter__(self):
        print('call_iter')
        self.index = 0
        return iter(self.marks)
    
    def __next__(self):
        print('call next Student')
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter
        
m = Mark([1, 2, 3, 4])   
igor = Student('igor', 'Nikolaev', m)

for i in igor:
    print(i)