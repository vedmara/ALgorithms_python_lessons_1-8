#Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. 
#Поиск медианы с сортировкой методом "расчёстка"

import random

m = int(input('Введите натуральное М:'))

SIZE = 2 * m + 1
MIN_ITEM = -1000
MAX_ITEM = 1000

def myMedian(data):
    gap = len(data)
    flag = True
    while gap > 1 or flag:
        gap = max(1, int(gap/1.25))
        flag = False
        for i in range(len(data)-gap):
            j = i + gap
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
                flag = True
    #print(data)
    
    midl = len(data) // 2
    print(data[midl])
        

array = [random.randint(MIN_ITEM, MAX_ITEM) for a in range(SIZE)]
print(array)

myMedian(array)
