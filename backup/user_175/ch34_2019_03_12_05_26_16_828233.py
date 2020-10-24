a = float(input())
b = float(input())
t = 1
num = 1
while (t <= 24):
    valor = a*(1 + b*t)
    t += 1 
    print('Mês: {0} Valor: R${1:.2f}' .format(num, valor))
    num += 1
print('Valor total ganho: {0:.2f}' .format(valor - a))