def fatorial(x):
    t = int(x) - 1
    fact = int(x)*t
    while t >= 1:
        fact = fact*t
    return fact