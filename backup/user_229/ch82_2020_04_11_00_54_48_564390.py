def primeiras_ocorrencias(string):
    dic = dict()
    for x in range(len(string)):
        for i in string:
            if i not in dic:
                dic[i] = x
    return dic