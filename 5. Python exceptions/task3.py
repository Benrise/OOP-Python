# else - исп-ся только один раз. Выводтся в том случае, если не сработал except
# finally - исп-ся только один раз. Всегда выводится в конце. Обычно исп-ют для закрытия файла

s = 'hello'
d = {}
# f = open('123.txt')
try:
    1/5
except (KeyError, IndexError):
    print('LookupError')
except ZeroDivisionError:
    print('ZeroDivisionError')
else:
    print('good')
finally:
    print('end')
    #f.close()