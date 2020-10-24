
def quantos_uns(a):
    b = str(a)
    contador = 0
    indice = 0
    while indice < len(b):
        if b[indice] == "1":
            contador += 1
            indice += 1
        else:
            indice += 1
    return contador
