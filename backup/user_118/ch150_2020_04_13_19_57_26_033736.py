import math
def calcula_pi(n):
    i=1
    n=0
    while i<=n:
        pi=(6/(i**2))
        n=sum(pi)
        i+=1
    px=math.sqrt(n)
    return px