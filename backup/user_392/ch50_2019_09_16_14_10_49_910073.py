def numero_no_indice(x):
    i = 0
    lista = []
    while i < len(x):
        if i == x[i]:
            lista.append(i)
        i += 1
    return lista 
        
            
        
        