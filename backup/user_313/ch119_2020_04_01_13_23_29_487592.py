def calcula_euler(x,n):

    euler = 1
    contador = 1
    valor = 1
    
    while contador != n and n>1:
        euler = euler + x**contador/valor

        contador = contador + 1
        valor = valor * contador


    return euler