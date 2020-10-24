def estritamente_crescente(lista):
    lista_crescente=[]
    for i in range(len(lista)):
        if lista[i]<lista[i+1]:
            lista_crescente.append(lista[i])
            lista_crescente.append(lista[i+1])
    return lista_crescente
        