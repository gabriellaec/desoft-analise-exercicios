def filtra_positivos(numeros_reais):
    i = 0
    positivos = []
    while i<len(numeros_reais):
        if numeros_reais[i] > 0:
            positivos.append(numeros_reais[i])           
            return positivos