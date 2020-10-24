from math import *

def bhaskara(x):
    return (4*x*(180-x))/(40500 - x*(180-x))

error = {}
for e in range(0, 91):
    error[abs(bhaskara(e)-sin(radians(e)))] = e

print(error.get(max(error)))
    