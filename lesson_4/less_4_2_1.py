import random
import timeit
import cProfile

def eratosfen(n):
    a = []
    for i in range(n + 1):
        a.append(i)
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
       
            j = i + i
            while j <= n:
            
                a[j] = 0
           
                j = j + i
        i += 1

    a = set(a)
    #a.remove(0)
    return a
print(eratosfen(100))

num = 1
while num < 1000:
     num *= 5
     t = timeit.timeit('eratosfen(num)', number = 1000, globals=globals())
     print(f"{num=}\t\t{t/num=}")

#num=5           t/num=0.0016850520000000035
#num=25          t/num=0.0013941645999999996
#num=125         t/num=0.0013980983360000004
#num=625         t/num=0.0017429720831999998
#num=3125        t/num=0.00194642045024      # наблюдается линейная зависимость

cProfile.run('eratosfen(1000)')

# 1005 function calls in 0.003 seconds

 #  Ordered by: standard name

  # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 #     1    0.000    0.000    0.003    0.003 <string>:1(<module>)
 #     1    0.002    0.002    0.003    0.003 less_4_2_1.py:5(eratosfen)
 #     1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
 #    1001  0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
 #     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

