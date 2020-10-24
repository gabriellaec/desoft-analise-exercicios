def encontra_maximo (matriz):
    linha =0
    max_linha =[]
    while linha < 3:
        maximo = 0
        i=0
        while i<3:
        if matriz[linha][i] > maximo:
            maximo = matriz[linha][i] 
        i+=1  
        max_linha.append(maximo)
    linha +=1     
    norma_infinita = max(max_linha)
    return norma_infinita