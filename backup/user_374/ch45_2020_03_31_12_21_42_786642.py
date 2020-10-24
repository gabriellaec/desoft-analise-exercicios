a = int(input('Digite um número '))
lista = []
while a > 0:
    lista.append(a)
    a = int(input('Digite um número '))

lista2 = []
i = len(lista)
x = 0
while i >= 0:
    lista2.append(lista[i-1])
    i = i - 1
    x +=1


del lista2[x-1]
print(lista2)