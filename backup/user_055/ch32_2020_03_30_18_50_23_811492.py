ddef lista_primos(n):
    if n == 0:
        return []
    lista = [2]
    i = 2
    while len(lista) < n:
        n_primo = 3
        if n_primo % 2 == 0 or n_primo % i == 0:
            break
        if i == (n_primo - 1):
            lista.append(n_primo)
    n_primo += 1
    i += 1
    return lista