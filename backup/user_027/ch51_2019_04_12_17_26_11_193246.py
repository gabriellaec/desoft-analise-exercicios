def estritamente_crescente(x):
    lista = [x[0]]
    maior = x[0]
    for i in range(len(x)):
        if x[i] > maior:
            lista.append(x[i])
            maior = x[i]
    return lista