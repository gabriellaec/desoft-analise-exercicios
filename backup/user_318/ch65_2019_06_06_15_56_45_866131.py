def acha_bigramas(string):
    lista=[]
    i=0
    while i<len(string):
        lista.append(string[i:i+2])
        i+=1
    return lista