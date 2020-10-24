def conta_ocorrencias(lista):
    contagem = {}
    for palavra in lista:
        if not palavra in contagem:
            contagem[palavra] = 1
        else:
            contagem[palavra] += 1
    return contagem

def mais_frequente(lista):
    dicionario = conta_ocorrencias(lista)
    ocorrencias = []
    for ocorrencia in dicionario.values():
        ocorrencias.append(ocorrencia)
    maior_ocorrencia = max(ocorrencias)
    i = 0
    while i < len(ocorrencias):
        if maior_ocorrencia == dicionario[i][1]:
            return dicionario[i][0]
        i += 1