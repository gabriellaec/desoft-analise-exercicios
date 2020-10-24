a = float(input())
b = float(input())
c = float(input())
print('Mês: 1, Valor: R${0:.2f}' .format(a*(1 + c) + b))
t = 2
valor = d
while t <= 24:
    valor = valor*(1 + c)
    valor = valor + b
    print('{1:.2f}' .format(valor))
    t += 1
ganho = valor - (a + 23*b)
print('{0:.2f}' .format(ganho))

