#!/usr/bin/env python
'''
The following iterative sequence is defined for the set of positive integers:

n ? n/2 (n is even)
n ? 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 ? 40 ? 20 ? 10 ? 5 ? 16 ? 8 ? 4 ? 2 ? 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
counter = 0
count = []
def collatz_chain(num):
    global counter
    if num%2==0:
        num = num/2
    else:
        num = 3*num + 1
    if num == 1:
        return None
    else:
        counter +=1
        collatz_chain(num)
def count_collatz():
    global counter
    i = 1
    while i <1000000:
        collatz_chain(i)
        count.append(counter)
        counter = 0
count_collatz()
count.sort()
print count[0]