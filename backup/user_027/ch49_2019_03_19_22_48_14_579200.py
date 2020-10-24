numero = int(input('Diga o primeiro número: '))
i = 1
lista1 = []
lista2 = []
while numero > 0:
    lista1.append(numero)
    numero = int(input('Digite o próximo número: '))
while i <= len(lista1):
    lista2.append(lista1[(len(lista1) - i)])
    i += 1
print(lista2)