def estritamente_crescente(lista):
    nova_lista=set[]
    nova_lista.append(lista[0])
    for i in range(len(lista)):
        if lista[i+1]>lista[i]:
            nova_lista.append(lista[i+1])
    return nova_lista
        