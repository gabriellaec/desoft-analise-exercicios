def numero_no_indice(x):
    i = 0
    resultado=[]
    while i<len(x):
        if x[i] == i:
            resultado.append(i)
        i += 1
    return resultado