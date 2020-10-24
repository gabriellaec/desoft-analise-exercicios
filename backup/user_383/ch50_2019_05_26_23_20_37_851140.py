def numero_no_indice(lista_numeros):
    i=0
    lista_vazia=[]
    while i < len(lista_numeros):
        if lista_numeros[i] == i:
            lista_vazia.append(lista_numeros[i])
        i+=1
    return lista_vazia
