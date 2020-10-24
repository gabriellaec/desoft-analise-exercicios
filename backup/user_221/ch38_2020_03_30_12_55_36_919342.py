def quantos_uns(x):
    i = 0
    contador = 0
    while contador <= len(x):
            if x[i] == 1:
                contador += 1
                i +=1
            else:
                i += 1
    return contador