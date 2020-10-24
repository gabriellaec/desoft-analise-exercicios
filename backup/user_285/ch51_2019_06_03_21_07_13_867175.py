def estritamente_crescente(lista):
    lista_crescente=[]
    for i in range(len(lista)+1):
        if lista[i]<lista[i+1]<lista[i+2]:
            lista_crescente.append(lista[i])
    return lista_crescente
        