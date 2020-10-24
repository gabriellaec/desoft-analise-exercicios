def conta_ocorrencias(lista):
    dicionario = {}
    for palavra in lista:
        if palavra not in dicionario:
            dicionario[palavra] = 1
        else:
            dicionario[palavra] += 1
    return dicionario



def mais_frequente(lista):
    d = conta_ocorrencias(lista)
    mais_frequente = 0
    for palavra, valor in d.items():
        if valor >= mais_frequente:
            mais_frequente = valor
            palavra_f = palavra
    return palavra_f
