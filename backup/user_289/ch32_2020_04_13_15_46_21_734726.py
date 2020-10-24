def lista_primos(n):
    lista_n = []*n
    i = 2
    while len(lista_n) < n:
        if i == 2:
            lista_n.append(i)
            i += 1
        else:
            contador = 2
            while contador < i:
                if i % contador != 0:
                    contador += 1
                else:
                    i += 1
            lista_n.append(i)
            i += 1
    return lista_n