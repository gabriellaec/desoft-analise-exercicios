def primeiras_ocorrencias(string):
    dicionario={}
    letras=[]
    index=[]
    for i in range(len(string)):
        if string[i] not in letras:
            index.append(i)
            letras.append(string[i])
    for indice in range(len(index)):
        dicionario[letras[indice]]= index[indice]
    return dicionario
