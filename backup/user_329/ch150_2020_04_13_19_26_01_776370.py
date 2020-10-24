x = 1
soma = 0

def calcula_pi(n):
    while x < n:
        m = (6/x**2)
        soma += m
        x += 1
    pi = soma**1/2
    return pi
