from math import factorial


def calcula_euler(x,n):
    a=0
    r=0
    while a<n :
        r+=(x**a)/(factorial(a))
        a+=1
        return r
        




