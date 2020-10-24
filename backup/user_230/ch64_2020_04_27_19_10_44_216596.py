def acha_bigramas (string):
    lista=[]
    for i in range(0, len(string)):
        bigrama=string[i]+string[i+1]
        lista.append(bigrama)
    return lista