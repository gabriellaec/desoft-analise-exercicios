lista = []
numero = int(input('Digite o número: '))
while numero != 0 and numero > 0:
    lista.append(numero)
    numero = int(input('Digite o número: '))
lista_reversa = lista[::-1]
print(lista_reversa)

