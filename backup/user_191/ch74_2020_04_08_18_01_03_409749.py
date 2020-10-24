def conta_bigramas(lista):
    dic = {}
    c = 0
    for [i,i+1] in lista:
        for [a,a+1] in lista:
            if [i,i+1] == [a,a+1]:
                c += 1
        dic[i,i+1] = c
        c = 0
    return dic