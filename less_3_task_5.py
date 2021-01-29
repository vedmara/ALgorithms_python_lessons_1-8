import random

SIZE = 10
MIN_ITEM = - 100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_el = array[0]
pos = 0

for i in range(1, len(array)):
    if (array[i] < 0) & (abs(array[i] ) < abs(max_el)):
        max_el = array[i]
        pos = i
print ("Максимальный отрицательный элемент", max_el, "и его индекс", pos)
