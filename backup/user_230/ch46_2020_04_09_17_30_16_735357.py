
def  numero_no_indice(lista):
    nova_lista=[]
    for i in range(len(lista)):
        if lista[i]==i:
            nova_lista.append(lista[i])
    return nova_lista