def estritamente_crescente(lista):
    nova_lista=[]
    i=0
    while i<len(lista)-1:
        if lista[i+1] >= lista[i]:
            nova_lista.append(lista[i+1])
            i+=1
        elif lista[0] > lista[1]:
            nova_lista.append(lista[0])
            i+=1
        else:
            i+=1
    return nova_lista
            
            