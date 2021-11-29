class Robot:
    population = 0
    
    def __init__(self, name):
        self.name = name
        print(f'Робот {self.name} был создан')
        Robot.population += 1
        
    def destroy(self):
        Robot.population -= 1        
        print(f'Робот {self.name} был уничтожен')
        
    def say_hello(self):
        print(f'Робот {self.name} приветствует тебя, особь человеческого рода')
    
    @classmethod  
    def how_many(cls):
        print(f'{cls.population}, вот сколько нас еще осталось')

r2 = Robot("R2-D2") # печатает "Робот R2-D2 был создан"
r2.say_hello() # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
Robot.how_many() # печатает "1, вот сколько нас еще осталось"
r2.destroy() # печатает "Робот R2-D2 был уничтожен"