numeros_positivos = []
numeros = int(input("Digite um numero positivo: "))
while numeros > 0:
    numeros_positivos.append(numeros)
    numeros = int(input("Digite outro numero positivo: "))

numeros_inversos = numeros_positivos[::-1]

print(numeros_inversos)
