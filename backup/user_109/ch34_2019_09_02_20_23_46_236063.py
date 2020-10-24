x = float(input('Insira o valor do seu depósito: '))
y = float(input('Insira o valor da taxa de rendimento em porcentagem: '))
z = y/100
n = 0
inicial = x
lista_valores = []

while n < 24:
    valor = x*(1+z)
    lista_valores.append(valor)
    x = valor
    n += 1
    print("{0:.2f}".format(x))


print('{:.2f}'.format(x - inicial))