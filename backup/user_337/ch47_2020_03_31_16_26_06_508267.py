
def estritamente_crescente(n):
    lista = [n]
    t = 0
    for i in n:
        if i > n[t]:
            lista.append(i)
        t += 1
    return lista