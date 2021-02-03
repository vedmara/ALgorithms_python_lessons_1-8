import random
import timeit
import cProfile

def changes(array):
    mx = max(array)
    ix = array.index(mx)
    mn = min(array)
    iy = array.index(mn)
    array[ix] = mn
    array[iy] = mx
    return array

size = 1
while size != 10000:
    size*= 10
    array = [random.randint(size * -10, size * 10) for _ in range(size)]
    print(timeit.timeit('changes(array)', number = 1000, globals=globals()))

#0.005016302000000028   - 10
#0.025098021000000026   - 100
#0.386195677            - 1000
#2.57786151             - 10000
# из представленных решений использование встроенных функций быстрее

cProfile.run('changes(array)')

#output
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#        1    0.000    0.000    0.003    0.003 less_4_1_3.py:5(changes)
#        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#        1    0.001    0.001    0.001    0.001 {built-in method builtins.max}
#        1    0.001    0.001    0.001    0.001 {built-in method builtins.min}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        2    0.001    0.001    0.001    0.001 {method 'index' of 'list' objects}

#Большая часть ресурсов расходуется для встроенных методов    



