def filtra_positivos (numeros):
    valores_pos = []
    i = 0
    n = len(numeros)
    while i < n:
        if numeros [i] > 0:
            valores_pos.append(numeros[i])
        i+=1 
    return valores_pos
a = [1,2,3,-5,-6,-8,-10]
b = filtra_positivos(a)