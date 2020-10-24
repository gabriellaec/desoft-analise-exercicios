x = 1
soma = 0

def calcula_pi(n):
    while x < n:
        d = (6/x**2)
        soma += d
        x += 1
        if x == n:
        pi = soma**1/2
    return pi
