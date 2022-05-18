# Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.

is_Error = True
while is_Error:
    n = input('Введите количество членов последовательности n = ')
    try:
        int(n)
        is_Error = False
    except ValueError:
        is_Error = True
    if not is_Error and int(n) > 0:
       n = int(n)
    else:
        is_Error = True
s = [(-3)**i for i in range(n)]
print(s)