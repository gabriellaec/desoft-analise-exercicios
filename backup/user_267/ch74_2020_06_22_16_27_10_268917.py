def conta_bigramas(string):
    dicio_ocorrencias = {}
    lista = []
    for i in range(len(string)):
        lista.append(string[i]+string[i+1])
        for a in lista:
            if a not in dicio_ocorrencias:
                dicio_ocorrencias[a] = 1
            else:
                dicio_ocorrencias[a] += 1
    return dicio_ocorrencias
                      
        
        