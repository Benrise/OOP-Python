class Cat:
    __shared_attr = {
        'breed': 'pers',
        'color': 'black'
    }
    
    def __init__(self):
        self.__dict__ = Cat.__shared_attr
        print(self.__dict__)

d = Cat()
g = Cat()
d.breed = 'siam'
d.name = 'Bob'
d = Cat()