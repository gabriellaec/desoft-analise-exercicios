def primeiras_ocorrencias(palavra):
    dic = {}
    i = 0
    for letra in palavra:
        if letra not in dic.keys():
            dic[letra] = i
        i += 1

    return dic