def estritamente_crescente(x):
    i = 0
    lista = [x[0]]
    maior = x[0]
    while i < len(x):
        if x[i] > maior:
            lista.append(x[i])
            maior = x[i]
        i += 1
    return lista
        
        