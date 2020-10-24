def inverte_dicionario(dic1):
    dic2 = {}
    chaves = list(dic1.keys())
    valores = list(dic1.values())
    for i in valores:
        for e in chaves:
            if chaves[e] not in dic2:
                dic2[chaves[e]] = valores [i]
            else:
                dic2[chaves[e]] += valores[i]
        