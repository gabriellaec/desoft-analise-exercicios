import math
def calcula_pi(n):
    pi=0
    for i in range(1,n+1):
        pi+=math.sqrt(6/(i**2))
    return pi