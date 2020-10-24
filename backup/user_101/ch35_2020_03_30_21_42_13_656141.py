num = int(input('Qual número? '))

lista = []
lista.append(num)

while num != 0:
    num = int(input('Qual número? '))
    lista.append(num)

soma_numeros = sum(lista)
print (soma_numeros)