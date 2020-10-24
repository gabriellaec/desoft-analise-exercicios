def interseccao_chaves(dicionario1,dicionario2):
    lista=[]
    for e in dicionario1:
        for i in dicionario2:
            if e==i:
                lista.append(e)
    return lista
    