numeros = []
n = int(input("Digite um número inteiro positivo (0 ou negativo para terminar): "))
while n > 0:
    numeros.append(n)
    n = int(input("Digite um número inteiro positivo (0 ou negativo para terminar): "))
i = len(numeros) - 1
while i >= 0:
    print(numeros[i])
    i -= 1