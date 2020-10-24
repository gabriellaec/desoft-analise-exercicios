def numero_no_indice(a):
    resultado = []
    i = 0
    while i < len(a):
        if a[i] == i:
            resultado.append(a[i])
            i += 1
            
        i += 1
    return resultado