a = float(input())
b = float(input())
c = float(input())
t = 1
valor = a
while t <= 24:
    valor = valor*(1 + c)
    print('{:.2f}' .format(valor))
    valor = valor + b
    t += 1
ganho = valor - a - 23*b
print('{:.2f}' .format(ganho))