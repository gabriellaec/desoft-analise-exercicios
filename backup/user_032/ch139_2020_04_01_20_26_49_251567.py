def arcotangente(x,n):
    #intercalando positivo e negativo
    valor = 1
    act = 0
    if -1 < x and x < 1:
        while valor <= n:
            #positivo:
            act = act + (x**valor)/valor
            valor = valor + 2
            #negativo:
            act = act - (x**valor)/valor
            valor = valor + 2
        return act
