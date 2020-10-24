def conta_a(texto):
    indice = 0
    contador = 0
    while indice < int(len(texto)):
        if texto[indice] == 'a' or texto[indice] == 'A':
            contador += 1
        indice += 1
    return contador