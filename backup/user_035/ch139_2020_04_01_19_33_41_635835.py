def arcotangente(x, n):
    contador = 0
    i = 1
    resultado = 0
    resultado2 = 0
    while contador<n and n>1:
        resultado1 = resultado2 + ((x**i)/i) - ((x**(i+2))/(i+2)) 
        i +=2
        contador +=2
    return resultado