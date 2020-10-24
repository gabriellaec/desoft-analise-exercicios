lista_invertida = []
digite_numero = int(input('Digite um número:'))
lista_invertida.append(digite_numero)
while digite_numero > 0:
    digite_numero = int(input('Digite um número:'))
    lista_invertida.append(digite_numero)
lista_invertida.reverse()
print(lista_invertida)