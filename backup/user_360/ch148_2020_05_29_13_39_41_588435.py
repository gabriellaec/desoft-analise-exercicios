def conta_letras(p):
    dic = {}
    for i in p:
        if i not in dic:
            dic[i] - 1
        else:
            dic[i] += i
    return dic