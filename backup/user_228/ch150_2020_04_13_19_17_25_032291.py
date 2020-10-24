import math
def calcula_pi(n):
    i=1
    r=0
    while i<n+1:
        r+=6/i**n
        i+=1
    return math.sqrt(r)