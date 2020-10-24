def estritamente_crescente(x):
    lista = [x[0]]
    maior = x[0]
    for i in range(0,len(x)):
        if x[i] > maior:
            lista.append(x[i])
            maior = x[i]
    return lista