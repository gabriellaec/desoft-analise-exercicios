import math
def calcula_pi(n):
    n=1
    p=0
    for c in range(1,n+1):
        p+=(6/(n**2))
        n+=1
    pi=math.sqrt(p)
    return pi