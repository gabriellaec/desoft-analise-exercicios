def estritamente_crescente(lista):
    lista=[]
    i=0
    while i<(int(len(lista)-1)):
        if (lista[i+1] <= lista[i]):
            (lista.append(lista[i+1]))
        i=i+1
    return (lista)