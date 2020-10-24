def acha_bigramas(string):
    i=0
    lista2=[]
    while i< len(string):
        if (string[i],string[i+1]) not in lista2:
            lista2.append(string[i], string[i+1])
        i+=1
    return lista2
        