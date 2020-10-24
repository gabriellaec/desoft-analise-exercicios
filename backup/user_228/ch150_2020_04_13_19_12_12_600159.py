import math
def calcula_pi(n):
    i=1
    r=0
    while i<n:
        r+=6/(i**2)
        i+=1
    return r