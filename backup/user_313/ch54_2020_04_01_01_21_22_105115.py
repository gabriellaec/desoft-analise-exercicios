def calcula_fibonacci(n):
    lista = [0]*n

    if len(lista) == 0:
        return lista   
    
    elif len(lista) == 1:
        lista[0] = 1
        return lista

    else:
        lista[0] = 1
        lista[1] = 1
        

        contador = 2

        while contador != n:

            lista[contador]=lista[contador-1]+lista[contador-2]

            contador = contador + 1

        return lista