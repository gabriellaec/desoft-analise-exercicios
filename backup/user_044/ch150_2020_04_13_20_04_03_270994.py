import math
def calcula_pi(n):
    pi=0
    for i in range(1,n+1):
        pi+=(6/(i**2))
    x=((pi)**(1/2))
    return x