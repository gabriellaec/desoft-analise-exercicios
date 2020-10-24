soma = 0
while True:
    numero = int(input('Escreva um número:'))
    if numero != 0:
        soma += numero
    else:
        print(soma)
        break