def acha_bigramas(palavra):
    i=1
    lista=[]
    while i<len(palavra):
        while palavra[i] and palavra[i-1] not in lista:
            lista.append(palavra[i]+palavra[i-1])
            i+=1
    return lista