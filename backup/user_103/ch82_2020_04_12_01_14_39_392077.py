def primeiras_ocorrencias(palavra):
    list(palavra)
    dicionario={}
    i=0
    while i < len(palavra):
        if not palavra[i] in dicionario:
            dicionario[palavra[i]]=i
            i+=1
        else:
            i+=1
    print(dicionario)
                                 