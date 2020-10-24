def acha_bigramas(string):
    lista=[]
    i=1
    while i<len(string):
        lista.append(string[i-1]+string[i])
        i+=1
    return lista