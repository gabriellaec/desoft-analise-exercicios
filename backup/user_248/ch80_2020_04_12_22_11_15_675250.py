def interseccao_chaves(dic1,dic2):
    lista=[]
    chave1=dic1.keys()
    chave2=dic2.keys()
    for i in chave1:
        if dic1==dic2:
            lista.append(dic1)
    return lista
    