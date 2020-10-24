def estritamente_crescente(lista_numeros):
    lista_vazia=[]
    cont=0
    maior=0
    lista_vazia.append(lista_numeros[cont])
    while cont<len(lista_numeros):
        if lista_numeros[cont] > maior:
            lista_vazia.append(lista_numeros[cont])
            maior=lista_numeros[cont]
        cont+=1
    return lista_vazia