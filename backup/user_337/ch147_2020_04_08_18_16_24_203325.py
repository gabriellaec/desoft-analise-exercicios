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
    frequencia = []
    for v in freq:
        frequencia.append (v)
    a = frequencia[0]
    i = 1
    while i<len(frequencia):
        if frequencia[i]>a:
            a = frequencia[i]
        i += 1
    for b in dicionario:
        if dicionario[b] == a:
            return b
