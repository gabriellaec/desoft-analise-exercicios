numero = int(input('Digite um numero: '))
lista = [numero]
while numero > 0:
    numero = int(input('Digite um numero: '))
    if numero > 0:
        lista.append(numero)

print(lista[::-1])