def medias_por_inicial(dicionario):
    d={}
    l=[]
    c=1
    for chaves, notas in dicionario.items():
        if chaves[0] not in d:
            d[chaves[0]]=notas
        else:
            c+=1
            d[chaves[0]]+=(notas)/2
    return d
            
            
     
       
    