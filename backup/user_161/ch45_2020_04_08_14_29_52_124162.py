lista = []
while True:
    numero = int(input("Numero? "))
    if numero <= 0:
        break
    else:
        lista.append(numero)

i = len(lista)-1
while i >=0:
    print(lista[i])
    i -= 1