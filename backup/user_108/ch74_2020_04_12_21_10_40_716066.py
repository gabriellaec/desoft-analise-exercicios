def conta_bigramas(palavra):
    dic = {}
    for i in range(len(palavra)-1):
        dic[palavra[i]+palavra[i+1]] = palavra.count(palavra[i]+palavra[i+1])
    return dic