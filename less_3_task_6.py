import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_pos = 0
max_pos = 0
summa_mas = 0
for i in range(1, len(array)):
    if array[i] < array[min_pos]:
        min_pos = i
    if array[i] > array[max_pos]:
        max_pos = i
#print(min_pos, max_pos)
if max_pos < min_pos:
    max_pos, min_pos = min_pos, max_pos
for j in range(min_pos +1, max_pos):
    summa_mas += array[j]
print("сумма элементов, находящихся между минимальным и максимальным элементами", summa_mas)