#Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. 

import random

m = int(input('Введите натуральное М:'))

SIZE = 2 * m + 1
MIN_ITEM = -1000
MAX_ITEM = 1000
  
array = [random.randint(MIN_ITEM, MAX_ITEM) for a in range(SIZE)]
print(array)

for i in range(0, len(array)):
    left = 0
    right = 0
    for j in range(0, len(array)):
        if array[i] <= array[j]:
            left += 1
        if array[i] >= array[j]:
            right += 1
    if left == right:
        print (str(array[i]))
        break
