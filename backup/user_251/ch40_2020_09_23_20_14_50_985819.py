def soma_valores(a):
    indice = 0
    resultado = 0
    while indice < len(a):
        resultado += a[indice]
        indice += 1
    return resultado

print(soma_valores([1, 2, 5]))
   