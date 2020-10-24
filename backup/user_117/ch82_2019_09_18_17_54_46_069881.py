def primeiras_ocorrencias(s):
    dic = {}
    for i in range(len(s)):
        letra = s[i]
        if letra not in dic:
            dic[letra] = i
    return dic