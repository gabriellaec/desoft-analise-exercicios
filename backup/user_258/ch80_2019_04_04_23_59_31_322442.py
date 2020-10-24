def interseccao_chaves(dic1,dic2):
    chaves=[]
    lista=[]
    for e in dic1.keys():
        lista.append(e)
    for k in dic2.keys():
        lista.append(k)
    for i in lista:
        if i not in chaves and i in dic1.keys() and i in dic2.keys():
            chaves.append(i)
    return chaves