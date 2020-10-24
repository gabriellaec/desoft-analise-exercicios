lista = [1] * 100

i = 0
soma = 0
j = 0

while i < len(lista):
    lista[i] = lista[i] * 1/2
    i += 1

while j < len(lista):
    soma += lista[j]
    j += 1

print(soma)