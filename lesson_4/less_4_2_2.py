import random
import timeit
import cProfile
import math

def primes(n):
    from math import sqrt
    a = [2]
    for i in range(3, n+1, 2):
        if (i > 10) and (i%10==5):
            continue
        for j in a:
            if a > int((sqrt(i)) + 1):
                a.append(i)
                break
            if (i % j == 0):
                break
        else:
            a.append(i)
    return a
#print(primes(1000))

num = 1
while num < 10000:
    num *= 5
    t = timeit.timeit('primes(num)', number = 1000, globals=globals())
    print(f"{num=}\t\t{t/num=}")

#num=5           t/num=0.0026905416000000014
#num=25          t/num=0.00231308748
#num=125         t/num=0.0025770058320000004
#num=625         t/num=0.0034405817504
#num=3125        t/num=0.004606165533439999

cProfile.run('eratosfen(1000)')

 #3 function calls in 0.001 seconds
# Ordered by: standard name
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
