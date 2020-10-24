import math
n=1
def calcula_euler(x,n):
    i=n-1
    while i<n:
        y=1/(1-(x/math.factorial(i)))  #Soma de PG infinita
        return y