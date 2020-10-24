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
    e = 0
    while e <= len(dic)-1:
        if dic[e] > dic[e+1]:
            maior = dic[e]
            e += 1
        else:
            maior = dic[e+1]
            e += 1
    return maior