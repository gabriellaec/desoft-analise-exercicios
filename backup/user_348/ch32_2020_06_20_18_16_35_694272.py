def lista_primos (n):
    lista = []
    contador = 0
    j = 1
    while contador < n:
        if j ==2:
            lista.append(j)
            contador += 1
        elif j ==3:
            lista.append(j)
            contador += 1
        else:
            for i in range (4, j):
                if (j%2 !=0) and (j%i != 0):
                    lista.append(j)
                    contador += 1
                    j = j + 1
        j = j + 1
    lista.sort(reverse=True)
    return lista