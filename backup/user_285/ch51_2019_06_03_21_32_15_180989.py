def estritamente_crescente(lista):
    lista_crescente=[]
    i=0
    lista_crescente.append(lista[0])
    while i <len(lista):
        if lista[i]<lista[i+1]:
            lista_crescente.append(lista[i+1])
        i+=1
    return lista_crescente
        