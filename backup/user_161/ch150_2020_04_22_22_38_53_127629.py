import math

def calcula_pi(x):
    i=1
    s=0
    while i<=x:
        s+=6/(i*i)
        i+=1
    pi=math.sqrt(s)
    return pi