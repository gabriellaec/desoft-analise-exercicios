def ocorrencias_letras(s):
    dic = {}
    for e in s:
        if e in dic:
            dic[e] +=1
        else:
            dic[e]=1
    return a