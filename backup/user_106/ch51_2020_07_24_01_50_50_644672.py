def primos_entre(a, b):
    lista_p = []
    p = a
    while p <= b:
        i = 2
        while i < p:
            if p % i == 0:
                primo = False
            i += 1
        if primo:
            lista_p.append(p)
        p += 1
    return lista_p