def estritamente_crescente(lista):
    i = 1
    list = []
    while i < len(lista):
        if lista[i] > lista[i - 1]:
            list.append(lista[i])
            i = i+1
        else:
            i = i + 1
    return list
    
        
    