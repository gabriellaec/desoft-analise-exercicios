numeros = []

while True:
    numero = float(input('Qual número deseja somar? '))
    numeros.append(numero)
    if numero == 0:
        break
soma = 0

print(sum(numeros))