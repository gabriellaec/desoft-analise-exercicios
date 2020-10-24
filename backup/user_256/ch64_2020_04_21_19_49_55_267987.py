def acha_bigramas(palavra):
    i=0
    lista = []
    while i<len(palavra):
        if not palavra[i,i+1] in lista:
            lista.append(palavra[i,i+1])
        i+=1
    return lista
     
        