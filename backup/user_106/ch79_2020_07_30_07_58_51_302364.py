def monta_dicionario(chaves, valores):
    dic = {}
    for i in range(0, len(chaves)):
        dic[chaves[i]] = valores[i]
    return dic