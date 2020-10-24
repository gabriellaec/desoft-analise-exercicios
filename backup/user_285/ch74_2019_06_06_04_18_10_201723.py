def conta_bigramas(palavra):
    contador1=0
    contador2=2
    listabigramas=[]
    listaocorrencias=[]
    while contador1<len(palavra):
        if palavra([contador1:contador2]) not in listabigramas:
            listabigramas.append(palavra[contador1:contador2])
            ocorrencia=1
        if palavra([contador1:contador2]) in listabigramas:
            ocorrencia+=1
        contador1+=1
        contador2+=1
    return [listabigramas,listaocorrencias]
                    
    
                
        
    
                                 
        