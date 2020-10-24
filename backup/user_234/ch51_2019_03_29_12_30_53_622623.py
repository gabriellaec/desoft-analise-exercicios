def estritamente_crescente(lista):
    lista_cresc=[]
    i=1
    num_lista=len(lista)
    if num_lista == 0:
        return []
    lista_cresc.append(lista[0])
    maior = lista[0]
    while i < num_lista:
        if lista[i] > maior:
            maior = lista[i]
            lista_cresc.append(lista[i])
            i+=1
        else:
            i+=1
    return lista_cresc