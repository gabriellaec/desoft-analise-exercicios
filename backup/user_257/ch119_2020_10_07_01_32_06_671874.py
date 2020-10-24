def calcula_euler(x,n):
    t=1
    e=1
    while t < n:
        e+= (x**t)/fatorial(t)
        t+= 1
    return e