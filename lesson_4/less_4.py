import random
import timeit
import cProfile


def changes(array):
    min_pos = 0
    max_pos = 0
    i = 1
    while i < len(array):
        if array[i] < array[min_pos]:
            min_pos = i
        if array[i] > array[max_pos]:
            max_pos = i
        i += 1
    
    array[min_pos], array[max_pos] = array[max_pos], array[min_pos]

    if i == len(array):
        return array
    
size = 1
while size != 10000:
    size*= 10
    array = [random.randint(size * -10, size * 10) for _ in range(size)]
    print(timeit.timeit('changes(array)', number = 1000, globals=globals())) 
    #0.011573541999999992   - 10
    #0.10542807299999998    - 100
    #1.2049587499999999     - 1000
    #12.487797813           - 10000 наблюжается линейная зависимость зависимость

cProfile.run('changes(array)')

 # output:\
 #Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.018    0.018 <string>:1(<module>)
#        1    0.014    0.014    0.017    0.017 less_4.py:6(changes)
#        1    0.000    0.000    0.018    0.018 {built-in method builtins.exec}
#    10001    0.004    0.000    0.004    0.000 {built-in method builtins.len}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}