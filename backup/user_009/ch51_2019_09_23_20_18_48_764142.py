def estritamente_crescente(x):
    if len(x) == 0:
        return []
    a = 0
    ultimo_maior = x[0]
    lista = [x[0]]
    while a < len(x):
        if x[a] > ultimo_maior:
            lista.append(x[a])
            ultimo_maior = x[a]
        a +=1
    return lista
