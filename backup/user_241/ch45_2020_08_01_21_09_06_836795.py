x = int(input('Digite um número positivo: '))
lista = []
while x > 0:
        lista.append(x)
        x = int(input('Digite um número positivo: '))
if x <= 0:
    y = lista.reverse()
    print(y)