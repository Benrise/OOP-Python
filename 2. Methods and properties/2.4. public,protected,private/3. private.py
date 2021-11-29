# приватный метод позволяет образаться к атрибутам или методам класса только внутри класса
# два подчеркивания self.__name

class BankAccount:
    
    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport
    
    def print_public_data(self):
        self.__print_private_data()    
    
    def __print_private_data(self):
        print(self.__name, self.__balance, self.__passport)

account = BankAccount('Jerry', 32032568, 6565656565)
account.print_public_data()
account._BankAccount__print_private_data() # через класс можем вызвать приватный метод
print(account._BankAccount__name) # через класс можем вызвать приватный атрибут
print(account._BankAccount__balance)
print(account._BankAccount__passport)