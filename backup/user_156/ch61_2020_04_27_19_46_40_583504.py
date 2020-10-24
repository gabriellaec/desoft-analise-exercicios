def filtra_positivos(entrada):
    saida = []
    
    for i in range(0,len(entrada)):
        if entrada[i] > 0:
            saida.append(entrada[i])
            
    return saida
            
