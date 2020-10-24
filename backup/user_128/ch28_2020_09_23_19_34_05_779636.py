lista = [1] * 100

i = 0
soma = 0

while i < len(lista):
    lista[i] = lista[i] * 1/2
    i += 1

for n in lista:
    soma += n

print(soma)