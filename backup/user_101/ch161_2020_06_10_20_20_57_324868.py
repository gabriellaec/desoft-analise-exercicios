def PiWallis(n):
    pi = 1
    lista = range(0, n, 2)
    for num in lista:
        if num-1 < 0:
            continue
        else:
            pi *= num/(num-1)*num/(num+1)
            pi = pi/2
    return pi