def conta_letras(string):
    dicio = {}
    lista = []
    for i in range(len(string)):
        lista.append(string[i])
        
    for i in lista:
        if i in dicio:
            dicio[i] += 1
        else:
            dicio[i] = 1
            
    return dicio