
def conta_bigramas(palavra):
    dic = {}
    lista = []
    i = 0
    e = 1
    while e<len(palavra):
        lista.append(palavra[i]+palavra[e])
        i+=1
        e+=1
    
    for k in lista:
        if k not in lista:
            dic[k] = 1
        else:
            dic[k] += 1
    return dic