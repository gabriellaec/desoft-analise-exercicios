def filtra_positivos(a):
    i = 0
    resultado = []
    while i < len(a):
        if a[i] > 0:
            resultado.append(a[i])
            i += 1
        else:
            i += 1
            
    return resultado