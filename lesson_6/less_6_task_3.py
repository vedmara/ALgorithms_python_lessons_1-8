# решение с помощью строки

import sys

n = str(input('Введите число:'))

print('Обратное число:', n[:: - 1])

print("В программе задействовано байт памяти:", sys.getsizeof(n))

#Возьмем число 123456789
#Обратное число:  987654321
#В программе задействовано байт памяти: 34 на строку из 9ти символов

#Возьмем число 1234567890987654321234567890987654321
#Обратное число:  1234567890987654321234567890987654321
#В программе задействовано байт памяти: 62 на строку из 37 символов

#Для данной задачи, не содержащей большого количества переменных, а количество цифр в вводимом числе неограничено, то
# затраты памяти напрямую зависят от того, какой длинны число будет введено
