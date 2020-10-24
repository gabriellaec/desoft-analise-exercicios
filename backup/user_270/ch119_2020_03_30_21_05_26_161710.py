import math
def factorial(n):
    sum = 1
    for i in range(1,n+1):
        sum = sum*i
    return sum
        

def calcula_euler(x,n):
    i = 0
    soma = 0
    while i < n:
        e_x = x**i/factorial(i)
        soma += e_x
        i += 1
    return soma