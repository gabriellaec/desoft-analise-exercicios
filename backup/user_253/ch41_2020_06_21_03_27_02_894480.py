def zera_negativos(lista):
    i=0
    while i< len(lista):
        if lista[i]>lista[i+1]:
            lista.pop(i+1)
        i+=1
    print (lista)
    