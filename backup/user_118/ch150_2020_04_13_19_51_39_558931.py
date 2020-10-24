import math
def calcula_pi(n):
    i=1
    n=int(input('Diga n'))
    while i<=n:
        pi=math.sqrt(6/(n**2))
        i+=1