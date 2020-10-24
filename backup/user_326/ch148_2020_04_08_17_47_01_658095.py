def conta_letras(lista):
    dicionario = {}
    for indice in len(lista):
        lista_letras = list(lista[indice])
        for letra in lista_letras:
            if letra in dicionario:
                dicionario[letra] += 1
            else:
                dicionario[letra] = 1
    return dicionario