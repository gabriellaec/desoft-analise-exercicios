def conta_letras(string):
    dicio = {}
    lista = []
    for i in range(len(string)):
        lista.append(a[i])
        
    for i in dicio:
        if i in dicio:
            dicio[i] += 1
        else:
            dicio[i] = 1
            
    return dicio