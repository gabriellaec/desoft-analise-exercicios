numeros = int(input('digite um numero: '))
numerosd = []
while True:
    if numeros > 0:
        numerosd.append(numeros)
        numeros = int(input('digite um numero: '))
    elif numeros <= 0:
        print(numerosd[::-1])
        break
