def contra_letras (string):
    dic = {}
    for i in len(string):
        letra = string[i]
        if not letra in dic:
            dic[letra] = 1
        else:
            dic[letra] += 1
    return dic