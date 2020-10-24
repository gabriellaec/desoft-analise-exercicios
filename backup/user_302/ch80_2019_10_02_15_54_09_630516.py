def interseccao_chaves(dicionario1, dicionario2):
    lista=[]
    for i in dicionario1 and dicionario2:
        if i in dicionario1 and dicionario2:
            lista.append(i)
    return lista