class Lion:
    
    def __init__(self, name):
        self.name = name
    
    # вывод для разработчиков
    def __repr__(self):
        return f'__repr__ - {self.name}'
    
    # вывод для пользователей  
    def __str__(self):
        return f'__str__ - {self.name}' 

x = Lion('Simba')
x
print(x)