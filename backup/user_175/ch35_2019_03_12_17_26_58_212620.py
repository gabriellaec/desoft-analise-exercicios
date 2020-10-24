a = float(input())
b = float(input())
c = float(input())
d = a*(1 + c) + b
print('Mês: 1, Valor: R${0:.2f}' .format(d))
t = 2
valor = d
while t <= 24:
    valor = valor*(1 + c)
    valor = valor + b
    print('Mês: {0}, Valor: R${1:.2f}' .format(t, valor))
    t += 1
ganho = valor - (a + 23*b)
print('Total ganho com juros: R${:.2f}' .format(ganho))

