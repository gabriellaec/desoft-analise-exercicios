d = int(input('KM: '))

if d>200:
    preco = 200*0.5 + (d-200)*0.45
else:
    preco = d*0.5

print("{0:.2f}".format(preco))