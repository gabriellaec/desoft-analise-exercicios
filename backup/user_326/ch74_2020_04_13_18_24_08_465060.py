def conta_bigramas(string):
    dicionario = {}
    lista_letras = list(string)
    for indice in range(len(lista_letras)- 1):
            bigrama = lista_letras[indice] + lista_letras[indice + 1]
            if bigrama in dicionario:
                dicionario[bigrama] += 1
            else:
                dicionario[bigrama] = 1
    return dicionario