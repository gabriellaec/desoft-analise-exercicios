def zera_negativos(valores):
    num_valores = len(valores)
    i = 0
    while i<num_valores:
        if valores[i]<0:                      #termo i da lista
             valores[i]=0                     #recebe o valor de 0
        i+=1 
    return valores
        
    