def interseccao_valores(dicio1,dicio2):
    lista=[]
    for chave in dicio1:
        for chave2 in dicio2:
            if dicio1[chave]==dicio2[chave2]:
                lista.append(dicio1[chave])
    return lista
                