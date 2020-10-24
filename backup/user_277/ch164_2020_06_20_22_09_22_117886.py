def traduz(lista, dicionario):
    lista2 = []
    for i in range(len(lista)):
        ingles = lista[i]
        if j in dicionario.keys():
            traducao = dicionario[ingles]
            lista2.append(traducao)
    return lista2