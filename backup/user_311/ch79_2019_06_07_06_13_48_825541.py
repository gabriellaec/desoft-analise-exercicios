def monta_dicionario(chaves, valores):
    dic = {}
    for i in range(len(chaves)):
        dic[chaves[i]] = valores[i]
        
    return dic