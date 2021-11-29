class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name 
        self.age = age
    def full_name(self):
        return f'{self.last_name} {self.first_name}'
    def is_adult(self):
        return self.age >= 18

p1 = Person('Jimi', 'Hendrix', 55)
print(p1.full_name())  # выводит "Hendrix Jimi"
print(p1.is_adult()) # выводит "True"