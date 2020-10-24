def conta_ocorrencias(lista):
    dicionario = {}
    for palavra in lista:
        if not palavra in dicionario:
            dicionario[palavra] = 1
        else:
            dicionario[palavra]+=1
    return dicionario

def mais_frequente (lista):
    dicionario = {}
    for palavra in lista:
        if not palavra in dicionario:
            dicionario[palavra] = 1
        else:
            dicionario[palavra]+=1
    freq = dicionario.values()
    a = freq[0]
    i = 1
    while i<len(freq):
        if freq[i]>a:
            a = freq[i]
        i += 1
    return a