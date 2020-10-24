def primeiras_ocorrencias(palavra):
    dic = {}
    i = 0
    for letra in palavra:
        if not letra in dic:
            dic[letra] = i
        i += 1
    return dic