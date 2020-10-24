def interseccao_chaves(dic1,dic2):
    chaves=[]
    lista=[]
    for e in dic1.keys():
        lista.append(e)
    for k in dic2.keys():
        lista.append(k)
    for i in lista:
        if i not in chaves:
            chaves.append(i)
    return chaves