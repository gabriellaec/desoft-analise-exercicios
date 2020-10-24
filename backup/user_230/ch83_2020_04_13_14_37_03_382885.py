def medias_por_inicial(dicio):
    novo_dicio=dict()
    dicio_cont=dict()
    for i in dicio:
        if i[0] not in novo_dicio:
            novo_dicio[i[0]]=dicio[i]
            dicio_cont[i[0]]=1
        else:
            novo_dicio[i[0]]+=dicio[i]
            dicio_cont[i[0]]+=1
    for c,v in novo_dicio.items():
        novo_dicio[c]=v/dicio_cont[c]
    return novo_dicio
            
         
            
        