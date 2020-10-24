def fatorial(n):
    contador = 1
    resultado = 1
    while contador<=n:
        conta = contador*resultado
        resultado +=conta
        contador +=1
    return resultado
x = fatorial(6)
print(x)