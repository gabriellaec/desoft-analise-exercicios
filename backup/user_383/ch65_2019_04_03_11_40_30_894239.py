def acha_bigramas(palavra):
    cont=0
    contador=1
    lista_bigrama=[]
    while cont<len(palavra)-1 and contador>=1:
        contador += 1
        lista_bigrama.append(palavra[cont:contador])
        cont += 1
    return lista_bigrama