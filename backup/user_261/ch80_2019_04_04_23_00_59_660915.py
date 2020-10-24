def interseccao_chaves(dicionario1,dicionario2):
    dic3={}
    l=[]
    for chaves1 in dicionario1:
        if chaves1 not in l:
            l.append(chaves1)
    for chaves 2 in dicionario2:
        if chaves2 in l:
            dic3[chaves2]=1
    return dic3

