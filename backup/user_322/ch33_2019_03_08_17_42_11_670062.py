lista = [0] * 100
i = 0
while i < 100:
    lista[i] = (1/2**i)
    i = i + 1
    sum(lista)
print(sum(lista))