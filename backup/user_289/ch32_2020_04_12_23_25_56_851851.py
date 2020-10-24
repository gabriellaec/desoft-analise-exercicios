def lista_primos(n):
    lista_n = []
    for i in range(2, len(lista_n) + 1):
        if i == 2:
            lista.append(i)
        else:
            contador = 3
            while contador < i:
                if i % contador != 0:
                    contador += 1   
            lista_n.append(i)
    return lista_n