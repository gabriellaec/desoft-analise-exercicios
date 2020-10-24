x = float(input('Insira o valor do seu depósito: '))
y = float(input('Insira o valor da taxa de rendimento em porcentagem: '))
z = y/100
n = 0

lista_valores = []

while n < 24:
    valor = x*(1+z)
    lista_valores.append(valor)
    x = valor
    n += 1

lucro = lista_valores[23] - lista_valores[0]

print(lista_valores)
print('O valor do seu lucro em 24 meses será: {}'.format(lucro))