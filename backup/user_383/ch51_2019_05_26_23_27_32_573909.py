def estritamente_crescente(lista_numeros):
    i=0
    lista_vazia=[]
    maior=0
    while i<len(lista_numeros):
        if lista_numeros[i] > maior:
            lista_vazia.append(lista_numeros[i])
            maior = lista_numeros[i]
        i+=1
    return lista_vazia