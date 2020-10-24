lista = [0]*5
lista[0] = 1
i = 1
while i < 5:
    lista[i] = lista[i-1] + 2
    i += 1
def soma_valores(lista):
    n = 0
    resultado = 0
    while n < 10:
        resultado += lista[n]
        n += 1
    return resultado
print(soma_valores(lista))
        
   