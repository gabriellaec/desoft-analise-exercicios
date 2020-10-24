def numero_no_indice(valores):
    i = 0 
    lista = []
    while i < len(valores):
        if i == valores[i]:
            lista.append(i)
        i += 1
    return lista
    
