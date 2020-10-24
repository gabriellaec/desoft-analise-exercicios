distancia = "Qual a distancia em km?"
if distancia <200:
    preco = 200*0.5
    print (preco)
else:
    preco = 200*0.50 + (distancia-200) * 0.45
    print (preco)