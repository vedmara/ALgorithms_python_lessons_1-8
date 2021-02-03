import random
import timeit
import cProfile


def changes(array):
    min_pos = 0
    max_pos = 0
    for i in range(1, len(array)):
        if array[i] < array[min_pos]:
            min_pos = i
        if array[i] > array[max_pos]:
            max_pos = i
    
    array[min_pos], array[max_pos] = array[max_pos], array[min_pos]

    if i == len(array):
        return array
    
size = 1
while size != 1000:
    size*= 10
    array = [random.randint(size * -10, size * 10) for _ in range(size)]
    print(timeit.timeit('changes(array)', number = 1000, globals=globals()))

#0.009217863999999992
# 0.07087255199999998
# 0.7482232300000001 получаем экспоненциальную зависимость

print('***')
cProfile.run('changes(array)')

 #ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#   1    0.001    0.001    0.001    0.001 less_3_task_3.py:6(changes)
#   1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#   2    0.000    0.000    0.000    0.000 {built-in method builtins.len}  
#   1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   1    0.000    0.000    0.001    0.001 <string>:1(<module>)

