def mais_frequente (lista):
    dicionario = {}
    for i in lista:
        if i not in dicionario:
            dicionario[i] = 1
            b = dicionario[i]
        else:
            dicionario[i] += 1
            a = dicionario[i]
            for i in a:
                if dicionario[i] > dicionario[i+1]
                    return dicionario[i]
                else:
                    return dicionario[i+1]
                