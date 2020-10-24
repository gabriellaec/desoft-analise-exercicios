pica = True
lista_numeros
while pica:
    numero = int(input('Digite números inteiros positivos: '))

    if numero <= 0:
        pica = False

    else:
        lista_numeros.append(numero)

