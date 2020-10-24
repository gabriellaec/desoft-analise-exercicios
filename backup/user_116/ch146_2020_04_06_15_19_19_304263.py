def conta_ocorrencias(lista):
    i=0
    u=0
    contador=0
    
    dicionario={}
    while i<len(lista):
        if u<len(lista):
            if lista[i]==lista[u]:
                contador+=1
                u+=1

            else:
                u+=1
        else:
            
            dicionario[lista[i]]=contador
            contador=0
            u=0
            i+=1
    return dicionario
   