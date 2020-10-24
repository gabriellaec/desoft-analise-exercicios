def estritamente_crescente(lista):
    lista2 = [0]
    for i in lista:
        if i > lista2[-1:][0]:
            lista2.append(i)
            
    return lista2
