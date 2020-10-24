def primos_entre(a,b):
    lista = {}
    p = 0
    while a <= p <= b:
        if p%1 == 0 or p%p == 0:
            lista.append(p)
        else:
            break
        p += 1
        return lista
    