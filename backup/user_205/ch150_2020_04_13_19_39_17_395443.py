from math import sqrt 
def calcula_pi(n):
    i = 1
    soma = 0
    while i<=n:
        y = sqrt(sum(6/i**2))
        print (y)
        i+=1
    return y 
     
        