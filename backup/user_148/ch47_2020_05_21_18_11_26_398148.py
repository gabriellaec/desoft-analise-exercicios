def estritamente_crescente(lista):
    lista2 = []
    if len(lista) == 0:
        return lista
    i = 0
    while i<len(lista):        
        if lista[i+1] > lista[i]:
            lista2.append(lista[0])
            lista2.append(lista[i+1])
            i+=1
        return lista2
