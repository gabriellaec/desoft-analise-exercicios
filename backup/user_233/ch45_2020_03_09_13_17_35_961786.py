lista = []

while True:
    num = int(input())
    if num <= 0: break
    lista.append(num)

lista_inv = range(len(lista))

for i in range(len(lista)):
    lista_inv[-i + 1] = lista[i]

print(lista_inv)