def calcula_fibonacci(F):
    lista=[]
    q=len(lista)
    i=0
    while F>i:
        if i<2:
            lista.append(1)
            i+=1
            continue
        else:
            a=lista[q-1]+lista[q-2]
            lista.append(a)
            i+=1
            continue
    return lista