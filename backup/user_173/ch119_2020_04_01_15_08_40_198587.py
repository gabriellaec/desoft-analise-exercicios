def fatorial (y):
    r = 1
    i = 1
    while i < y:
        i += 1 
        r *= i
    return r

def calcula_euler (x,n):
    i = 0
    a = 0
    while i < n:
        a += (x**i)/fatorial(n)
    return a
    