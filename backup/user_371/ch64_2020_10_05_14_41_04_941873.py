def acha_bigramas(palavra):
    i=0
    lista=[]
    while (len(palavra)-1)>i:
        if palavra[i]+palavra[i+1] not in lista:
            lista.append(palavra[i]+palavra[i+1])
        i+=1
   