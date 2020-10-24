def primeiras_ocorrencias (string):
    dic = {}
    for i in string:
        x = string.find(i)
        dic[i] = x
    return dic