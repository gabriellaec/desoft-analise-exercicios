import math
def calcula_pi(n):
    a=1
    p=0
    while a<=n:
        p+=(6/(a**2))
        a+=1
    pi=math.sqrt(p)
    return pi