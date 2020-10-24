def lista_primos(n):
    if n == 0:
        return []
    lista = [2]
    primo = 3
    while len(lista) < n:
        i = 0
        while i < primo:
            i += 1
            if primo % i == 0:
                break
            if i == primo:
                lista.append(primo)
        primo += 1
    return lista