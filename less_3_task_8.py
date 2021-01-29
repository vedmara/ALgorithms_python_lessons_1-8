M = 4
N = 5
array = [[], [], [], []]

for i in range(N):
    summa = 0
    for j in range(M - 1):
        a = int(input())
        summa += a
        array[i].append(a)
    array[i].append(summa)

for i in range(0, N):
    print(array[i])







 #       a = int(input())
  #      sum = sum + a
   # m[i][3]=sum
#print(m)
    