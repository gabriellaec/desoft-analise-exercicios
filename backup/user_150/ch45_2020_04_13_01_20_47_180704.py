lista_numero = []
numero = int(input('Digite um número inteiro positivo. Se for negativo, ou zero, você para a sequência: '))
while numero > 0:
    lista_numero.append(numero)
    numero = int(input('Digite um número inteiro positivo. Se for negativo, ou zero, você para a sequência: '))

i = len(lista_numero)
while i >= 0:
    print(lista_numero[i])
    i -= 1