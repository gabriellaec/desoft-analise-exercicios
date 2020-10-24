a = float(input())
b = float(input())
c = float(input())
d = a*(1 + c) 
print('{0:.2f}' .format(d))
t = 2
valor = d
soma= 0
while t <= 24:
    valor = valor*(1 + c)
    valor = valor + b
    print('{1:.2f}' .format(valor))
    t += 1
ganho = valor - a - 23*b
print('{:.2f}' .format(ganho))

