def lista_primos(n):
    lista_n = list(range(2, 10000))
    lista_p = list(range(2, 10000))

    for i in lista_n:
        for c in range(2, i):
            if i % c == 0:
                lista_p.remove(i)
                break

    return lista_p [0:n]