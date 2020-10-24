def numero_no_indice(lista):
    i=0
    nova=[]
    while i< len(lista):
        if lista[i]==i:
            nova.append(i)
            i+=1
        else:
            i+=1
    return (nova)