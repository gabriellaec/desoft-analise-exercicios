def fatorial(a):
    y = True
    contador = 1
    x = 1
    while y:
        x = x * contador
        contador = contador + 1
        if contador > a:
            return(x)
            y = False