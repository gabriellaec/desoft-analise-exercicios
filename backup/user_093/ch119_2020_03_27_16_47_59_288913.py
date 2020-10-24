import math


def calcula_euler(x):
    a=1
    i=0
    while i!=19:
        print(a)
        a+=1+(x/(math.factorial(i)))
        return a
        i+=1