from math import *

def sen_bhaskara(x):
    return (4*x*(180-x))/(40500-x*(180-x))

seno = []
mathseno = []
for x in range(0,91):
    diff = abs(sin(x) - sen_bhaskara(x))
    if diff > max_diff:
        max_diff = diff
        angle = x
print(angle+1)