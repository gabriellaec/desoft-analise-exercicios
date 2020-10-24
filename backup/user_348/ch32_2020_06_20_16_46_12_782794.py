def lista_primos (n):
    lista = []
    contador = 0
    j = 2
    while contador < n:
        if j ==2:
            lista.append(j)
            contador += 1
        for i in range (3, j, 2):
            if (j%2 !=0):
                lista.append(j)
                contador += 1
            elif(j%i != 0):
                lista.append(j)
                contador += 1
        j = j + 1
    return lista