def acha_bigramas(string):
    i=0
    lista=[]
    while i<len(string):
        if string[i:i+2] not in lista and len(string[i:i+2])==2:
            lista.append(string[i:i+2])
            i+=1
        else:
            i+=1
    

    return lista