def lista_primos (n):
    lista = []
    j = 2
    while j < n:
        if j ==2:
            lista.append(j)
        for i in range (3, j, 2):
            if (j%2 !=0):
                lista.append(j)
            elif(j%i != 0):
                lista.append(j)
    j = j + 1
    return lista