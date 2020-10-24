import math
def calcula_pi (n):
    i=1
    p=0
    while i<=n:
        p+=6/(i**2)
    pi=math.sqrt(p)
    return pi