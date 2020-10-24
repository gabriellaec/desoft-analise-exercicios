def lista_primos (n):
    lista = []
    j = 0
    while j < n:
        if j == 2:
            lista.append(j)
        for j in range (3, n):
            if (j%2!=0):
                lista.append(j)
            i = 1
            while i<j:
                if j%i != 0:
                    lista.append(j)
                i = i + 2
        j = j + 1
    return lista