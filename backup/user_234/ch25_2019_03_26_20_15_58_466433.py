dist = float(input("Distancia: "))

if dist <= 200.00:
    preco = 0.500*dist
else:
    preco = (0.500*200.00)+((dist-200.00)*0.4500)

print(preco)