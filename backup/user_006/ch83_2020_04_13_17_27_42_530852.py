def medias_por_inicial(dicio):
    dicio2={}
    listaL=[]
    a=1
    for i in dicio:
        if i[0] not in listaL:
            listaL.append(i[0])
            dicio2[i[0]]=dicio[i]
        else:
            a=a+1
            dicio2[i[0]]=(dicio2[i[0]]+dicio[i])/a
    return dicio2