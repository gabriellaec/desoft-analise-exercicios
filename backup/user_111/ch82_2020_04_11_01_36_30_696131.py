def primeiras_ocorrencias(x):
    dicionario={}
    i=0
    for letra in x:
        if letra not in dicionario:
            dicionario[letra]=i
        i+=1
    return dicionario