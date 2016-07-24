#!/usr/bin/env python
#Need to find the perfect pathagorinal square (a**2 + b**2 = c**2) where c > b > a and a + b + c = 1000
a = 0
b = 0
c = 0
final = []
left_side = 0
for c in range (334, 999):
    left_side = (1000-c)
    for b in range(left_side/2, left_side):
        if b < c:
            a = 1000 - c - b
            if (a**2+b**2 == c**2):
                final.append([a, b, c])
print final
print final[0][0]*final[0][1]*final[0][2]
    