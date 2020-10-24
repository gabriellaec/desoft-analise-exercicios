def conta_ocorrencias (lista1):
    dicio={}
    for i in lista1:
        if i not in dicio:
            dicio[i]=1
        else:
            dicio[i]+=1
    return dicio