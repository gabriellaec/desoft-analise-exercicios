def primos_entre(a, b):
    lista_p = []
    p = a
    while p <= b:
        primo = True
        i = 2
        while i < p:
            if p % i == 0:
                primo = False
                break
            i += 1
        if primo:
            lista_p.append(p)
        p += 1
    return lista_p