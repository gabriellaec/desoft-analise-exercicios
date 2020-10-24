def primos_entre(n1, n2):
    lista_n = list(range(2, 1000))
    lista_p = list(range(2, 1000))

    if n1 == 2 and n2 == 3:
        return 2

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
    lista_p.insert(0, 3)
    lista_p.insert(0, 2)
    qnt = lista_p[n1:n2]

    return len(qnt)