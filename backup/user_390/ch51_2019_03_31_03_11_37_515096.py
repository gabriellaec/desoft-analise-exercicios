def estritamente_crescente(lista):
    i=0
    nova= [lista[i]]
    while i<len(lista):
        if lista[i+1]>lista[i]:
            nova.append(lista[i+1])
            i+=1
        else:
            i+=1
    return nova

            