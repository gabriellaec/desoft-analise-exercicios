def estritamente_crescente(lista):
    i=0
    lista_1=[lista[0]]
    while i<len(lista):
        if lista[i+1]>lista[i]:
            lista_1.append(lista[i+1])
        i+=1