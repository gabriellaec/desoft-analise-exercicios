def substracao_de_listas (lista1,lista2):
    listafinal = lista1
    i=0
    while i <= len(lista1):
        if i in lista2:
            listafinal.remove(i)
        i+=1
    return listafinal