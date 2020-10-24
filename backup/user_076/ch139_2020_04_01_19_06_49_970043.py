def arcotangente(x,n):
    contador = 0 
    expoente = 1 
    y = 0
    while contador < n:
        if contador % 2 = 0:
            y = y + (x**expoente)/expoente
        if contador % 2 != 0:
            y = y - (x**expoente)/expoente
        expoente +=2
        contador +=1
    return y