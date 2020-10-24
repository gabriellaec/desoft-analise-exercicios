def acha_bigramas(string):
    lista=[]
    n=len(string)
    for i in range(0,n-1):
        lista.append(string[i]+string[i+1])
    return lista