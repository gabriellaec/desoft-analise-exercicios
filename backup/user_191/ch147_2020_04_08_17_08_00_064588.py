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
def mais_frequente(dic):
    for l in dic.values():
        return max(dic.key())