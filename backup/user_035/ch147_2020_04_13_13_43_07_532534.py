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
    for e in range(len(lista)):
        if dic[lista[e+1]] > dic[lista[e]]:
            maior = dic[lista[e+1]]
        else:
            maior = dic[lista[e]]
    return maior