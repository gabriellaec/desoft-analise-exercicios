lista = []

numero = int(input('digite um numero: '))

while numero>0:
    lista.append(numero)
    numero = int(input('digite um numero: '))
else:
    print(lista[::-1])