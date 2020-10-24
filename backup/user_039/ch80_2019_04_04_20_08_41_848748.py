def interseccao_chaves(dicionario1, dicionario2):
    lista=[]
    for c in dicionario1:
        for e in dicionario2:
            if c=e:
                lista.append(e)
    return lista
        