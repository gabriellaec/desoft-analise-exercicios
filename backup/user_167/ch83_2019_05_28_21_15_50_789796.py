def medias_por_inicial (x):
    saida={}
    cont={}
    for k,v in x.items():
        letra=k[0]
        if letra not in saida:
            saida[letra]=v
            cont[letra]=1
        else:
            cont[letra]+=1
            saida[letra]+=v
    for k in saida:
        saida[k]=saida[k]/cont[k]
    return saida
    
        
            
        
            
        
     
     
        
        