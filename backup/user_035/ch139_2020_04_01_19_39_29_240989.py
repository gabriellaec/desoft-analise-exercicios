def arcotangente(x, n):
    contador = 0
    i = 1
    resultado = 0
    while contador<n and n>1:
        resultado = resultado + ((x**i)/i) - ((x**(i+2))/(i+2)) 
        i +=2
        contador +=1
        resultado = resultado - ((x**(i+2))/(i+2)) 
        i +=2
        contador +=1
    return resultado