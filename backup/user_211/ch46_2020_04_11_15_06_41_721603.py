def estritamente_crescente(lista):
    crescente=[]
    crescente.append(lista[0])
    i=1
    while(i<len(lista)):
        if lista[i]>lista[i-1]:
            crescente.append(lista[i])
        
        else:
             break
        i+=1
    return crescente