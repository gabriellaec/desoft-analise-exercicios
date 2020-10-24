def conta_ocorrencias (palavras):
    dicio ={}
    for k in palavras:
        if k in dicio:
            dicio[k] +=1
        else:
            dicio[k] =1
    return dicio