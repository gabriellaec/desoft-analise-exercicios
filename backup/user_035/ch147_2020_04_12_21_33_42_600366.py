def mais_frequente(lista):
    dic = {}
    i = 0
    while i <= len(lista)-1:
        if lista[i] not in dic:
            dic[lista[i]] = 1
            i += 1
        else:
            dic[lista[i]] += 1
            i += 1
    for e in range(len(dic)-1):
        x = dic[lista[e-1]]
        y = dic[lista[e]]
        if x < y:
            frequente = dic[e-1]
        elif x > y:
            frequente = dic[e]
        else:
            continue
        e += 1
    return frequente
    