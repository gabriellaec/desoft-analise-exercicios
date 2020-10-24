def primeiras_ocorrencias(string):
    dic={}
    for i in string:
        if i not in dic:
            dic[i]==i
    return dic
