dist = float(input("Distancia: "))

if dist <= 200.00:
    preco = 0.50*dist
else:
    preco = (0.50*200.00)+((dist-200.00)*0.45)

print "{:.2f}".format(preco)