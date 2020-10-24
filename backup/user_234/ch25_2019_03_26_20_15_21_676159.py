dist = int(input("Distancia: "))

if dist <= 200:
    preco = 0.50*dist
else:
    preco = (0.50*200)+((dist-200)*0.45)

print(preco)