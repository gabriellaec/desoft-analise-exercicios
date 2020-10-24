def lista_primos(n):
    lista_de_numeros = list(range(3, 10 * 5))
    lista_de_primos = list(range(3, 10 * 5))
    n = len(lista_de_primos)
    for i in lista_de_numeros:
        for b in range(2, i):
            if i % b == 0:
                lista_de_primos.remove(i)
                break
    return lista_de_primos