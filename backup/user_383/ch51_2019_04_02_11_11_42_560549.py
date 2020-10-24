def estritamente_crescente(lista_numeros):
    cont=0
    while cont<len(lista_numeros):
        lista_numeros.sort()
        cont+=1
    return lista_numeros