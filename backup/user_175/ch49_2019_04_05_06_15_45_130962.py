numero = int(input('Digite o primeiro número: '))

lista1 = []
lista2 = []

i = 1

while numero > 0:
    lista1.append(numero)
    numero = int(input('Digite o próximo número: '))
    
print('{}'.format(lista1))

while i <= len(lista1):
    lista2.append(lista1[(len(lista1) - i)])
    i += 1
    
print('{}'.format(lista2))