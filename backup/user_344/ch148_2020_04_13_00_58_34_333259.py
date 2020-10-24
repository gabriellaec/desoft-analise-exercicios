def conta_letras(string):
    dic = {}
    for e in string:
        if e not in string:
            dic[e] = 1
        else:
            dic[e] +=1
    return dic