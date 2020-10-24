x = int(input('Digite um número positivo: '))
lista = []
for i in x:
    if i > 0:
        lista.append(x)
    if i < 0:
        y = lista.reverse()
        print(y)