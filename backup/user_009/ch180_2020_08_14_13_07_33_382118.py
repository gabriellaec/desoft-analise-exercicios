def ocorrencias_letras(stri):
    dic = {}
    for i in stri:
        if i not in dic:
            dic[i] = stri.count(i)

    return dic