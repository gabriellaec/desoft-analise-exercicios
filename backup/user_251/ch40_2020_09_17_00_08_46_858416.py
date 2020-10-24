n = 3
lista = [0]*n
def soma_valores(lista):
    n = 3
    resultado = 0
    while n:
        resultado += lista[n]
        n += 1
    return resultado
print(soma_valores(lista))
   