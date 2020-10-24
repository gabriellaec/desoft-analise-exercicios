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
    for e in range(len(dic)):
        x = dic[lista[i-1]]
        y = dic[lista[i]]
        if x < y:
            frequente = y
        elif x > y:
            frequente = x
        else:
            continue
        e += 1
    return frequente
    