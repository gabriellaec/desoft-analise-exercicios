lista = []
lista_invertida = []

while True:
    numero = int(input())
    if numero <= 0:
        break
    lista.append(numero)

while len(lista) > 0:
    lista_invertida.append(lista[-1])
    del lista[-1]

print(lista_invertida)