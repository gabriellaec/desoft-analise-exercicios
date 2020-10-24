a = float(input())
b = float(input())
valor = a
t = 1
num = 1
while (t < 25):
    valor = valor*(1 + b)
    t += 1 
    print('Mês: {0} Valor: R${1:.2f}' .format(num, valor))
    num += 1
valor_ganho = valor - a
print('Valor total ganho: R${:.2f}' .format(valor_ganho))