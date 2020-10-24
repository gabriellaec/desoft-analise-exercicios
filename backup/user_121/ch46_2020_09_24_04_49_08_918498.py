def numero_no_indice(lista):
    i=0
    nova_lista=[]
    while i<len(lista):
        if lista[i]==i:
            resultado=nova_lista.append(i)
        i+=1
    return nova_lista