#!/usr/bin/env python
#Problem_5 Soulution
'''multiplication = []
palindromes = []
temp = 0
def check_palindrome(num):
    #abcde
    if num > 10000:
        num = str(num)
        if (num[0]==num[-1] and num[1]==num[-2] and num[2] == num [-3]):
            return 'true'
    else:
        pass
def multiply():
    for i in range (100, 1000):
        for j in range (100, 1000):
            temp = i * j
            if check_palindrome(temp) == 'true':
                palindromes.append(temp)
def sort(list):
    palindromes.sort()
multiply()
sort(palindromes)
print palindromes'''
#problem 5
import timeit

start = timeit.default_timer()

i = 20
 
while (i %  2 != 0 or i %  3 != 0 or i %  4 != 0 or i %  5 != 0 or i %  6 != 0 or i %  7 != 0 or i %  8 != 0 or i %  9 != 0 or i % 10 != 0 or i % 11 != 0 or i % 12 != 0 or i % 13 != 0 or i % 14 != 0 or i % 15 != 0 or i % 16 != 0 or i % 17 != 0 or i % 18 != 0 or i % 19 != 0 or i % 20 != 0 ):
    i+=20
print i

stop = timeit.default_timer()

a = stop - start
print "it took", a, "seconds"
