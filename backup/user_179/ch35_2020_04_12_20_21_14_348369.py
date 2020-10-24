numero = int(input('numero: '))
lista = []
lista.append(numero)
while numero != 0:
    numero = int(input('numero: '))
    lista.append(numero)
print(sum(lista))