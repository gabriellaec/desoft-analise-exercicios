def conta_bigramas(string):
    dicionario = {}
    lista_letras = list(string)
    for indice in range(len(lista_letras)):
        if indice == 0:
            bigrama = lista_letras[indice] + lista_letras[indice + 1]
            dicionario[bigrama] = 1
        elif indice < len(lista_letras) - 1:
            bigrama_para_frente = lista_letras[indice] + lista_letras[indice + 1]
            if bigrama_para_frente in dicionario:
                dicionario[bigrama_para_frente] += 1
            else:
                dicionario[bigrama_para_frente] = 1
    print(dicionario)
    return dicionario
