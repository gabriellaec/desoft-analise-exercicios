def acha_bigramas(palavra):
    i=0
    lista_vazia=[]
    while i < len(palavra)-1:
        bigrama = palavra[i] + palavra[i+1]
        lista_vazia.append(bigrama)
     	i+=1
    return lista_vazia