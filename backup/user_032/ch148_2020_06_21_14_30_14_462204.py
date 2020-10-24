def conta_letras(frases):
    dic = {}
    for x in frases:
        if x not in dic:
            dic[x]=1
        else:
            dic[x] += 1
    return dic