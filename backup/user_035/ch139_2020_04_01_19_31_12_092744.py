def arcotangente(x, n):
    contador = 0
    i = 1
    resultado = 0
    resultado2 = 0
    while contador<n and n>1:
        resultado1 = resultado2 + ((x**i)/i) 
        i +=2
        resultado2 = resultado1 - ((x**i)/i)
        contador +=2
        i +=2
    return resultado