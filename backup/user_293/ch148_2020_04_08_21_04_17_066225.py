def conta_letras(string):
    dic = {}
    for e in string:
        if not e in dic:
            dic[e] = 1
        else:
            dic[e] += 1
    return dic