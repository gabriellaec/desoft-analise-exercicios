def conta_ocorrencias (lista):
    dicio={}
    for palavra in lista:
        if palavra in dicio:
            dicio[palavra]+=1
        else:
            dicio[palavra]=1
    return dicio