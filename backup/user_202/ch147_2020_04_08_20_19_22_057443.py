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
    lkey = []
    lvalor = []
    for key in dic:
        lkey.append(key)
        lvalor.append(dic[key])
    valormax = 0
    for valor in lvalor:
        if valor > valormax:
            valormax = valor
    c = 0
    for i in lvalor:
        if i == valormax: 
            posicao = c
        c += 1
    resposta = lkey[posicao]
    return resposta