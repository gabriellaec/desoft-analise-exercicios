numero = input('Qual é o número: ')
lista = []
while numero != 0:
    lista.append(numero)
    numero = input('Qual é o número: ')
print(sum(lista))