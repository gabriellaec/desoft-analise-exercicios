def calcula_pi(n):
    lista = []
    i = 1
    while i <= n:
        lista.append(6/(i**2))
        i += 1
    return (sum(lista)**0.5)