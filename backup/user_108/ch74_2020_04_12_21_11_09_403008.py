def conta_bigramas(palavra):
    dic = {}
    for i in range(len(palavra)-1):
        bigrama = palavra[i]+palavra[i+1]
        dic[bigrama] = palavra.count(bigrama)
    return dic