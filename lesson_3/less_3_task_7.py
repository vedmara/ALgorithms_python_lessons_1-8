import random

SIZE = 10
MIN_ITEM = -1000
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_pos = 0
min_pos_2 = 0

for i in range(1, len(array)):
    if array[i] < array[min_pos]:
        min_pos = i
for j in range(1, len(array)):
    if (array[j] <= array[min_pos_2])&(j != min_pos):
        min_pos_2 = j
print("Два наименьших элемента:", array[min_pos], array[min_pos_2])