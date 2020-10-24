def primeiras_ocorrencias(palavra):
    d=[]
    for e in palavra:
        if palavra[e] not in d:
            d[palavra[e]]=e
      
    return d