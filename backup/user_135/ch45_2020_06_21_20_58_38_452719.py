int numero
lista = []
lista_invertida = []

while numero > 0:
    numero = int(input())
    lista.append(numero)

while len(lista) > 0:
    lista_invertida.append(lista[-1])
    del lista[-1]

print(lista_invertida)