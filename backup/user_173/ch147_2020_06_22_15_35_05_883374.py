def conta_ocorrencias (lista):
    dicionario = {}
    for i in lista:
        dicionario [i] = lista.count(i)
    
    return dicionario

def mais_frequente(palavras):
    for palavra in palavras:
        return conta_ocorrencias(palavras)