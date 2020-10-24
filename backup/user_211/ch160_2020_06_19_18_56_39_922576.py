from math import *
dif=[]
def senbask(x):
    return ((4*x*(180-x))/(40500-x*(180-x)))

for i in range (0,91,1):
    dif.append(abs(sin(i)-senbask(i)))

print (dif.index(max(dif)))