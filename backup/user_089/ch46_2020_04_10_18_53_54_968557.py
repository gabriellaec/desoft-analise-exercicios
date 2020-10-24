def numero_no_indice(x):
   
    soma = []
    
    i = 0
    while i < len(x):
        if x[i] == i:
            soma.append(x[i])
            i = i + 1
        else:
            i = i + 1
    return soma
