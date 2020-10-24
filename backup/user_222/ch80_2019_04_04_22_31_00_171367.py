def interseccao_chaves(dicionario1,dicionario2):
    lista=[]
    elemento=0
    for k1 in dicionario1:
        for k2 in dicionario2:
            if k1==k2:
                elemento=k1
                lista.append(elemento)
    return lista