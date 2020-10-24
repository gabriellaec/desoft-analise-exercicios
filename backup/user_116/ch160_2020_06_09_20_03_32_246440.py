from math import *
lista=[]
for values in range(0,91):
    y=sin(values*pi/180)
    x=(4*values*(180-values))/(40500-values*(180-values))
    lista.append(abs(x-y))
va=max(lista)
index=lista.index(va)
print(index)