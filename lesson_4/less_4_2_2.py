import random
import timeit
import cProfile

def primes(num):
    a=[2]
    for i in range(3, num+1, 2):
	    if (i > 10) and (i%10==5):
		    continue
	    for j in a:
		    if j*j-1 > i:
			    a.append(i)
			    break
		    if (i % j == 0):
			    break
	    else:
		    a.append(i)
    return a

num = 1
while num < 10000:
    num *= 5
    t = timeit.timeit('primes(num)', number = 1000, globals=globals())
    print(f"{num=}\t\t{t/num=}")

#num=5           t/num=0.0011009895999999964
#num=25          t/num=0.0008924666800000003
#num=125         t/num=0.0011051258399999999
#num=625         t/num=0.0013835876672
#num=3125        t/num=0.00193039958336
#num=15625       t/num=0.003025825726656

cProfile.run('eratosfen(1000)')

 #3 function calls in 0.001 seconds
# Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# При сравнении работы 2х алгоритмов, сначала оба алгортма ведут себя одинаково, 
# но если увеличивать номер искомого числа более 100000, то "Решето Эратосфена" требует затраты большего количества ресурсов.
# Следовательно, для больших чисел он неудобен.