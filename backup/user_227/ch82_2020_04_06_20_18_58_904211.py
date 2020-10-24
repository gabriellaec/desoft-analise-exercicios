def primeiras_ocorrencias(string):
    dicionario={}
    i=0
    for caractere in string:
        if not caractere in dicionario:
            dicionario[caractere]=i
        i+=1
    return dicionario