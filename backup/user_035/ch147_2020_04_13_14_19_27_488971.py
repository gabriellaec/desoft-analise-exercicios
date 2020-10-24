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
        if dic[lista[e]] > dic[lista[e+1]]:
            maior = dic[lista[e]]
        else:
            maior = dic[lista[e+1]]
    return maior