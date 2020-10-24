numero = float(input('Escolha um número: '))
lista_numero = []
while numero > 0:
    lista_numero.append(numero)
    numero = float(input('Escolha um numero: '))
if numero <= 0:
    print (lista_numero[: : -1])
