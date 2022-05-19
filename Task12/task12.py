# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

is_Error = True
while is_Error:
    n = input('Введите количество элементов в словаре n = ')
    try:
        int(n)
        is_Error = False
    except ValueError:
        is_Error = True
    if not is_Error and int(n) > 0:
       n = int(n)
    else:
        is_Error = True

result = dict(map(lambda x: (x, 3*x +1), [i for i in range(1, n+1)]))
print(result)