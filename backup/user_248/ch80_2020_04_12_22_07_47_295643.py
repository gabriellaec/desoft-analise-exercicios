def interseccao_chaves(dic1,dic2):
    lista=[]
    chave1=dic1.keys()
    chave2=dic2.keys()
    for k in chave1 and chave2:
        lista.append(chave1 and chave2)
    return lista
    