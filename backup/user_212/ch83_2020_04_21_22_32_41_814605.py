def medias_por_inicial(dici_notas):
    quant={}
    media={}
    for k,v in dici_notas.items():   #k= nome #v=média
        letra_inicial=k[0]
        if letra_inicial in media:
            media[letra_inicial] += v
            quant[letra_inicial] +=1
        elif letra_inicial not in media:
            media[letra_inicial] = v
            quant[letra_inicial]= 1 

    saida={}
    for k,v in media.items():
        q=quant[k]
        saida[k]=v/q
    return saida
    
        
            
            