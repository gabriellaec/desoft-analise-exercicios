numero = int(input('Digite um número inteiro positivo: '))

lista_numeros = []

while numero > 0:
    lista_numeros.append(numero)
    numero = int(input('Digite outro número: '))

for i in lista_numeros:
    if i == 0:
        print(-i)