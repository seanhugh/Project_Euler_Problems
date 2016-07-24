#!/usr/bin/env python
#This is my second solution to problem 1 in the Euler Project. I have imported a timer which I found the code for on Stack Overflow
#So that I can judge how efficient my code is. (Source: http://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python)
#I did it myself first. Then optomized it myself. Then looked at outside sources: http://www.mathblog.dk/project-euler-problem-1/
import timeit
start = timeit.default_timer()

#my first go: 0.517400061678 ms
num = 0
three = 3
five = 5
both = 15
while three < 1000:
    num +=three
    three+=3
while five < 1000:
    num +=five
    five+=5
#here I just used some simple while loops to basically go through all of the multiples of 3 and 5 below 1000 and
#add them up to a variable num
while both < 1000:
    num-=both
    both+=15
print num
#At the end I realized that I needed to take away the overlapp of the two (which were all the multiples of 15)

#---------------------------------------------------------------------------------------------------
#my second go: 0.123477313905 ms
print sum(range (3,1000, 3)) + sum(range(5,1000, 5)) - sum(range(15,1000, 15))
#We went over the range() function in class. It works like the following: range(start, stop, step). So the range of
#(3,1000,3) starts at 3, stops at 999 (1 short of 1000)and goes up by 3's (3, 6, 9.....)

#---------------------------------------------------------------------------------------------------
#my third go using an outside theorem and some math to try and speed it up: 0.0632444778536 ms

def multiples(num, maximum):
    maximum = maximum/num
    return num * maximum * (maximum +1) * .5
#here I created a function multiples. This function allowed me to implement a common math theorem about the sum
#of the elements in a list. For example, the sum of (1 + 2 +3 +4.....+ N) is equal to the average of the elements
#in the list (N+1)/2 * the total number of elements (N). So, since the multiples of 3 up to 1000 is (3, 6, 9.....999)
#which is basically 3*(1,2,3....333), I was able to change this to 3*(333+1)*333/2. This creates the formula
#n*N*(N+1)/2 which I was then able to apply to all of the numbers
print multiples(3, 999) + multiples (5, 999) - multiples(15, 999)

#---------------------------------------------------------------------------------------------------
#End part of timer code:
stop = timeit.default_timer()
a = stop - start
print "it took", a*1000, "ms"