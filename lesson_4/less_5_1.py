#Пользователь вводит данные о количестве предприятий, 
# их наименования и прибыль за 4 квартал (т.е. 4 числа) 
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) 
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

import collections

from collections import defaultdict
from collections import deque

companies = collections.defaultdict()
prof = collections.deque()
unprof = collections.deque()
all_profit = 0
quarter = 4

n = int(input('Введите количество компаний: '))

for i in range(n):
    name = input(f'Введите название {i+1}й компании: ')
    profit = 0
    q = 1
    while q <= quarter:
         profit += int(input(f'Введите прибыль за {q}й квартал: '))  
         q += 1
    companies[name] = profit
    all_profit += profit 

midl_profit = all_profit / n

for i, it in companies.items():
    if it >= midl_profit:
        prof.append(i)
    else:
        unprof.append(i)
print(f'Средняя прибыль всех компаний составила: {midl_profit}')
print(f'Прибыль выше среднего у {len(prof)} компаний:')
for name in prof:
    print(f' {name} составляет: {companies[name]} фантиков')
print(f'Прибыль ниже среднего у {len(unprof)} компаний:')
for name in unprof:
    print(f' {name} составляет: {companies[name]} фантиков')

