def medias_por_inicial(x):
    y={}
    soma=0
    cont=cont+1
    for k,v in x.items():
        if k[0] not in y:
            y[k[0]]=v
        cont=cont+1
        else:
            soma=soma+v
            y[k[0]]=soma/cont
    return y
        
            