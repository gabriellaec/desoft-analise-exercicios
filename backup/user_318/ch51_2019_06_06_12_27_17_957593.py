def estritamente_crescente(lista):
    nova_lista=[]
    i=0
    nova_lista.append(lista[0])
    while i<len(lista):
        if lista[i+1] >= lista[i]:
            nova_lista.append(lista[i+1])
            i+=1
        else:
            del(lista[i])
            i+=1
    return nova_lista
            
            