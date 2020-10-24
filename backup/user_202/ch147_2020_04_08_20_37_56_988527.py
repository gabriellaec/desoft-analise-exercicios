def conta_ocorrencias(lista):
    dic = {}
    c = 0
    for i in lista:
        for a in lista:
            if i == a:
                c += 1
        dic[i] = c
        c = 0
    return dic

def mais_frequente(lista):
    dic = conta_ocorrencias(lista)
    vmax = 0
    for k, v in dic.items():
        if v > vmax:
            vmax = v
            palavra = k
    return palavra