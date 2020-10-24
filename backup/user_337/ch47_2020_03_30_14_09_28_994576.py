def estritamente_crescente(n):
    lista = []
    i = 0
    t = 0
    lista.append(n[0])
    while i < len(n):
        if n[i+1] > lista[t]:
            lista.append(n[i+1])
            t += 1
        i += 1
    return lista
