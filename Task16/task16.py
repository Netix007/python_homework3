# Задать список из n чисел последовательности (1+1/n)**n и вывести на экран их сумму.
# Например n = 4: результат [2, 2.25, 2.37037037037, 2.44140625] сумма элементов - 9.06177662037037

is_Error = True
while is_Error:
    n = input('Введите число n = ')
    try:
        int(n)
        is_Error = False
    except ValueError:
        is_Error = True
    if not is_Error and int(n) > 0:
       n = int(n)
    else:
        is_Error = True
result = ([(1+1/(i))**(i) for i in range(1, n+1)])
print(result)
print('Сумма элементов:', sum(result))