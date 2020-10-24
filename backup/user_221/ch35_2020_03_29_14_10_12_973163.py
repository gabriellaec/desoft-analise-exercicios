def soma_valores(lista):
    i = 0
    s = 0
    lista = []
    numero = float(input('Diga um numero: '))
    while numero != 0:
        numero = float(input('Diga um numero: '))
        lista.append(numero)
        s += lista[i]
        i += 1
    if numero == 0:
        return s
