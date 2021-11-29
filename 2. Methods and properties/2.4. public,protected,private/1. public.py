# публичные атрибуты и методы
# обращение через метод или аргумент account1.print_public_data(), account1.name 

class BankAccount:
    
    def __init__(self, name, balance, passport):
        self.name = name
        self.balance = balance
        self.passport = passport
        
    def print_public_data(self):
        print(self.name, self.balance, self.passport)

account = BankAccount('Bob', 100000, 454545454554)
account.print_public_data()
print(account.name)
print(account.balance)
print(account.passport)