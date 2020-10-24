lista = []
numeros = int(input("digite numeros positivos: "))
while numeros > 0:
    lista.append(numeros)
    numeros = int(input("digite numeros positivos: "))
print(lista[::-1])