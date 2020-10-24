def filtra_positivos (numeros):
    valores_pos = []
    i=0
    n=len(numeros)
    while i<n:
        if numeros[i]>0:
            valores_pos.append(numeros[i])
        i+=1
    return valores_pos
a = [-1,-3,4]
b = filtra_postivos(a)