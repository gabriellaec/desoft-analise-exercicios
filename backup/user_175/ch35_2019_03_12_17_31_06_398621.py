a = float(input())
b = float(input())
c = float(input())
print('{:.2f}' .format(a*(1 + c) + b))
t = 2
valor = d
while (t <= 24):
    valor *= (1 + c)
    valor += b
    print('{:.2f}' .format(valor))
    t += 1
ganho = (valor - (a + 23*b))
print('{:.2f}' .format(ganho))

