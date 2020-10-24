i=0

lista = []
termo1 = 1

while i < 100:
    termo2 = termo1/(2**i)
    lista.append(termo2)
    i += 1

soma = 0
j=0

while j < 100:
    soma += lista[j]
    j += 1

print(soma)