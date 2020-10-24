def estritamente_crescente(n):
    lista = []
    i = 0
    lista.append(n[0])
    while i+1 < len(n):
        if n[i+1] > n[i]:
            lista.append(n[i+1])
        i += 1
    return lista