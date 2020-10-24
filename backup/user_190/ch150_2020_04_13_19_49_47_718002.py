import math
def calcula_pi(n):
    i=0
    while i<=n and n!=0:
        x=math.sqrt(6/(i**2))
        i+=1
        return x