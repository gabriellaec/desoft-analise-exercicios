def estritamente_crescente(lista):
    nova_lista=[]
    nova_lista.append(lista[0])
    for i in range(len(lista)):
        if lista[i+1]>lista[i] and lista[i]>=nova_lista[i]:
            nova_lista.append(lista[i+1])
    return nova_lista