def acha_bigramas(palavra):
    lista_bigramas = []
    i=0
    while i < (len(palavra)-1):
        bigrama = palavra[i]+palavra[i+1]
        if bigrama not in lista_bigramas:
            lista_bigramas.append(bigrama)
        i+=1
    return lista_bigramas
