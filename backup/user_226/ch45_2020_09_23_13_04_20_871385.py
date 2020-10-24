lista = []

while True:
    numero = int(input("digite um numero"))
    if numero > 0:
        lista.append(numero)
    else:
        break

i = len(lista) - 1

while i >= 0:
    print(lista[i])
    i -= 1