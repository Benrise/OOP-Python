class Initialization:
    
    def __init__(self, capacity, food):
        if isinstance(capacity, int):
            self.capacity = capacity
            self.food = food
        else:
            print('Количество людей должно быть целым числом')
            
class Vegetarian(Initialization):
    
    def __init__(self, capacity, food):
        super().__init__(capacity, food)
        
    def __str__(self):
        return f'{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}'
    
class MeatEater(Initialization):
    
    def __init__(self, capacity, food):
        super().__init__(capacity, food)
        
    def __str__(self):
        return f'{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}'
    
class SweetTooth(Initialization):
    
    def __init__(self, capacity, food):
        super().__init__(capacity, food)
        
    def __str__(self):
        return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}'
        
    def comparison(self, other, func):
        if isinstance(other, int):
            return func(self.capacity, other)
        elif isinstance(other, (Vegetarian, MeatEater)):
            return func(self.capacity, other.capacity)
        else:
            return 'Невозможно сравнить количество сладкоежек с {other}'
    
    def __eq__(self, other):
        return self.comparison(other, lambda x, y: x == y)
    
    def __lt__(self, other):
        return self.comparison(other, lambda x, y: x < y)
        
    def __gt__(self, other):
        return self.comparison(other, lambda x, y: x > y)    


v_first = Vegetarian(10000, ['Орехи', 'овощи', 'фрукты'])
print(v_first)  # 10000 людей предпочитают не есть мясо! Они предпочитают ['Орехи', 'овощи', 'фрукты']
v_second = Vegetarian([23], ['nothing'])  # Количество людей должно быть целым числом
m_first = MeatEater(15000, ['Жареную картошку', 'рыба'])
print(m_first)  # 15000 мясоедов в Москве! Помимо мяса они едят еще и ['Жареную картошку', 'рыба']
s_first = SweetTooth(30000, ['Мороженое', 'Чипсы', 'ШОКОЛАД'])
print(s_first)  # Сладкоежек в Москве 30000. Их самая любимая еда: ['Мороженое', 'Чипсы', 'ШОКОЛАД']
print(s_first > v_first)  # True
print(30000 == s_first)  # True
print(s_first == 25000)  # False
print(100000 < s_first)  # False
print(100 < s_first)  # True