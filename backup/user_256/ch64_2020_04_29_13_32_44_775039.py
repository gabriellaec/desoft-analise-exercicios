def acha_bigramas(palavra):
    i=0
    lista = []
    while i<len(palavra)-1:
        bigramo = palavra[i] + palavra[i+1]
        if not bigramo in lista:
            lista.append(bigramo)
        i+=1
    return lista
     
        