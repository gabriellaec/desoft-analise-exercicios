def PiWallis(len):
    pi = 2
    lista = range(2, len, 2)
    for num in lista:
        pi *= num/(num-1)*num/(num+1)
    return pi