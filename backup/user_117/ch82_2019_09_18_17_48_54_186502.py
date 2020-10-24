def primeiras_ocorrencias(s):
    dic = {}
    for i in range(len(s)):
        dic[i] += i
    return dic