distancia = input("Qual distância deseja ser percorrida?")
if distancia <= 200:
    preco = distancia * 0.5
    print preco
else: 
    preco = 100 + 0.45 * (distancia -200)
    print preco