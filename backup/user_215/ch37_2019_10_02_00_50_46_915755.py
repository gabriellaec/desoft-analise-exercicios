def lista_primos(n):
    lista = []
    x = 1
    while len(lista) < n:
        for i in range(2,2000000):
            if x % i != 0:
                lista.append(x)
                x += 1
            else:
                x += 1