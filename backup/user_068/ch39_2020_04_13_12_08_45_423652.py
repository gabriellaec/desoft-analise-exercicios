
    conta_maior = 0
    numero_maior = 0
    while 1 < n < 1000:
        cont = 0 
        while i > 1:
        if n % 2 ==0:
            n = n/2
        else:
            n = 3*n + 1
        cont += 1
        if cont>conta_maior:
            conta_maior = cont
            numero_maior = n
print(numero_maior)

