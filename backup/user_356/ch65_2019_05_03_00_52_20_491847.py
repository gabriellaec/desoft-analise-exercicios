def acha_bigramas(string):
    lista=[]
    n=len(string)
    for i in range(0,n-1):
        if string[i]+string[i+1] not in lista:
            lista.append(string[i]+string[i+1])
    return lista