def filtra_positivos(reais):
    positivos = []
    i = 0
    while i < len(reais):
        if reais[i] > 0:
            positivos.append(reais[i])
        
        i += 1
    
    return positivos