def numero_no_indice(lista):
    lista = [0,1,2,3]
    i = 0
    lista2 = []
    while i < len(lista):
        if lista[i] == i:
            lista2.append(i)
        i+=1
    return lista2