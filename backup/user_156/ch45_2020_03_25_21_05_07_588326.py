lista = []

y = 1

while y > 0:
    x = int(input("Digite numeros inteiros positivos:"))
    if x > 0:
        lista.append(x)
    else:
        y = 0

print(lista[::-1])
