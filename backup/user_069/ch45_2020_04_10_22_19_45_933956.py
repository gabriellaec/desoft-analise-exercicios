lista = []
while True:
    n = int(input('Digite um número inteiro: '))
    if n > 0:
        lista.append(n)
    else:
        break
lista.reverse()
print(lista)