def estritamente_crescente(lista):
    nova_lista=[]
    a=0
    for i in range(len(lista)):
        nova_lista.append(lista[0])
        if lista[i+1]>lista[i] and lista[i+1]>nova_lista[a]:
            nova_lista.append(lista[i+1])
            a+=1
    return nova_lista