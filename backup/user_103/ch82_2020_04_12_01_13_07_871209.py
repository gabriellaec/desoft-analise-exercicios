def primeiras_ocorrencias(palavra):
    list(palavra)
    dicionario={}
    i=0
    for i in palavra:
        if not palavra[i] in dicionario:
            dicionario[palavra[i]]=i
            i+=1
    print(dicionario)
                                 