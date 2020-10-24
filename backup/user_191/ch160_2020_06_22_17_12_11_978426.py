from math import *
dif=[]
for i in range(0,91):
    dif.append(abs(sin(i)-(4*i(180-i)/(40500-i(180-i)))))
    print(max(dif))