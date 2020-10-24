def calcula_euler(x,n):

    euler = 0
    fatorial = 1
    contador = 1
    
    while contador != n and n>1:
        euler = euler + 1 + x + x**contador/fatorial

        contador = contador + 1
        fatorial = fatorial * 1


    return euler