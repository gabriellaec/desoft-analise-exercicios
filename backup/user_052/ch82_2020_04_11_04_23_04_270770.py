def primeiras_ocorrencias (string):
    dic = []
    i = 0
    for i in string:
        dic[i] = string[i]
        if string[i] not in dic:
            dic[i] = 1
        else:
            dic[i] += 1