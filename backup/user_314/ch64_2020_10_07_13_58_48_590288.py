def acha_bigramas(str):
    lista=[]

    i=0
    
    while(i<len(str)-1):

        x=str[i]+str[i+1]

        if not x in lista:
            lista.append(x)
       
        i+=1


    return lista