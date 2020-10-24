
def conta_bigramas(string):
    dic = {}
    lista = []
    i = 0
    e = 1
    while e<len(string):
        lista.append(string[i]+string[e])
        i+=1
        e+=1
    
    for k in lista:
        if k not in lista:
            dic[k] = 1
        else:
            dic[k] += 1
    return dic