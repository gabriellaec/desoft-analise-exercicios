def quantos_uns(x):
    i = 0
    contador = 0
    while i < len(x):
        if x[i] == 1:
            contador += 1
        i += 1
    print(contador)
            