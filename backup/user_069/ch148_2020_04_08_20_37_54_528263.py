def conta_letras (string):
    dic = {}
    for i in range(len(string)):
        letra = string[i]
        if not letra in dic:
            dic[letra] = 1
        else:
            dic[letra] += 1
    return dic