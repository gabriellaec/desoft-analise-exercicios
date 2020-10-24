def por inicial(dici_notas):
    quant={}
    medias={}
    for k,v in dici_notas.items():   #k= nome #v=média
        k[0]=letra_inicial
        if letra_inicial in medias:
            media[letra_inicial] += v
            quant[letra_inicial] +=1
        elif letra_inicial not in medias:
            media[letra_inicial] = v
            quant[letra_inicial]= 1 

    saida={}
    for k,v in media.items():
        q=quant[k]
        saida[k]=v/q
    return saida
    
        
            
            