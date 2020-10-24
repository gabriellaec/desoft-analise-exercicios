def numero_no_indice(lista):
    
    resultado = []
    
    for i in range(len(lista)):
        if lista[i] == i: resultado.append(i)
    
    return resultado