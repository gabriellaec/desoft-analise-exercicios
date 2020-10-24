def primeiras_ocorrencias(s):
    dic = {}
    for i in range(len(s)):
        dic[s[i]] = i
    return dic