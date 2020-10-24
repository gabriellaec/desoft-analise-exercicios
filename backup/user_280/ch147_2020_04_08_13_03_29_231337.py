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
        ocorrencias.append(int(ocorrencia))
    maior_ocorrencia = max(ocorrencias)
    if dicionario.values() == maior_ocorrencia:
        return dicionario.keys()
