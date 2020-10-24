def estritamente_crescente(lista):
    newlist=[lista[0]]
    i=0
    while i<len(lista)-1:
        if lista[i+1]>newlist[i]:
            newlist.append(lista[i+1])
        i+=1
    return newlist