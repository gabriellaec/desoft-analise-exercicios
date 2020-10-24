def conta_bigramas(string):
    dicio = {}
    lista = []
    for i in range(len(string)):
        lista.append(string[i:i+2])
        
    for i in lista:
        if i in dicio:
            dicio[i] += 1
        else:
            dicio[i] = 1
    dicio.pop()    
    return dicio