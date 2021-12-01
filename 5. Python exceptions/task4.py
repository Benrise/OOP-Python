try:
    raise ValueError('ошибка значения')
except ValueError as first:
    try:
        raise TypeError('Ошибка типа')
    except TypeError as second:
        raise Exception('Большое исключение') from None

try:
    raise ValueError('ошибка значения')
except ValueError as first:
    try:
        raise TypeError('Ошибка типа')
    except TypeError as second:
        raise Exception('Большое исключение') from second

try:
    raise ValueError('ошибка значения')
except ValueError as first:
    try:
        raise TypeError('Ошибка типа')
    except TypeError as second:
        raise Exception('Большое исключение') from first