lista = []
numero = int(input('Digite o número: '))
while numero != 0 and numero > 0:
    lista.append(numero)
    numero = int(input('Digite o número: '))
lista_reversa = []
for e in range lista[-1::-1]:
    lista_reversa.append(e)
print(lista_reversa)

