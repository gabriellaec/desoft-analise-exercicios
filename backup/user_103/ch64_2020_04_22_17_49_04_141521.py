def acha_bigramas(string):
    i=1
    lista2=[]
    while i< len(string):
        if (string[i-1]+string[i]) not in lista2:
            lista2.append(string[i]+ string[i-1])
        i+=1
    return lista2
        