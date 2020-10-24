def traduz (lista, dic):
    nova = []
    for i in lista:
        for k,v in dic:
            if i == k:
                nova.append(v)
    return nova