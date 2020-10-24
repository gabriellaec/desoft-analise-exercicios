distance = int(input(""))
if distance < 201:
    preco = distance/2
if distance > 200:
    preco = ((distance-200)*0.45)+100.00
print("{0:.2f}".format(preco))