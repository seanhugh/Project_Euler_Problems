#!/usr/bin/env python
#Problem 6 on Euler Project. Looking for the 10,001st prime number
primes = []
i = 1
q=0
def check_prime(num):
    if num ==1: return 'false'
    if num ==2: return 'true'
    if num % 2 == 0: return 'false'
    for j in range(3, int((num+1)**.5)+1, 2):
        if  (num % j == 0) and (num != j):
            return 'false'
    return 'true'
while len(primes) <10001:
    if check_prime(i)=='true':
        primes.append(i)
    i += 1
print len(primes)
print primes[-1]