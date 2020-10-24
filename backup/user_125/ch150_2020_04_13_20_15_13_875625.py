import math
def calcula_pi(numeros):
    i=1
    x=0
    while i <= numeros:
        x+=6/(i**2)
        i+=1
    pi=math.sqrt(x)
    return pi