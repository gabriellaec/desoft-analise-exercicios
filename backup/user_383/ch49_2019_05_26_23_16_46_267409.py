
lista_vazia = []

n = int(input('Digite um numero: '))

while n > 0:
    lista_vazia.append(n)
    n = int(input('Digite um numero: '))

lista_vazia.reverse()
print(lista_vazia)