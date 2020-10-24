def zera_negativos(x):
    num_valores = len(x)
    lista = [0]*num_valores
    
    for i in range(num_valores):
        if x[i] > 0:
            lista[i] = x[i]
            
    return lista