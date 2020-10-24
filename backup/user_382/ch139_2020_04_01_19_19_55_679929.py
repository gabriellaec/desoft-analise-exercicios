import random
def arcotangente(x,n):
    x = random.uniform(-1,1)
    soma = x
    i = 3
    while i < n+2:
        soma -= (x**i)/i
        i += 4
    t = 5
    while t < n+4:
        soma -= (x**t)/t
        t += 4
    return soma 