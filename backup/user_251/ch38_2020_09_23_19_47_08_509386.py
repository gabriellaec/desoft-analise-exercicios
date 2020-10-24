a = 11
def quantos_uns(a):
    contador = 0
    indice = 0
    while indice < len(a):
        if a[indice] == "1":
            contador += 1
            indice += 1
        else:
            indice += 1
    return contador
