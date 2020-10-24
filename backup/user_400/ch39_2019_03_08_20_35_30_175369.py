i = int(input())
lista = []
t = 0
soma = 0
while i != 0:
    lista.append(i)
    i = int(input())
while t < len(lista):
    soma += lista[t]
    t += 1
print(soma)

    