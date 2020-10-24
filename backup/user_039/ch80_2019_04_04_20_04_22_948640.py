def interseccao_chaves(dicionario1, dicionario2):
    lista=[]
    for c in dicionario1.keys():
        if c not in lista:
            lista.append(c)
    for e in dicionario2.keys():
        if e not in lista:
            lista.append(e)
    return lista
        