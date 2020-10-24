def arcotangente(x,n):
    valor = 1  #eleva o x e/ou divide o número
    act = 0   #arcotangente inicial = 0
    if -1 < x and x < 1:   #intervalo de x
        while valor <= n:
            #intercalando positivo e negativo
            #positivo:
            act = act + (x**valor)/valor
            valor = valor * 2
            #negativo:
            act = act - (x**valor)/valor
            valor = valor + 2
        return act