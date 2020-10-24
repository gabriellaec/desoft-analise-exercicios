def monta_dicionario(chaves,valores):
    dic={key:value for key,value in zip(chaves,valores)}
    return dic
    for i in range(len(chaves)):
        dic[chaves[i]]=valores[i]
    return dic