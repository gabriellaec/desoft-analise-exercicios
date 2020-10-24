lista = []
num = int(input("Insira numeros na lista"))

while num > 0:
    lista.append(num)
    num = int(input("Insira numeros na lista"))

print(lista[::-1])