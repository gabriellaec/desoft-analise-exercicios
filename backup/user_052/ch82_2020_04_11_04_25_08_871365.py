def primeiras_ocorrencias (string):
    dic = []
    c = 0
    for i in string:
        if i not in dic:
            dic[i] = c
        c += 1
    return dic 