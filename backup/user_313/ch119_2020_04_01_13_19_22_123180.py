def calcula_euler(x,n):

    euler = 1
    fatorial = 1
    contador = 1
    
    while contador != n and n>1:
        euler = euler + x**contador/fatorial

        contador = contador + 1
        fatorial = fatorial * 1


    return euler