def arcotangente(x,n):
    global cont
    cont = 1
    while cont <= n:
        equa = x - (x**cont)/cont
        cont += 2
    return equa