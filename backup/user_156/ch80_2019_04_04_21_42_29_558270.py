def interseccao_chaves(dicionario1,dicionario2):
    lista=[]
    for k in dicionario1.keys():
        for kk in dicionario2.keys():
            if k==kk:
                lista.append(k):
    return lista
    