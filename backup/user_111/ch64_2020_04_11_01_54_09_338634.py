def acha_bigramas(palavra):
    i=0
    lista=[]
    while i<len(palavra):
        while palavra[i+1] and palavra[i] not in lista:
            lista.append(palavra[i+1]+palavra[i])
            i+=1
    return lista