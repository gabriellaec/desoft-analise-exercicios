lista = []
programa = True
while programa:
    numeros = int(input('digite um número inteiro: '))
    if numeros <= 0:
        programa = False
    else:
        lista.append(numeros)
lista.sort(reverse = True)
print(lista)