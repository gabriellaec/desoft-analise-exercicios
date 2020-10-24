import math
def calcula_pi(n):
    i=0
    x=0
    while i<n+1:
        x=x+6/n**2
        i+=1
    return(math.sqrt(x))
        