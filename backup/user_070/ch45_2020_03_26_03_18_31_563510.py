lista = []
n = int(input('digite inteiros positivos: '))
while n < 0:
    lista.append(n)
    n = int(input('digite inteiros positivos: '))
l = len(lista)
while l != 0:
    print(lista[l-1])
    l -= 1