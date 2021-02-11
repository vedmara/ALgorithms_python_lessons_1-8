#Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
# заданный случайными числами на промежутке [0; 50). 
# Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50

def myMerge(data):
    if len(data) > 1:
        midl = len(data) // 2
        lefthalf = data[: midl]
        righthalf = data[midl :]

        #print(lefthalf)
        #print(righthalf)

        myMerge(lefthalf)
        myMerge(righthalf)
        
        i = 0
        j = 0
        k = 0
        while (i < len(lefthalf)) and (j < len(righthalf)):
            if lefthalf[i] < righthalf[j]:
                data[k] = lefthalf[i]
                i += 1
            else:
                data[k] = righthalf[j]
                j += 1
            k += 1
                
        while i < len(lefthalf):
            data[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            data[k] = righthalf[j]
            j += 1
            k += 1
        #print(data)

array = [random.uniform(MIN_ITEM, MAX_ITEM) for a in range(SIZE)]
print(array)

myMerge(array)
print(array)
