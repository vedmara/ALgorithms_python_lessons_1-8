import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_pos = 0
max_pos = 0
for i in range(1, len(array)):
    if array[i] < array[min_pos]:
        min_pos = i
    if array[i] > array[max_pos]:
        max_pos = i
array[min_pos], array[max_pos] = array[max_pos], array[min_pos]
print(array)