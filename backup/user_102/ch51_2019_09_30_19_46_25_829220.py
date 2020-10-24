def estritamente_crescente(x):
    i = 1
    resultado=[]
    resultado.append(x[0])
    while i<len(x):
        if x[i-1] < x[i]:
            resultado.append(x[i])
        i += 1
    return resultado