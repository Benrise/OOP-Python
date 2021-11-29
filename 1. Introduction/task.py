class Car: # класс
    model = 'BMW' # атрибуты класса
    engine = 1.6
    
    def drive(): # метод класса
        print("Let's go")

example = Car() # экземпляр класса

# обращение к атбрибуту через класс или экземпляр
print(Car.model) 
print(example.model)

# вызов ф-ии через класс
Car.drive()
getattr(Car, 'drive')()

# создание и изменение значения атрибута
Car.model = 'new model'
Car.new_attribute = 'creation_new_attribute'
setattr(Car, 'new_attr', 'change_new_attr')

# удаление атрибута
del Car.new_attribute
delattr(Car, 'new_attr')

# посмотреть атрибуты класса или экземпляра
print(Car.__dict__) 
print(example.__dict__)