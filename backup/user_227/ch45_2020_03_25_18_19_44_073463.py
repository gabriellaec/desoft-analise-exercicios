lista = []
numero = int(input("Digite um numero: "))

while not numero <= 0:
    lista.append(numero)
    numero = int(input("Digite um numero: "))

if numero <= 0:
    print(lista[::-1])