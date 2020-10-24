def estritamente_crescente(lista):
    if lista== []:
        return []
    lista_estritamente_crescente= []
    lista_estritamente_crescente.append(lista[0])
    maximo= lista[0]
    i= 0
    while i < len(lista):
        if lista[i] > maximo:
            lista[i]= maximo
            i= i + 1
            lista_estritamente_crescente.append(lista[i])
            
        else:
            i= i + 1
        
    return lista_estritamente_crescente