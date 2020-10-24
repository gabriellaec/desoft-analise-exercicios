def primeiras_ocorrencias(string):
    dic={}
    for a in range len(string):
        if string[a] not in dic:
            dic[string[a]] = a
    return dic