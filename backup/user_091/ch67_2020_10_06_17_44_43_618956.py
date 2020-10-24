def aunos_impares(lista):
    lista_nova=[]
    i=1
    while i<len(lista)-1:
        lista_nova.append(lista[i])
        i+=2
    return lista_nova
    