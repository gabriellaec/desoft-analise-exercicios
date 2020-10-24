def encontra_maximo (matriz):
    #modular matriz
    linha =0
    max_linha =[]
    while linha < len(matriz):
        maximo = 0
        i=0
        while i<3:
            if abs(matriz[linha][i]) >= maximo:
                maximo =abs(matriz[linha][i]) 
            i+=1  
        max_linha.append(maximo)
        linha +=1     
    norma_infinita = 0
    j=0
    while j<3:
        if norma_infinita <= max_linha[j]:
            norma_infinita = max_linha[j]
        j+=1
        
    return norma_infinita