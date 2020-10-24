def conta_letras(palavra):
    dic = {}
    for e in palavra:
        if e in dic:
            dic[e]+=1
        else:
            dic[e] = 1
    return dic