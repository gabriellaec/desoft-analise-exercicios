def positivo(lista10):
    lista0 = []
    for i in lista10:
        if i<0:
            i = i*-1
            lista0.append(i)
        else:
            lista0.append(i)
            pass
    return lista0
def encontra_maximo(lista):
    lista1 = positivo(lista[0])
    lista2 = positivo(lista[1])
    lista3 = positivo(lista[2])
    lista_final = [max(lista1),max(lista2),max(lista3)]
    print(lista)
    print(max(lista_final))
    return max(lista_final)
    