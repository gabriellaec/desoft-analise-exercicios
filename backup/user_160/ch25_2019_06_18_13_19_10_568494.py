distancia = int(input("Qual distância deseja ser percorrida?"))
if distancia <= 200:
    preco = distancia * 0.5
else: 
    preco = 100 + 0.45 * (distancia -200)
print("{0:.2f}".format(preco))