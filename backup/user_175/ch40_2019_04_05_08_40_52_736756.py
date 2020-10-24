def fatorial(x):
    x = int(x)
    cont = 1
    factor = x
    while cont < x:
        factor = factor*(x-cont)
        cont += 1
    return factor