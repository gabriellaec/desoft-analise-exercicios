def estritamente_crescente(x):
    i = 0
    resultado=[]
    while i<len(x):
        if x[i] < x[i+1]:
            resultado.append(x[i])
        i += 1
    return resultado