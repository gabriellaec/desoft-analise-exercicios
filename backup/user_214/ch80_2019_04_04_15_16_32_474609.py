def interseccao_chaves(dic1, dic2):
    x=[]
    chaves = dic2.keys()
    lista_chaves=[]
    for u in chaves:
        lista_chaves.append(u)
    for a in dic1:
        if a in lista_chaves:
            x.append(a)
    return x