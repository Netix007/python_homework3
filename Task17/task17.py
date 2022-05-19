# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число

from random import randint
from functools import reduce

is_Error = True
while is_Error:
    n = input('Введите число для формирования списка N = ')
    try:
        int(n)
        is_Error = False
    except ValueError:
        is_Error = True
    if not is_Error and int(n) > 0:
       n = int(n)
    else:
        is_Error = True

f_txt = open("text.txt", 'w')
first_elem = randint(1, n)
temp_list = {first_elem}
num_elem_file = randint(2, n)
for i in range(1, num_elem_file):
    rep = True
    while rep:
        elem = randint(1, n)
        if elem not in temp_list:
            temp_list.add(elem)
            rep = False
for item in temp_list:
    f_txt.write(f'{item}\n')
f_txt.close()

new_list = [randint(-n,n) for i in range(n)]

f_txt = open("text.txt")
posit = [int(i) for i in f_txt.read().splitlines()]
f_txt.close()
print('Список:', new_list)
print('Позиции необходимых элементов:', posit)
result = reduce(lambda x,y: x * y, [new_list[i-1] for i in posit])
print('Произведение элементов на указанных позициях:', result)