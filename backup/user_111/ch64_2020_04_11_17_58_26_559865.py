def acha_bigramas(palavra):
    i=1
    lista=[]
    while i<len(palavra):
        if (palavra[i-1]+palavra[i]) not in lista:
            lista.append(palavra[i-1]+palavra[i])
        i+=1
    return lista