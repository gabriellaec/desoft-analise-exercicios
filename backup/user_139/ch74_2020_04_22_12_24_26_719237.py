def conta_bigramas(palavra):
    if len(palavra) < 2:
        return []
    dic = {}
    i = 0
    while i < len(palavra) - 1:
        bigrama = palavra[i] + palavra[i+1]
        if not bigrama in dic:
            dic[bigrama] = 1
        else:
            dic[bigrama] += 1
        i += 1
    return dic