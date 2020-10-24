def zera_negativos(valores):
    i = 0
    a = valores[i]
    while i:
        i = i + 1
        if valores[i]<0:
            valores[i] = 0
    return a  
        
