#Определение количества различных подстрок с использованием хеш-функции. 
# Пусть на вход функции дана строка. 
# Требуется вернуть количество различных подстрок в этой строке.

import hashlib

def my_arr(s):
    t = []
    for i in range(0, len(s)):
        for j in range(1, len(s)+1):
            if s[i:j] != '' and s[i:j] != s and not(s[i:j] in t): 
                t.append(s[i:j])          
    return  t

def rabin_karp(s, t):
    len_sub = len(t)
    h_subs = hashlib.sha1(t.encode('utf-8')).hexdigest()
    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i+len_sub].encode('utf-8')).hexdigest():
            return True
    return False

string = input('введите строку:')
arr = my_arr(string)

count = 0

for substring in arr:
    if rabin_karp(string, substring):
        count += 1
print('Количество различных подстрок:', count)
