def PiWallis(n):
    lista = []
    par = 2
    impar = 1
    pi = 1
    while len(lista)<n:
        div = par/impar
        lista.append(div)
        if par>impar:
            impar += 2
        else:
            par += 2
    for i in lista:
        pi *= i 
    return pi