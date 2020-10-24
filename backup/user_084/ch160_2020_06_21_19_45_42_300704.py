from math import *
seno=[]
for i in range(91):
    x=sin(radians(i))
    y=4*i*(180-i)/(40500-i*(180-i))
    seno.append(abs(x-y))
print(max(seno))
    
    