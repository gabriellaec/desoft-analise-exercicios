def estritamente_crescente(n):
    lista = []
    i = 1
    t = 0
    lista.append(n[0])
    while i < len(n):
        if n[i] > lista[t]:
            lista.append(n[i])
            t += 1
        i += 1
    return lista
