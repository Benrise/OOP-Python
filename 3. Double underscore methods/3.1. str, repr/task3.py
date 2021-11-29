class Vector:
    
    def __init__(self, *args):
        self.values = [x for x in args if isinstance(x, int)]

    def __str__(self):
        if len(self.values) > 0:
            return f'Вектор{tuple(sorted(self.values))}'
        else:
            return 'Пустой вектор'

v1 = Vector(1,2,3, 2.0)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2) # печатает "Пустой вектор"