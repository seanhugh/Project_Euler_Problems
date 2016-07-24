#!/usr/bin/env python
#Problem 6 on Euler Project
#Find the difference between the sum of the squares of the first hundred natural numbers and the square of the sums
#First I will calculate the sum of the squares
sum_of_squares = 0
square_of_sums = 0
final = 0
for i in range (1, 101):
    sum_of_squares += (i*i)
    square_of_sums += i
square_of_sums = square_of_sums**2
final = square_of_sums - sum_of_squares
print final