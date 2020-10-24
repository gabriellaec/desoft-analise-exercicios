import math
def calcula_pi(n):
    n=1
    for c in range(1,n+1):
        pi=math.sqrt(6/(n**2))
        n+=1
    return pi