a = float(input())
b = float(input())
c = float(input())

t = 1
valor = a

while t <= 24:
    valor = valor*(1 + c)
    print('Mês: {0}, Valor: R${1:.2f}' .format(t, valor))
    valor = valor + b
    t += 1
    
ganho = valor - a - 23*b
print('Total ganho com juros: R${:.2f}' .format(ganho))