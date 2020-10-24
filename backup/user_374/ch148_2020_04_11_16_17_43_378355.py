def conta_letras(texto):
    dic = {}
    for letra in texto:
        if letra not in dic:
                dic[letra] = 1
        else:
                dic[letra] += 1
    return dic
