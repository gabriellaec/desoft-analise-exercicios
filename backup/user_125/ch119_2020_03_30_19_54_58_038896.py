import math 
n=1
def calcula_euler (x,n):
    j=0
    soma=0
    while j<n:
        soma+=x**j/math.factorial(j)
        j+=1
        return soma