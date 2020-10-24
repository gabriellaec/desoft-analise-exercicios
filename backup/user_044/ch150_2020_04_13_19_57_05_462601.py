import math
def calcula_pi(n):
    pi=0
    pi=float(pi)
    for i in range(1,n+1,1):
        pi+=6/(i**2)
    x=(pi)**1/2
    return x