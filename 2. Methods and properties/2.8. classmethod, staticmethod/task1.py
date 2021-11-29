class Example:
    
    # метод вызывается от класса, но не вызывается от экземпляра
    def hello():
        print('hello')   
    
    # метод вызывается от экземпляра, но не вызывается от класса
    def instance_hello(self):
        print(f'instance hello {self}')  
    
    # метод staticmethod - позволяет обратиться и к классу и к экземпляру
    @staticmethod
    def static_hello():
        print('static hello')
    
    # метод classmethod - передает в аргумент значение класса
    @classmethod    
    def class_hello(cls):
        print(f'class hello {cls}')

Example.static_hello()
y = Example()
y.static_hello()

Example.class_hello()
d = Example()
d.class_hello()