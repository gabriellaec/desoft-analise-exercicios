def PiWallis():
    pi = 2
    lista = range(2, 10000, 2)
    for num in lista:
        pi *= num/(num-1)*num/(num+1)
    return pi