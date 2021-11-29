from string import digits


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__secret = 'остров сокровищ'
        
    @property
    def secret(self):
        secret_User = input('Введите пароль: ')
        if secret_User == self.password:
            return self.__secret
        else:
            raise ValueError('Неверный пароль')

    @property
    def password(self):
        return self.__password            
            
    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False
    
    @staticmethod
    def check_password(popular_password):
        with open(r'password.txt') as file:
            file = file.read()
            if popular_password not in file:
                return True
            return False
    
    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError ('Пароль должен быть строкой')
        if len(value) < 4:
            raise ValueError ('Пароль должен быть больше 4 символов')
        if len(value) > 12:
            raise ValueError ('Пароль должен быть не больше 12 символов')
        if not User.is_include_number(value):
            raise ValueError ('Пароль должен содержать цифру')
        if not User.check_password(value):
            raise ValueError ('Слишком популярный пароль')
        self.__password = value

user = User('www', 'pass1word1')
print(user.secret)
user.password = 123 # TypeError: Пароль должен быть строкой
user.password = 'g13' # ValueError: Пароль должен быть больше 4 символов
user.password = 'g13vsDAVFDVWEVCDSCSCSCSD' # ValueError: Пароль должен быть не больше 12 символов
user.password = 'gJEJEJ' # ValueError: Пароль должен содержать цифру
