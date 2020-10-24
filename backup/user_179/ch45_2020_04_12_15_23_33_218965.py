numero = int(input('n: '))
lista = [numero]
while numero > 0:
    numero = int(input('n: '))
    lista.append(numero)

print (lista.reverse())