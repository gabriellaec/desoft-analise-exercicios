def acha_bigramas(palavra):
    lista=[]
    i=0
    while(i<len(palavra)-1):
        if(palavra[i]+palavra[i+1] not in lista):
            lista.append(palavra[i]+palavra[i+1])
            i=+1
        else:
            i+=1
    return lista
       