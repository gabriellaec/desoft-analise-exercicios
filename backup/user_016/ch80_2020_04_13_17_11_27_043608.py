def interseccao_chaves(dicionario1,dicionario2):
    lista = []
    for i in dicionario1.keys():
        if i in dicionario2.keys():
            lista.append(i)
    return lista
            