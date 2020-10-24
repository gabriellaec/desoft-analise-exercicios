def calcula_euler(x, n):
    i = 2
    j = 2
    euler = 1 + x
    fatorial = 1
    while j < n:

        fatorial = fatorial * j
        funcao = (x**i)/fatorial

        euler += funcao

        i+=1
        j+=1

    return funcao