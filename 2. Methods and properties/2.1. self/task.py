class Cat:
    breed = 'pers'
    def hello(*args):
        print('Hello world from kitty', args)
        
    def show_breed(self):
        print(f'my breed is {self.breed}')
    
    def show_name(self):
        if hasattr(self, 'name'):
            print(f'my name is {self.name}')
        else:
            print('nothing')
            
    def set_value(self, value, age=0):
        self.value = value
        self.age = age
        print(f'My value is {self.value}. My age is {self.age}')
        
    def new_method(self):
        print(self)

tom = Cat()
tom.hello('Tom', 'Mia', 'Jerry')
tom.show_breed()
tom.show_name()
tom.set_value('Tom')
tom.new_method()