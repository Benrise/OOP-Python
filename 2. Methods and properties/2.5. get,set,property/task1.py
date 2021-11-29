class BankAccount:   
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        
    def get_balance(self):
        print('get balance')        
        return self.__balance
    
    def set_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value
        
    def del_balance(self):
        print('delete balance')
        del self.__balance   
        
    balance = property(fget=get_balance, fset=set_balance, fdel=del_balance) # свойство класса
    
d = BankAccount('Nasty', 500)
d.balance
d.balance = 550
del d.balance
d.balance = 450
d.balance




