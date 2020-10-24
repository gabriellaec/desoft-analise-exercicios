def acha_bigramas (string):
    lista=[]
    for i in range(0, len(string)-1):
        lista.append(string[i]+string[i+1])
    return lista