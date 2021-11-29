# 1 вариант: обращения через self
    
class DepartmentIT:
    python_dev = 2
    go_dev = 3
    react_dev = 4
    
    def make_backend(self):
        print(f'Количество backend разработчиков: python - {self.python_dev}, go - {self.go_dev}')
              
    def make_frontend(self):
        print(f'Количество frontend разработчиков: react - {self.react_dev}') 

it1 = DepartmentIT()
it1.make_backend()

# 2 вариант: обращения через DepartmentIT

class DepartmentIT:
    python_dev = 2
    go_dev = 3
    react_dev = 4
    
    def make_backend(self):
        print(f'Количество backend разработчиков: python - {DepartmentIT.python_dev}, go - {DepartmentIT.go_dev}')
              
    def make_frontend(self):
        print(f'Количество frontend разработчиков: react - {DepartmentIT.react_dev}') 

it2 = DepartmentIT()
it2.make_backend()

# 3 вариант: обращения через @property

class DepartmentIT:
    python_dev = 2
    go_dev = 3
    react_dev = 4
    
    @property
    def make_backend(self):
        print(f'Количество backend разработчиков: python - {self.python_dev}, go - {self.go_dev}')
    
    @property              
    def make_frontend(self):
        print(f'Количество frontend разработчиков: react - {self.react_dev}') 

it3 = DepartmentIT()
it3.make_backend

# 4 вариант: обращения через @classmethod, @staticmethod 

class DepartmentIT:
    python_dev = 2
    go_dev = 3
    react_dev = 4
    
    @classmethod 
    def make_backend(cls):
        print(f'Количество backend разработчиков: python - {cls.python_dev}, go - {cls.go_dev}')
    
    @staticmethod        
    def make_frontend():
        print(f'Количество frontend разработчиков: react - {DepartmentIT.react_dev}') 

it4 = DepartmentIT()
it4.make_backend()
it4.make_frontend()
DepartmentIT.make_backend()
DepartmentIT.make_frontend()