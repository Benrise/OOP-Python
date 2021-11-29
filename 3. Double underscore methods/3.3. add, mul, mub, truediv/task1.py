class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def __add__(self, other):
        print('__add__call')
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            return self.balance + other
        raise NotImplemented
        
    def __radd__(self, other):
        print('__radd__call')
        return self + other
    
    def __mul__(self, other):
        print('__add__call')
        if isinstance(other, BankAccount):
            return self.balance * other.balance
        if isinstance(other, (int, float)):
            return self.balance * other
        if isinstance(other, str):
            return self.name + other
        raise NotImplemented

c = BankAccount('Vasy', 200)
print(c * 3)
print(c * 'aaa')