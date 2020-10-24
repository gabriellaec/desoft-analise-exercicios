def primeiras_ocorrencias(palavra):
    dicionario={}
    for e in palavra:
        dicionario[e]=palavra.index(e)
    return dicionario
palavra='abracadabra'
print(primeiras_ocorrencias(palavra))