def lista_primos(n):
    lista = []
    i = 1
    impar = 3
    while n < len(lista):
        if i % 2 == 0:
            if i == 2:
                lista.append(i)
        else:
            if i % impar != 0:
                  lista.append(i)
                
    i += 1
    impar += 2