def estritamente_crescente(x):
    lista = []
    maior = x[0]
    lista.append(maior)
    i = 1
    while i < len(x):
        if maior < x[i]:
            maior = x[i]
            lista.append(maior)
        i+=1  
    return lista