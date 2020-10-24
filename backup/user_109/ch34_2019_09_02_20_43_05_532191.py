x = float(input())
y = float(input())
z = y
n = 0
inicial = x

while n < 24:
    valor = x*(1+z)
    x = valor
    print("{0:.2f}".format(x))
    n += 1


print('{:.2f}'.format(x - inicial))