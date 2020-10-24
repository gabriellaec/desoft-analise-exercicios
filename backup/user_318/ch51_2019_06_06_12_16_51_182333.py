def estritamente_crescente(lista):
    nova_lista=[]
    while i<len(lista):
        if lista[i] >= lista[i-1]:
            nova_lista.append(i)
            i+=1
        else:
            i+=1
    return nova_lista
            
            