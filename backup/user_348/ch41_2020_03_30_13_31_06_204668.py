def zera_negativos(valores):
    i = 0
    while i < len(valores):
        i = i + 1
        if valores[i]<0:
            valores[i] = 0
    return valores  
        
