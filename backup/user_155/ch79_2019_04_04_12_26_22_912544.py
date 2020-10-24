def monta_dicionario(chaves,valores):
    dic = {}
    i = 0 
    for chave in chaves:
        dic[chave] = valores[i]
        i += 1
    return dic
        