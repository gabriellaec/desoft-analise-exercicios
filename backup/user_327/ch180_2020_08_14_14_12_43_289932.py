def ocorrencias_letras(s):
    dic = {}
    for c in s:
        if not (c in dic):
            dic[c] = 1
        else:
            dic[c] += 1