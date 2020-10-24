num = int(input("Digite numeros: "))
lista = []

while num > 0:
    lista.append(num)
    num = int(input("Digite outros numeros: "))

print(lista[::-1])