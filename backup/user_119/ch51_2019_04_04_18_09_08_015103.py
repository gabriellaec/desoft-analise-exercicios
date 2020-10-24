def estritamente_crescente():
    i=1
    p=lista[0]
    nova_lista=[]
    while i<len(lista):
        if lista[i]>p:
            nova_lista.append(lista[i])
            p=i
        i+=1
    return nova_lista