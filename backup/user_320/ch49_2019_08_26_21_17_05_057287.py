lista = []

while True:
    num = int(input('Digite um número: '))
    if num < 1:
        break
    lista.append(num)
print(lista[::-1])