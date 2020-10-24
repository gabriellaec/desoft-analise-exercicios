def calcula_euler(x,n):

    contador = 2
    fatorial = 1
    
    while contador != n:
         
        elevado = x ** contador
        fatorial = fatorial * contador

        resultado = 1 + x + elevado/fatorial

        contador = contador + 1

    return(resultado)