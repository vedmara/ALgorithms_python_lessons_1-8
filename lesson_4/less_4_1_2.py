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
while size != 10000:
    size*= 10
    array = [random.randint(size * -10, size * 10) for _ in range(size)]
    print(timeit.timeit('changes(array)', number = 1000, globals=globals()))

#0.009064479999999986   - 10
#0.07378369800000001    - 100
#0.7588842179999999     - 1000
#7.43289099             - 10000 как и в первом варианте линейная зависимость, но цикл с параметром работает быстрее

print('***')
cProfile.run('changes(array)')

 #   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 #       1    0.000    0.000    0.008    0.008 <string>:1(<module>)
 #       1    0.008    0.008    0.008    0.008 less_4_1_2.py:6(changes)
 #       1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
 #       2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
 #       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

 # основное время уходит на работу функции