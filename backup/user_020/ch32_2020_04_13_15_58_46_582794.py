def lista_primos(n):
    lista = []
    i = 1
    impar = 3
    for i in range(len(lista)
        i += 1
    if i <= 1:
        return False
    if i%2 == 0:
        if i == 2:
            lista.append(i)
        else:
            return False
    else:
        if i % impar == 0:
            return False
        else:
            impar += 2
            lista.append(i)
            
        
    