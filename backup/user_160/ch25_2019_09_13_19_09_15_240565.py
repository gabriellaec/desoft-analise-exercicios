distancia = "Qual a distancia em km?"
if distancia <= 200:
    preço = 200*0.50
    return preco
else:
    preço = 200*0.50 + (distancia-200) * 0.45
    return preco