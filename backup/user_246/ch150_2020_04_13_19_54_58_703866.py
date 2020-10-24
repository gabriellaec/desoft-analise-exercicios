import math
def calcula_pi(n):
    i=1
    x=0
    while i<n+1:
        x=x+6/n**2
    return(math.sqrt(x))
        