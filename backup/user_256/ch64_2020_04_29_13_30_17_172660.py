def acha_bigramas(palavra):
    i=0
    lista = []
    while i<len(palavra):
        bigramo = palavra[i] + palavra[i+1]
        if not bigramo in lista:
            lista.append(palavra[i,i+1])
        i+=1
    return lista
     
        