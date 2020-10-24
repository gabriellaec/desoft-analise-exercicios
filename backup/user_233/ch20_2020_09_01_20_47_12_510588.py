distancia = float(input())

if distancia >= 200: preco = (distancia - 200)  * 0.45 + 100
else: preco = distancia * 0.5

print("%.2f" % preco)