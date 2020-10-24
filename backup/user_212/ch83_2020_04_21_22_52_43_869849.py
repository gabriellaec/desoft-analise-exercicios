def medias_por_inicial(dici_notas):
    quant={}
    media={}
    for k,v in dici_notas.items():   #k= nome #v=média
        
        if (dici_notas[[k][0]]) in media:
            media[dici_notas[[k][0]]] += v
            quant[dici_notas[[k][0]]] +=1
        elif dici_notas[[k][0]] not in media:
            media[dici_notas[[k][0]]] = v
            quant[dici_notas[[k][0]]]= 1 

    saida={}
    for k,v in media.items():
        q=quant[k]
        saida[k]=v/q
    return saida
    
        
            
            