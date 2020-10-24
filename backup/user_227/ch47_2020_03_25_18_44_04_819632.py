def numero_no_indice(lista):
    i = 1
    while i < len(lista):
        a=1
        while lista[i] <= lista[i-a] :
            a+=1            
            del lista[i]
        i += 1
    
    return lista