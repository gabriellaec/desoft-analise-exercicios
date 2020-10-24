def primos_entre(n1, n2):
    lista_n = list(range(2, 1000))
    lista_p = list(range(2, 1000))

    for i in lista_n:
        for c in range(2, i):
            if i % c == 0:
                lista_p.remove(i)
                break

            elif i < n1:
                lista_p.remove(i)
                break

            elif i > n2:
                lista_p.remove(i)
                break
    if n1 > 2:
        lista_p.remove(2)
    qnt = len(lista_p)
    return qnt