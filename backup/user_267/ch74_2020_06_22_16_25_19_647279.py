def conta_bigramas(string):
    dicio_ocorrencias = {}
    dicio_new = {}
    for i in range(len(string)):
        dicio_ocorrencias[i] = (string[i]+string[i+1])
        for a in dicio_ocorrencias:
            if a not in dicio_new:
                dicio_new[a] = 1
            else:
                dicio_new[a] += 1
    return dicio_ocorrencias
                      
        
        