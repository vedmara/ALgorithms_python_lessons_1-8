#Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, 
# заданный случайными числами на промежутке [-100; 100).

import random

SIZE = 10
MIN_ITEM = - 100
MAX_ITEM = 100

def mybubble(data):
    
    for  i in range(len(data)):
        for j in range(len(data) - i -1):
            if data[j] < data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
        
array = [random.randrange(MIN_ITEM, MAX_ITEM) for a in range(SIZE)]
print(array)

mybubble(array)
print(array)

