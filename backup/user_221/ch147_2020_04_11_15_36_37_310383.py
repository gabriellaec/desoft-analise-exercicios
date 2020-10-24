def conta_ocorrencias(lista):
    dicionario = {}
    for i in range(len(lista)):
        if not lista[i] in dicionario:
            dicionario[lista[i]] = 1
        else:
            dicionario[lista[i]] += 1
    return dicionario
def mais_frequente(lista):
    dicionario = conta_ocorrencias(lista)
    maior_ocorrencia = 0
    palavra_recorrente = ''
    for p, v in conta_ocorrencias(lista).items():
        if v > maior_ocorrencia:
            maior_ocorrencia = v
            palavra_recorrente = p
    return palavra_recorrente