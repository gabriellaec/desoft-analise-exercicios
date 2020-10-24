def primeiras_ocorrencias(string):
    dic={}
    for i in string:
        dic[string[i]]=int(i)
    return dic