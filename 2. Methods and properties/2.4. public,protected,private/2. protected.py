# защищенные атрибуты и методы позволяют нам обратиться к ним вне класса
# для разработчиков это метка, что лучше обращаться внутри класса
# одно подчеркивание self._name

class BankAccount:
    
    def __init__(self, name, balance, passport):
        self._name = name
        self._balance = balance
        self._passport = passport
        
    def print_protected_data(self):
        print(self._name, self._balance, self._passport)

account = BankAccount('Mia', 120000, 1212121212)
account.print_protected_data()
print(account._name)
print(account._balance)
print(account._passport)