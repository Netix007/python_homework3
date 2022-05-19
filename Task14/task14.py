# Подсчитать сумму цифр в вещественном числе.

def inp_float():
    is_Error = True
    while is_Error:
        n = input('Введите вещественное число n = ')
        try:
            float(n)
            is_Error = False
        except ValueError:
            is_Error = True
    return n

str = inp_float()
result = sum([int(x) for x in str if x != '.' and x != '-'])
print('Сумма цифр в числе:', result)