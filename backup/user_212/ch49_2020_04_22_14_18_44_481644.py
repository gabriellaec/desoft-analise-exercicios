def inverte_lista(lista):
    lista_invertida=[]
    tamanho=len(lista)
    menos=1
    for i in range(0,tamanho):
        lista_invertida.append(lista[tamanho-menos])
        menos+=1
    return lista_invertida