def estritamente_crescente(lista):
       i = 0
    lista2 = []
    k=True
    while i <len(lista) and k:
        if i == 0:
            lista2.append(lista[i])
        elif lista[i-1] < lista[i]:
            lista2.append(lista[i])
        
        else:
            k=False
        i+=1

    return lista2
        