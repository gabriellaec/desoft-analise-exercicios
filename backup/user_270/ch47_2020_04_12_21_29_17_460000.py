def estritamente_crescente(lista):
    newLista= []
    index=0
    if lista:
        newLista.append(lista[0])
    for i in lista:
        if i>newLista[index]:
            newLista.append(i)
            index +=1
    return newLista