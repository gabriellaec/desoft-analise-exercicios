lista = []
numero = int(input('Digite um número: '))
while numero != 0:
    lista.append(numero)
    numero = int(input('Digite um número: '))
print(sum(lista))