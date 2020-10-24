def acha_bigramas(string):
    lista=[]
    i=0
    while i<len(string):
        if string[i:i+2] not in lista and len(string[i:i+2]
            lista.append(string[i:i+2])
        i+=1
    return lista