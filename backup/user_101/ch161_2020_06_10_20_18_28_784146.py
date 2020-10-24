def PiWallis(n):
    pi = 1
    lista = range(2, n, 2)
    for num in lista:
        pi *= num/(num-1)*num/(num+1)
    return pi/2