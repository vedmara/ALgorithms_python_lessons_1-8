#Написать программу сложения и умножения двух шестнадцатеричных чисел. 
# При этом каждое число представляется как коллекция, элементы которой — цифры числа. 
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

import collections

from collections import defaultdict
from collections import deque

HEX_NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')

numbers = {'0': 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, 
            'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}

def summa(n1, n2):
   
    if len(n2) > len(n1):
        n1, n2 = n2, n1
    
    n2.extendleft('0' * (len(n1)-len(n2)))
    
    result = deque()
    overflow = 0
    
    while len(n1) !=0:
        n1_num = numbers[n1.pop()]
        n2_num = numbers[n2.pop()]
        result_num = n1_num + n2_num + overflow
        
        if result_num >= 16:
            overflow = 1
            result_num -= 16            
        else:
            overflow = 0

        result.appendleft(HEX_NUMBERS[result_num])

    if overflow == 1:
        result.appendleft('1')
    return result

a = deque(input('Введите 1-е шестнадцатиричное число: ').upper())
b = deque(input('Введите 2-е шестнадцатиричное число: ').upper())

#print(f'{a} + {b} = {summa(a, b)} - выводит как очередь deque(['A', 'F']) + deque(['A']) = deque(['B', '9'])
print(f'{list(a)} + {list(b)} = {list(summa(a, b))}') #выводит результат в виде ['A', '2'] + ['C', '4', 'F'] = ['C', 'F', '1']
