
lista = []

a = 1
while a > 0:
    a = int(input('Digite um número: '))
    lista.append(a)
    
del lista[-1]

i = len(lista) - 1
while i >= 0:
    print(lista[i])
    i -= 1