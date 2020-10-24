import math


def calcula_euler(x,a):
    a=0
    i=1
    while i!=19:
        a=(x/(math.factorial(i)))
        a=1+a+a
        i+=1
        return a
        

print(calcula_euler(2,3))
        


