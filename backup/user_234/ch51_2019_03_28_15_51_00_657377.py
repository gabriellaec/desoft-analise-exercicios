
def estritamente_crescente(lista):
    lista_cresc=[]
    i=1
    num_lista=len(lista)
    lista_cresc.append(lista[0])
    while i < num_lista:
        if lista[i]>lista[0] and lista[i]>lista[i-1]:
            lista_cresc.append(lista[i])
            i+=1
        else:
            i+=1
    return lista_cresc