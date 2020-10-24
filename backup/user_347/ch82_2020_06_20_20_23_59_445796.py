def primeiras_ocorrencias(string):
    dic = {}
    for i in range(len(string)):
        if i not in dic:
            dic[string[i]] = i