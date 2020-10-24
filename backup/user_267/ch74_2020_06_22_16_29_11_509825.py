def conta_bigramas(string):
    dicio_ocorrencias = {}
    lista = []
    for i in range(0,len(string)-1):
        lista.append(string[i]+string[i+1])
        for a in lista:
            dicio_ocorrencias[a] = lista.count(a)
    return dicio_ocorrencias
                      
        
        