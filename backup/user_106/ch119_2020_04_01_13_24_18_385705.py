import math

def calcula_euler(x,n):
    t=0
    s=0
    e=math.e
    p=e**x
    while t<n:
        p=(x**t)/math.factorial(t)
        t+=1
        s+=p
    return s