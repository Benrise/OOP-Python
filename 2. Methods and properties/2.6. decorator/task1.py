class BankAccount:
    
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    
    @property # my_balance = property(my_balance) - свойство
    def my_balance(self):
        print('get balance')        
        return self.__balance
    
    # my_property = my_balance
    
    @my_balance.setter # my_balance = my_property.setter(my_balance)
    def my_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value  
        
    @my_balance.deleter
    def my_balance(self):
        print('delete balance')
        del self.__balance  

g = BankAccount('Ily', 1000)
print(g.my_balance)
g.my_balance = 2000
print(g.my_balance)
del g.my_balance