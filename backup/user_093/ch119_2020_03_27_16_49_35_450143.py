import math


def calcula_euler(x,a):
    a=0
    i=0
    while i!=19:
        print(a)
        a+=(x/(math.factorial(i)))
        b=a+1
        return b
        i+=1