def zera_negativos(a):
    indice = 0
    while indice < len(a):
        if a[indice] < 0:
            a[indice] = 0
            indice += 1
        else:
            indice += 1
    return a

print(a)